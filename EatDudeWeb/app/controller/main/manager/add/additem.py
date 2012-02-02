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

from app.model.main.manager.restaurant import *
from app.model.main.manager.country import *
from app.model.main.manager.city import *
from app.model.main.manager.state import *
from app.model.main.manager.menu import *
from app.model.main.manager.category import *
from app.model.main.manager.item import *

from app.model.main.manager.restaurantedit import *

    
addcategory_form = form.Form( 
                             form.Textbox(
                                      'category_name',
                                      form.notnull,
                                      description='category name'
                                      )
                             )

additem_form = form.Form(
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


class AddItem:
            
    def GET(self,id):
        
        re = RestaurantEdit()
        r_id = re.getRestaurantEditId()
        r = RestaurantModel.get_by_id(int( r_id ))
        restaurant_selected = re.isRestaurantSelected()
        r_name_id = re.getRestaurantIdNameList()
        m_name_id = re.getMenuIdNameList()
        
        cri = re.getRestaurantEditModel()
    
        if cri :
            current_restaurant_id = cri.current_model_edit_id
            current_menu_id = cri.current_model_menu_id
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if(user):
                        
                        #memcache this
                        c = MenuCategoryModel.get_by_id(int(id))
                        cat_name = c.category
                        
                        nest = main_view.manager.add.additem(additem_form,str(id),cat_name)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        
        else:
                return web.seeother('/')
            
            
            
    
    def POST(self,entity):
        
        re = RestaurantEdit()
        r_id = re.getRestaurantEditId()
        r = RestaurantModel.get_by_id(int( r_id ))
        restaurant_selected = re.isRestaurantSelected()
        r_name_id = re.getRestaurantIdNameList()
        m_name_id = re.getMenuIdNameList()
        
        cri = re.getRestaurantEditModel()
    
        if cri :
            current_restaurant_id = cri.current_model_edit_id
            current_menu_id = cri.current_model_menu_id
        
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        if(user):
               
               validateForm = additem_form()
               if not validateForm.validates():
                            nest = main_view.manager.edit.additem_form(validateForm)
                            return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                                  
               else:
                   data = web.input()
                   
                   #memcache this
                   c = MenuCategoryModel.get_by_id(int(data.category_id))
                   cat_name = c.category
                            
                   items = Item()
                   items.add(data.item_name,
                                data.item_desc,
                                data.item_price,
                                data.item_number,
                                data.category_id )
                            
                   nest = main_view.manager.add.additem(additem_form,data.category_id,cat_name)
                   return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                          
        else:
           return web.seeother('/')
       
       
       
       