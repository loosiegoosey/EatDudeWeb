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

from config import main_view
from google.appengine.api import users
from web import form

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

delrestaurant_form = form.Form(
                              form.Textbox(
                              'restaurant',
                              form.notnull,
                              readonly='readonly',
                              description='restaurant : ')
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

class Delete:
    
    def GET(self,entity):
            
            user = users.get_current_user()
            isadmin = users.is_current_user_admin()
            
            if(user):
                    re = RestaurantEdit()
                    rem = re.getRestaurantEditModel()
                    m_id = re.getMenuId()
            
                    current_restaurant_id = rem.current_model_edit_id
                    current_menu_id = rem.current_model_menu_id
                    current_model_name = rem.current_model_name
            
                    restaurant_selected = re.isRestaurantSelected()
                    m_name_id = re.getMenuIdNameList()
                    r_name_id = re.getRestaurantIdNameList()
            
                    editform2 = editmenu_form2()
                    editcat2 = editcategory_form()
                    itemselect2 = itemselect_form()
                    
                    if entity=='restaurant' :
                        
                        delrestaurant_form['restaurant'].value = current_model_name
                        nest = main_view.manager.delete.restaurant(delrestaurant_form,current_restaurant_id)
                        
                    elif entity=='menu' :
                        menu = Menu()
                        re = RestaurantEdit()
                        r_id = re.getRestaurantEditId()
                        m = menu.getMenuFromParentKey(int(r_id))
                        
                        if not m :
                            return web.seeother('/manager/main/view/' + r_id )
                        else :
                            editform2.Menu.args = []
                            for key,value in sorted(m.iteritems()) :
                                    editform2.Menu.args.append( (str(value.key().id()),value.name) )
                                
                        nest = main_view.manager.delete.menu(editform2)
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
                        
                        nest = main_view.manager.delete.category(editcat2)
                          
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
                return main_view.manager.error()
            
            
            
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
        
                editform2 = editmenu_form2()
                editcat2 = editcategory_form()
                itemselect2 = itemselect_form()
                
                if entity=='restaurant' :
                    
                    validateForm = delrestaurant_form()
                    if not validateForm.validates():
                        nest = main_view.manager.delete.restaurant(validateForm)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                         data = web.input()
                         restaurant_id = data.restaurant_id
                         r = Restaurant()
                         r.delete(restaurant_id)
                         
                         return web.seeother( '/user/' )
                     
                elif entity=='menu' :
                        
                    validateForm = editmenu_form2()
                    if not validateForm.validates():
                        nest = main_view.manager.delete.menu(validateForm)
                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                        re = RestaurantEdit()
                        r_id = re.getRestaurantEditId()
                        
                        data = web.input()
                        menu_id = data.Menu
                        m = Menu()
                        m.delete(menu_id)
                        
                        return web.seeother('/manager/main/view/' + r_id)
                        #nest = main_view.manager.delete.menu(editmenu_form2)
                        
                elif entity=='category' :
                    validateForm = editcategory_form()
                    if not validateForm.validates():
                            nest = main_view.manager.delete.menu(validateForm)
                            return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                          sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                    else:
                            re = RestaurantEdit()
                            m_id = re.getMenuId()
                        
                            data = web.input()
                            category_id = data.Category
                            c = Category()
                            c.delete(category_id)
                        
                    return web.seeother('/manager/menu/view/' + m_id)
                    #nest = main_view.manager.delete.category()
                    
                elif entity=='item' :
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
                                        re.addCatId(data.Category)
                                        re.addCatName(mcm.category)
                                
                                        if items.count() == 0 :
                                            return web.seeother('/manager/add/item')
                                        else :
                                            itemselect2.Item.args = []
                                            for i in items :
                                                itemselect2.Item.args.append( (str(i.key().id()),i.itemName) )
                                        
                                        nest = main_view.manager.delete.select_items(itemselect2)
                                        return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                    else :
                                         
                                         re = RestaurantEdit()
                                         m_id = re.getMenuId()
                        
                                         data = web.input()
                                         item_id = data.Item
                                         i = Item()
                                         i.delete(item_id)
                        
                                    return web.seeother('/manager/menu/view/' + m_id)
                                     
                else :
                        #return web.seeother('/user/')
                        nest = main_view.manager.error()
                
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                                          
        else:
           return web.seeother('/')
       
       
       