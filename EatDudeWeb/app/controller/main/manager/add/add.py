'''
    Copyright (C) 2012  Wiley Snyder

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or 
     any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    Any other questions or concerns contact wiley@wileynet.com
'''
import web
import logging

from web import form
from config import main_view
from google.appengine.api import users

from dbModel import *
from google.appengine.ext import db

from app.model.main.user.profile import *

from app.model.main.manager.restaurant import *
from app.model.main.manager.country import *
from app.model.main.manager.city import *
from app.model.main.manager.state import *
from app.model.main.manager.menu import *
from app.model.main.manager.category import *
from app.model.main.manager.item import *

from app.model.main.manager.restaurantedit import *

addrestaurant_form = form.Form(
                        form.Textbox(
                                      'Name',
                                      form.notnull,
                                      description='name of rest'
                                      ),
                        form.Dropdown('Country',
                                       [('us' ,'United States'),
                                        ('uk', 'United Kingdom'),
                                        #('um', 'United States Minor Outlying Islands'),
                                        #('af', 'Afghanistan'),
                                        #('ax', 'Aland Islands'),
                                        #('al', 'Albania'),
                                        #('dz', 'Algeria'),
                                        #('as', 'American Samoa'),
                                        #('ad', 'Andorra'),
                                        #('ao', 'Angola'),
                                        #('ai', 'Anguilla'),
                                        #('aq', 'Antarctica'),
                                        #('ag', 'Antigua and Barbuda'),
                                        #('ar', 'Argentina'),
                                        #('am', 'Armenia'),
                                        #('aw', 'Aruba'),
                                        #('au', 'Australia'),
                                        #('at', 'Austria'),
                                        #('az', 'Azerbaijan'),
                                        #('bs', 'Bahamas'),
                                        #('bh', 'Bahrain'),
                                        #('bd', 'Bangladesh'),
                                        #('bb', 'Barbados'),
                                        #('by', 'Belarus'),
                                        #('be', 'Belgium'),
                                        #('bz', 'Belize'),
                                        #('bj', 'Benin'),
                                        #('bm', 'Bermuda'),
                                        #('bt', 'Bhutan'),
                                        #('bo', 'Bolivia'),
                                        #('ba', 'Bosnia and Herzegovina'),
                                        #('bw', 'Botswana'),
                                        #('bv', 'Bouvet Island'),
                                        #('br', 'Brazil'),
                                        #('io', 'British Indian Ocean Territory'),
                                        #('vg', 'British Virgin Islands'),
                                        #('bn', 'Brunei'),
                                        #('bg', 'Bulgaria'),
                                        #('bf', 'Burkina Faso'),
                                        #('bi', 'Burundi'),
                                        #('kh', 'Cambodia'),
                                        #('cm', 'Cameroon'),
                                        #('cv', 'Cape Verde'),
                                        #('ky', 'Cayman Islands'),
                                        #('cf', 'Central African Republic'),
                                        #('td', 'Chad'),
                                        #('cl', 'Chile'),
                                        #('cn', 'China'),
                                        #('cx', 'Christmas Island'),
                                        #('cc', 'Cocos (Keeling) Islands'),
                                        #('co', 'Colombia'),
                                        #('km', 'Union of the Comoros'),
                                        #('cg', 'Congo'),
                                        #('ck', 'Cook Islands'),
                                        #('cr', 'Costa Rica'),
                                        #('hr', 'Croatia'),
                                        #('cu', 'Cuba'),
                                        #('cy', 'Cyprus'),
                                        #('cz', 'Czech Republic'),
                                        #('cd', 'Democratic Republic of Congo'),
                                        #('dk', 'Denmark'),
                                        #('xx', 'Disputed Territory'),
                                        #('dj', 'Djibouti'),
                                        #('dm', 'Dominica'),
                                        #('do', 'Dominican Republic'),
                                        #('tl', 'East Timor'),
                                        #('ec', 'Ecuador'),
                                        #('eg', 'Egypt'),
                                        #('sv', 'El Salvador'),
                                        #('gq', 'Equatorial Guinea'),
                                        #('er', 'Eritrea'),
                                        #('ee', 'Estonia'),
                                        #('et', 'Ethiopia'),
                                        #('fk', 'Falkland Islands'),
                                        #('fo', 'Faroe Islands'),
                                        #('fm', 'Federated States of Micronesia'),
                                        #('fj', 'Fiji'),
                                        #('fi', 'Finland'),
                                        #('fr', 'France'),
                                        #('gf', 'French Guyana'),
                                        #('pf', 'French Polynesia'),
                                        #('tf', 'French Southern Territories'),
                                        #('ga', 'Gabon'),
                                        #('gm', 'Gambia'),
                                        #('ge', 'Georgia'),
                                        #('de', 'Germany'),
                                        #('gh', 'Ghana'),
                                        #('gi', 'Gibraltar'),
                                        #('gr', 'Greece'),
                                        #('gl', 'Greenland'),
                                        #('gd', 'Grenada'),
                                        #('gp', 'Guadeloupe'),
                                        #('gu', 'Guam'),
                                        #('gt', 'Guatemala'),
                                        #('gn', 'Guinea'),
                                        #('gw', 'Guinea-Bissau'),
                                        #('gy', 'Guyana'),
                                        #('ht', 'Haiti'),
                                        #('hm', 'Heard Island and McDonald Islands'),
                                        #('hn', 'Honduras'),
                                        #('hk', 'Hong Kong'),
                                        #('hu', 'Hungary'),
                                        #('is', 'Iceland'),
                                        #('in', 'India'),
                                        #('id', 'Indonesia'), 
                                        #('ir', 'Iran'),
                                        #('iq', 'Iraq'),
                                        #('xe', 'Iraq-Saudi Arabia Neutral Zone'),
                                        #('ie', 'Ireland'),
                                        #('il', 'Israel'),
                                        #('it', 'Italy'),
                                        #('ci', 'Ivory Coast'),
                                        #('jm', 'Jamaica'),
                                        #('jp', 'Japan'),
                                        #('jo', 'Jordan'),
                                        #('kz', 'Kazakhstan'),
                                        #('ke', 'Kenya'),
                                        #('ki', 'Kiribati'),
                                        #('kw', 'Kuwait'),
                                        #('kg', 'Kyrgyz Republic'),
                                        #('la', 'Laos'),
                                        #('lv', 'Latvia'),
                                        #('lb', 'Lebanon'),
                                        #('ls', 'Lesotho'),
                                        #('lr', 'Liberia'),
                                        #('ly', 'Libya'),
                                        #('li', 'Liechtenstein'),
                                        #('lt', 'Lithuania'),
                                        #('lu', 'Luxembourg'),
                                        #('mo', 'Macau'),
                                        #('mk', 'Macedonia'),
                                        #('mg', 'Madagascar'),
                                        #('mw', 'Malawi'),
                                        #('my', 'Malaysia'),
                                        #('mv', 'Maldives'),
                                        #('ml', 'Mali'),
                                        #('mt', 'Malta'),
                                        #('mh', 'Marshall Islands'),
                                        #('mq', 'Martinique'),
                                        #('mr', 'Mauritania'),
                                        #('mu', 'Mauritius'),
                                        #('yt', 'Mayotte'),
                                        #('mx', 'Mexico'),
                                        #('md', 'Moldova'),
                                        #('mc', 'Monaco'),
                                        #('mn', 'Mongolia'),
                                        #('ms', 'Montserrat'),
                                        #('ma', 'Morocco'),
                                        #('mz', 'Mozambique'),
                                        #('mm', 'Myanmar'),
                                        #('na', 'Namibia'),
                                        #('nr', 'Nauru'),
                                        #('np', 'Nepal'),
                                        #('nl', 'Netherlands'),
                                        #('an', 'Netherlands Antilles'),
                                        #('nc', 'New Caledonia'),
                                        #('nz', 'New Zealand'),
                                        #('ni', 'Nicaragua'),
                                        #('ne', 'Niger'),
                                        #('ng', 'Nigeria'),
                                        #('nu', 'Niue'),
                                        #('nf', 'Norfolk Island'),
                                        #('kp', 'North Korea'),
                                        #('mp', 'Northern Mariana Islands'),
                                        #('no', 'Norway'),
                                        #('om', 'Oman'),
                                        #('pk', 'Pakistan'),
                                        #('pw', 'Palau'),
                                        #('ps', 'Palestinian Territories'),
                                        #('pa', 'Panama'),
                                        #('pg', 'Papua New Guinea'),
                                        #('py', 'Paraguay'),
                                        #('pe', 'Peru'),
                                        #('ph', 'Philippines'),
                                        #('pn', 'Pitcairn Islands'),
                                        #('pl', 'Poland'),
                                        #('pt', 'Portugal'),
                                        #('pr', 'Puerto Rico'),
                                        #('qa', 'Qatar'),
                                        #('re', 'Reunion'),
                                        #('ro', 'Romania'),
                                        #('ru', 'Russia'),
                                        #('rw', 'Rwanda'),
                                        #('sh', 'Saint Helena and Dependencies'),
                                        #('kn', 'Saint Kitts & Nevis'),
                                        #('lc', 'Saint Lucia'),
                                        #('pm', 'Saint Pierre and Miquelon'),
                                        #('vc', 'Saint Vincent and the Grenadines'),
                                        #('ws', 'Samoa'),
                                        #('sm', 'San Marino'),
                                        #('st', 'Sao Tome and Principe'),
                                        #('sa', 'Saudi Arabia'),
                                        #('sn', 'Senegal'),
                                        #('sc', 'Seychelles'),
                                        #('sl', 'Sierra Leone'),
                                        #('sg', 'Singapore'),
                                        #('sk', 'Slovakia'),
                                        #('si', 'Slovenia'),
                                        #('sb', 'Solomon Islands'),
                                        #('so', 'Somalia'),
                                        #('za', 'South Africa'),
                                        #('gs', 'South Georgia and the South Sandwich Islands'),
                                        #('kr', 'South Korea'),
                                        #('es', 'Spain'),
                                        #('pi', 'Spratly Islands'),
                                        #('lk', 'Sri Lanka'),
                                        #('sd', 'Sudan'),
                                        #('sr', 'Suriname'),
                                        #('sj', 'Svalbard and Jan Mayen Islands'),
                                        #('sz', 'Swaziland'),
                                        #('se', 'Sweden'),
                                        #('ch', 'Switzerland'),
                                        #('sy', 'Syria'),
                                        #('tw', 'Taiwan'),
                                        #('tj', 'Tajikistan'),
                                        #('tz', 'Tanzania'),
                                        #('th', 'Thailand'),
                                        #('tg', 'Togo'),
                                        #('tk', 'Tokelau'),
                                        #('to', 'Tonga'),
                                        #('tt', 'Trinidad and Tobago'),
                                        #('tn', 'Tunisia'),
                                        #('tr', 'Turkey'),
                                        #('tm', 'Turkmenistan'),
                                        #('tc', 'Turks and Caicos Islands'),
                                        #('tv', 'Tuvalu'),
                                        #('ug', 'Uganda'),
                                        #('ua', 'Ukraine'),
                                        #('ae', 'United Arab Emirates'),
                                        #('uy', 'Uruguay'),
                                        #('vi', 'US Virgin Islands'),
                                        #('uz', 'Uzbekistan'),
                                        #('vu', 'Vanuatu'),
                                        #('va', 'Vatican City'),
                                        #('ve', 'Venezuela'),
                                        #('vn', 'Vietnam'),
                                        #('wf', 'Wallis and Futuna Islands'),
                                        #('eh', 'Western Sahara'),
                                        #('ye', 'Yemen'),
                                        #('zm', 'Zambia'),
                                        #('zw', 'Zimbabwe'),
                                        #('rs', 'Serbia'),
                                        ('ca', 'Canada')],
                                        description='rest country'),
                        form.Textbox(
                                      'City',
                                      form.notnull,
                                      description='rest city'
                                      ),
                        form.Textbox(
                                      'State',
                                      form.notnull,
                                      description='state/province'
                                      ),
                         form.Textbox(
                                      'Address',
                                      form.notnull,
                                      description='street address'
                                      ),
                        form.Textbox(
                                      'Phone',
                                      form.notnull,
                                      description='rest phone #'
                                      )
                         )


addmenu_form = form.Form( 
                             form.Textbox(
                                      'menu_name',
                                      form.notnull,
                                      description='menu name'
                                      )
                             )

addcategory_form = form.Form( 
                             form.Textbox(
                                      'category_name',
                                      form.notnull,
                                      description='category name'
                                      )
                             )

additem_form = form.Form(
                form.Dropdown(
                              'category_id', []),
                form.Textbox(
                             'item_name',
                             form.notnull,
                             description='item name'
                                ),
                form.Textbox(
                            'item_desc',
                            description='item desc'
                                ),
                form.Textbox(
                            'item_price',
                            description='item price'
                                ),
                form.Textbox(
                            'item_number',
                            description='item number'
                                ),
                form.Hidden(
                            name='form', 
                            value='itemForm'
                                )
                )

class Add:
    
    def GET(self,entity):
            
            user = users.get_current_user()
            isadmin = users.is_current_user_admin()
                    
            if(user):
                
                    re = RestaurantEdit()
                    rem = re.getRestaurantEditModel()
            
                    current_restaurant_id = rem.current_model_edit_id
                    current_menu_id = rem.current_model_menu_id
            
                    restaurant_selected = re.isRestaurantSelected()
                    m_name_id = re.getMenuIdNameList()
                    r_name_id = re.getRestaurantIdNameList()
                    
                    if entity=='restaurant' :
                        nest = main_view.manager.add.restaurant(addrestaurant_form)
                    elif entity=='menu' :
                        nest = main_view.manager.add.menu(addmenu_form)
                    elif entity=='category' :
                        nest = main_view.manager.add.category(addcategory_form)
                    elif entity=='item' :
                        
                         c = Category()
                         categories = c.getCategoryNoId()
                         item = additem_form
                         categoryDict = sorted(categories.iteritems())
                         
                         if not categoryDict :
                             return web.seeother('/manager/add/category')
                         else:
                             #get edit model category
                             cat_name = re.getCatName()
                             cat_id = re.getCatId()
                        
                             item.category_id.args = []
                             #add selection to top
                             if not cat_id == '0' :
                                 item.category_id.args.append( (cat_id , cat_name) )
                             
                             for key, value in categoryDict :
                                 if not str(key) == cat_id :
                                     item.category_id.args.append( ( str(key) , value.category ) )
                            
                             nest = main_view.manager.add.item(additem_form)
                             
                    else :
                        #return web.seeother('/user/')
                        nest = main_view.manager.error()
                        
                    return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        
            else:
                return web.seeother('/')
            
            
    def POST(self,entity):
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
                
        if(user):
                
                re = RestaurantEdit()
                rem = re.getRestaurantEditModel()
            
                current_restaurant_id = rem.current_model_edit_id
                current_menu_id = rem.current_model_menu_id
            
                restaurant_selected = re.isRestaurantSelected()
                m_name_id = re.getMenuIdNameList()
                r_name_id = re.getRestaurantIdNameList()
        
                if entity=='restaurant' :
                    validateForm = addrestaurant_form()
                    if not validateForm.validates():
                        nest = main_view.manager.add.restaurant(validateForm)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                        data = web.input()
                        
                        r = Restaurant()
                            
                        restaurant_id = r.add(data.Name,
                                                            data.Country,
                                                            data.City, 
                                                            data.Phone,
                                                            data.Address, 
                                                            data.State)
                        
                        if r :
                            c = Country()
                            country_id = c.add(data.Country)
                        
                            s = State()
                            state_id = s.add(data.State,country_id)
                        
                            ci = City()
                            city_id = ci.add(data.City,state_id)
                            
                            r.addCityModel(restaurant_id,city_id)
                            
                            rm = RestaurantModel.get_by_id(int(restaurant_id))
                            rm.country_id = str(country_id)
                            rm.state_id = str(state_id)
                            rm.city_id = str(city_id)
                            rm.put()
                        
                        return web.seeother('/user/')
                        
                elif entity == 'menu' :
                         validateForm = addmenu_form()
                         if not validateForm.validates():
                             nest = main_view.manager.add.menu(validateForm)
                             return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                         else:
                             data = web.input()
                             m = Menu()
                             
                             m.add(data.menu_name,
                                   current_restaurant_id)
                             
                             
                             return web.seeother('/manager/main/view/' + current_restaurant_id)
                         
                elif entity == 'category' :
                        validateForm = addcategory_form()
                        if not validateForm.validates():
                            nest = main_view.manager.add.menu(validateForm)
                            return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                                  
                        else:
                            data = web.input()
                            m = Category()
                            m.add(data.category_name)
                            
                            #return web.seeother('/manager/menu/view/' + self.current_menu_id)
                            return web.seeother('/manager/add/category')
                        
                        
                elif entity == 'item' :
                        #del self.categoryDict[:]
                        
                        validateForm = additem_form()
                        if not validateForm.validates():
                            nest = main_view.manager.add.item(validateForm)
                            return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                                  
                        else:
                            data = web.input()
                            re = RestaurantEdit()
                            re.addCatId(data.category_id)
                            item = additem_form
                            
                            #make sure selection moves to top for easy multi adds
                            c = MenuCategoryModel.get_by_id(int(data.category_id))
                            c_name = c.category
                            re.addCatName(c_name)

                            item.category_id.args.insert( 0, ( data.category_id , c_name ) )
                            item.category_id.args.remove(( data.category_id , c_name ))
                            
                            items = Item()
                            items.add(data.item_name,
                                            data.item_desc,
                                            data.item_price,
                                            data.item_number,
                                            data.category_id )
                            
                            return web.seeother('/manager/add/item')
                            
                       
                        
                                          
        else:
           return web.seeother('/')
            
            