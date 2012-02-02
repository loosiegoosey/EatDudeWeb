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

from app.model.main.manager.restaurantedit import *
    
    
editrestaurant_form = form.Form(
                form.Textbox(
                                'Name',
                                form.notnull,
                                description='Name',
                                ),
                form.Dropdown('Country',
                                [('us' ,'United States'),
                                ('uk', 'United Kingdom'),
                                ('ca', 'Canada')]),
                form.Textbox(
                                'City',
                                form.notnull,
                                description='City',
                                ),
                form.Textbox(
                                'State',
                                form.notnull,
                                description='State / Province',
                                ),
                form.Textbox(
                                'Address',
                                form.notnull,
                                description='Address',
                                ),
                form.Textbox(
                                'Phone',
                                form.notnull,
                                description='Phone #',
                                )
                    )


editmenu_form = form.Form( 
                        form.Textbox(
                        'menu_name',
                        form.notnull,
                        description='menu name'
                        )
                )

editmenu_form2 = form.Form( 
                        form.Dropdown('Menu',[])
                        )

itemselect_form = form.Form( 
                        form.Dropdown('Item',[])
                        )

editcategory_form = form.Form(
                              form.Dropdown('Category', [])
                              )


class Edit:
    
    
    def GET(self,entity):
    
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if(user):
                    
                    rem = RestaurantEdit()
                    r_id = rem.getRestaurantEditId()
                    m_id = rem.getMenuId()
                    r = RestaurantModel.get_by_id(int( r_id ))
                    restaurant_selected = rem.isRestaurantSelected()
                    r_name_id = rem.getRestaurantIdNameList()
                    m_name_id = rem.getMenuIdNameList()
        
                    editform2 = editmenu_form2()
                    editcat2 = editcategory_form()
                    itemselect2 = itemselect_form()
        
                    if entity=='restaurant' :
                        
                        editrestaurant_form['Name'].value = r.name
                        editrestaurant_form['City'].value = r.city
                        editrestaurant_form['State'].value = r.state
                        editrestaurant_form['Address'].value = r.address
                        editrestaurant_form['Phone'].value = r.phone
                        
                        nest = main_view.manager.edit.restaurant(editrestaurant_form)
                        
                    elif entity=='menu' :
                        
                        menu = Menu()
                        m = menu.getMenuFromParentKey(int(r_id))
                        
                        if not m :
                            return web.seeother('/manager/main/view/' + r_id )
                        else :
                            editform2.Menu.args = []
                            for key,value in sorted(m.iteritems()) :
                                    editform2.Menu.args.append( (str(value.key().id()),value.name) )
                            
                        nest = main_view.manager.edit.menu(editform2)
                        
                    elif entity=='category' :
                        editcategory_form.Category.args = []
                        
                        mm = MenuModel.get_by_id(int(m_id))
                        categories = mm.categories
                        if categories.count() == 0 :
                            return web.seeother('/manager/add/category')
                        else :
                            editcat2.Category.args = []
                            for c in categories :
                                editcat2.Category.args.append( (str(c.key().id()),c.category) )
                        
                        nest = main_view.manager.edit.category(editcat2)
                        
                    elif entity=='item' :
                        
                        editcategory_form.Category.args = []
                        
                        mm = MenuModel.get_by_id(int(m_id))
                        categories = mm.categories
                        if categories.count() == 0 :
                            return web.seeother('/manager/add/category')
                        else :
                            editcat2.Category.args = []
                            for c in categories :
                                editcat2.Category.args.append( (str(c.key().id()),c.category) )
                                
                        nest = main_view.manager.edit.item_categories(editcat2)
                        
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
            
                rem = RestaurantEdit()
                r_id = rem.getRestaurantEditId()
                m_id = rem.getMenuId()
                r = RestaurantModel.get_by_id(int( r_id ))
                restaurant_selected = rem.isRestaurantSelected()
                r_name_id = rem.getRestaurantIdNameList()
                m_name_id = rem.getMenuIdNameList()
        
                editform2 = editmenu_form2()
                editcat2 = editcategory_form()
                itemselect2 = itemselect_form()
                
                if entity=='restaurant' :
                    validateForm = editrestaurant_form()
                    if not validateForm.validates():
                        nest = main_view.manager.add.restaurant(validateForm)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                        data = web.input()
                        
                        rem = RestaurantEdit()
                        r_id = rem.getRestaurantEditId()
                        r = RestaurantModel.get_by_id(int( r_id ))
                        
                        r.name = data.Name
                        r.city = data.City
                        r.phone = data.Phone
                        r.address = data.Address
                        r.state = data.State
                        r.put()
                        
                        if r :
                            c = Country()
                            country_id = c.add(data.Country)
                        
                            s = State()
                            state_id = s.add(data.State,country_id)
                        
                            ci = City()
                            city_id = ci.add(data.City,state_id)
                            
                            #r.addCityModel(restaurant_id,city_id)
                        
                        return web.seeother( '/manager/main/view/'  + r_id)
                        
                elif entity == 'menu' :
                         validateForm = editmenu_form2()
                         if not validateForm.validates():
                             nest = main_view.manager.edit.item_categories(validateForm)
                             return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                         else:
                             data = web.input()
                             return web.seeother('/manager/editmenu/' + data.Menu)
                         
                elif entity == 'category' :
                            validateForm = editcategory_form()
                            if not validateForm.validates():
                                nest = main_view.manager.edit.category(validateForm)
                                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                            else:
                                data = web.input()
                                return web.seeother('/manager/editcategory/' + data.Category )
                         
                elif entity == 'item' :
                           
                            validateForm = editcategory_form()
                            if not validateForm.validates():
                                nest = main_view.manager.edit.item_categories(validateForm)
                                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                            else:
                                data = web.input()
                                
                                for x in data :
                                    if x == 'Category' :
                                        
                                        category_id = data.Category
                                        mcm = MenuCategoryModel.get_by_id(int(category_id))
                                        items = mcm.items
                                        
                                        #add to edit model
                                        rem.addCatId(data.Category)
                                        rem.addCatName(mcm.category)
                                
                                        if items.count() == 0 :
                                            return web.seeother('/manager/add/item')
                                        else :
                                            itemselect2.Item.args = []
                                            for i in items :
                                                itemselect2.Item.args.append( (str(i.key().id()),i.itemName) )
                                        
                                        nest = main_view.manager.edit.select_items(itemselect2)
                                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                    else :
                                         
                                         return web.seeother('/manager/edititem/' + data.Item)
                                
                                
                        
                else :
                        nest = main_view.manager.error()

                
                return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                    sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                          
        else:
           return web.seeother('/')
            
            
            
            
            
            