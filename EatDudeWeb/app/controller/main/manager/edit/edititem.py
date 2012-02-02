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
    
    
edititem_form = form.Form(
                form.Dropdown(
                              'category_id', [],
                              description='category name'),
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
                                ),
                form.Dropdown('item_order', [],
                            description='item order'
                                )
                )

class EditItem:
    
    def GET(self,id):
        re = RestaurantEdit()
    
        menu_id = re.getMenuId()
        c = Category()
        categories = c.getCategory(menu_id)
                        
        item = edititem_form
        edititem_form.category_id.args = []
        for key, value in categories :
                item.category_id.args.append( ( str(key) , value.category ) )
            
        r_id = re.getRestaurantEditId()
        r = RestaurantModel.get_by_id(int( r_id ))
        restaurant_selected = re.isRestaurantSelected()
        r_name_id = re.getRestaurantIdNameList()
        m_name_id = re.getMenuIdNameList()
        
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if(user):   
            
                        i = MenuItemModel.get_by_id(int(id))
                        
                        #category
                        itemCategoryId = i.menucategorymodel.key().id()
                        c = MenuCategoryModel.get_by_id(int(itemCategoryId))
                        c_name = i.menucategorymodel.category
                        item.category_id.args.remove(( str(itemCategoryId) , c_name ))
                        item.category_id.args.insert( 0, ( str(itemCategoryId) , c_name ) )
                        
                        #items
                        edititem_form['item_name'].value = i.itemName
                        edititem_form['item_desc'].value = i.itemDesc
                        edititem_form['item_price'].value = i.itemPrice
                        edititem_form['item_number'].value = i.itemNumber
                        
                        mcm = MenuItemModel.get_by_id(int(id))
                        item_order = mcm.order
                        i = Item()
                        item_count = i.getCount(itemCategoryId)
                        
                        edititem_form.item_order.args = []
                        for i in range(1,item_count) :
                            if not i == item_order :
                                edititem_form.item_order.args.append( (i, i) )
                        
                        edititem_form.item_order.args.insert(0,item_order)
                        
                        nest = main_view.manager.edit.edititem(edititem_form,id)
                        
                        #nest = main_view.manager.error()

                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        
        else:
                return main_view.manager.error()
            
            
            
    
    def POST(self,id):
        re = RestaurantEdit()
    
        menu_id = re.getMenuId()
        c = Category()
        categories = c.getCategory(menu_id)
                        
        item = edititem_form
        edititem_form.category_id.args = []
        for key, value in categories :
                item.category_id.args.append( ( str(key) , value.category ) )
            
        r_id = re.getRestaurantEditId()
        r = RestaurantModel.get_by_id(int( r_id ))
        restaurant_selected = re.isRestaurantSelected()
        r_name_id = re.getRestaurantIdNameList()
        m_name_id = re.getMenuIdNameList()
        
        
        user = users.get_current_user()
        if(user):
                    data = web.input()
                    validateForm = edititem_form()
                    if not validateForm.validates():
                        nest = main_view.manager.edit.edititem(validateForm,data.item_id)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                         data = web.input()
                        
                         items = Item()
                         items.update(data.item_name,
                                        data.item_desc,
                                        data.item_price,
                                        data.item_number,
                                        data.category_id,
                                        data.item_id )
                         
                         items.updateOrder(data.item_order,data.category_id,data.item_id)
                        
                         return web.seeother( '/manager/menu/view/' + menu_id )
                                          
        else:
           return main_view.manager.error()
            
            
            
            
            
            