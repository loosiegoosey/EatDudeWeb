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
from web import form
from google.appengine.ext import db
from google.appengine.api import users

from dbModel import *
from app.model.admin.menu import *
from app.model.admin.restaurant import *
from app.model.admin.item import *
from app.model.admin.category import *

from config import admin_view


r = Restaurant()
r_names = r.getRestaurantName()
                
selectRestaurant = form.Form( 
                             form.Textbox(
                                      'menu_name',
                                      form.notnull,
                                      description='menu name'
                                      ),
                             form.Dropdown(
                                      'restaurant_name', 
                                      r_names,
                                      description='restaurant name'
                                           ),
                             form.Hidden(
                                      name='form', 
                                      value='selectRestaurant'
                                           )
                             )


categoryForm = form.Form( 
                        form.Textarea(
                                'add_categories',
                                form.notnull,
                                rows=30,
                                cols=40,
                                description='Add Categories'
                                 ),
                        form.Hidden(
                                name='form', 
                                value='categoryForm'
                                 )
                        )

itemForm = form.Form(
                form.Textbox(
                             'item_name',
                             form.notnull,
                             description='item name'
                                ),
                form.Textbox(
                            'item_desc',
                            form.notnull,
                            description='item desc'
                                ),
                form.Textbox(
                            'item_price',
                            form.notnull,
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

class AddMenu:
    def GET(self):
        
                r = Restaurant()
                r_names = r.getRestaurantName()

                if not r_names :
                    return 'error - add a restaurant - ' 
                else :
                    nest = admin_view.menu_form.index(selectRestaurant)
                    return admin_view.index(nest)
                
            
    def POST(self):
                data = web.input()
                theForm = data.form
                
                validateForm = selectRestaurant()
                if theForm == 'selectRestaurant' :
                           if not validateForm.validates():
                                    nest = admin_view.menu_form.index( validateForm )
                                    return admin_view.index(nest)
                           else:
                                    data = web.input()
                                    m = Menu()
                                    menu_id = m.add(data.menu_name,
                                                    data.restaurant_name
                                                    )
                                    
                                    nest = admin_view.menu_form.categoryForm(categoryForm, menu_id)
                                    return admin_view.index(nest)
                                
                validateForm = categoryForm()
                if theForm == 'categoryForm' :
                          
                          if not data.menu_id == ""  :
                                   menu_id_for_validation = data.menu_id
                        
                          if not validateForm.validates():
                                   nest = admin_view.menu_form.categoryForm( validateForm, menu_id_for_validation )
                                   return admin_view.index(nest)
                          else:
                                   data = web.input()
                                   c = Category()
                                   c.add(data.add_categories,
                                           data.menu_id)
                                   
                                   mcm = Category()
                                   mcm_names = mcm.getCategoryName(data.menu_id)
                                   
                                   nest = admin_view.menu_form.itemForm( itemForm, data.menu_id, mcm_names)
                                   return admin_view.index(nest)
            
                validateForm = itemForm()
                if theForm == 'itemForm' :
                                  mcm = Category()
                                  mcm_names = mcm.getCategoryName(data.menu_id)
                                  if not validateForm.validates() :
                                        nest = admin_view.menu_form.itemForm( validateForm, data.menu_id, mcm_names )
                                        return admin_view.index(nest)
                                  else:
                                        data = web.input()
                                        items = Item()
                                        items.add(data.item_name,
                                                          data.item_desc,
                                                          data.item_price,
                                                          data.item_number,
                                                          data.category_name
                                                  )
                                        
                                        nest = admin_view.menu_form.itemForm( itemForm, data.menu_id, mcm_names)
                                        return admin_view.index(nest)
                    
                    