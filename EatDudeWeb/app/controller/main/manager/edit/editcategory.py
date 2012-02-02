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

editcategory_form = form.Form( 
                             form.Textbox(
                                      'category_name',
                                      form.notnull,
                                      description='category name'
                                      ),
                              form.Dropdown('category_order', [],
                                      description='category order'
                                      )
                             )

class EditCategory:
            
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
                        
                        c = Category()
                        category_count = c.getCount()
                        
                        mcm = MenuCategoryModel.get_by_id(int(id))
                        category_name = mcm.category
                        category_order = mcm.order
                        editcategory_form['category_name'].value = category_name
                        
                        editcategory_form.category_order.args = []
                        for i in range(1,category_count) :
                            if not i == category_order :
                                editcategory_form.category_order.args.append( (i, i) )
                        
                        editcategory_form.category_order.args.insert(0,category_order)
                        
                        nest = main_view.manager.edit.editcategory(editcategory_form,str(mcm.key().id()))
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        
        else:
                return main_view.manager.error()
            
            
            
    
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
               
               validateForm = editcategory_form()
               if not validateForm.validates():
                            nest = main_view.manager.edit.editcategory(validateForm)
                            return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                                  
               else:
                   data = web.input()
                   c = Category()
                   c.update(data.category_name,data.category_id)
                   c.updateOrder(data.category_order, data.category_id)
                            
                   return web.seeother('/manager/menu/view/' + current_menu_id)
                                          
        else:
           return main_view.manager.error()
            
            
            
            