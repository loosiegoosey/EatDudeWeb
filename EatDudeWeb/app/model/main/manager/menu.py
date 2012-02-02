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

from dbModel import *
from google.appengine.ext import db
from google.appengine.api import users



class Menu:
    
        def add(self,name,id):
                            
                            restaurant = RestaurantModel.get_by_id(int(id))

                            mm = MenuModel()
                            mm.author = users.get_current_user()
                            # date is inserted auto
                            mm.name = name
                            mm.active = True
                            mm.restaurantmodel = restaurant
                            mm.put()
                            # return the menu_id
                            # return mm.key().id()
        
        
        def getMenuFromParentKey(self,id):
                out = {}
                rm = RestaurantModel.get_by_id(int(id))
                menu = rm.menus
 
                for menus in menu:
                        out[menus.key().id()] = menus
                        
                return out
            
            
        def update(self,menu_name,menu_id):
                       
                       mm = MenuModel.get_by_id(int(menu_id))
                       mm.name = menu_name
                       mm.put()
                       
        def delete(self,id):
                       #delete menu
                       #menu_delete = []
                       category_delete = []
                       item_delete = []
                       
                       mm = MenuModel.get_by_id(int(id))
                       if mm :
                           menucategory = mm.categories
                               
                           if menucategory :
                                       for y in menucategory :
                                           #logging.info('delete category : ' + str(y.key().id()))
                                           mcm = MenuCategoryModel.get_by_id(y.key().id())
                                           category_delete.append(y.key().id())
                                           items = mcm.items
                                       
                                           if items :
                                               for z in items :
                                                   #logging.info('delete item : ' + str(z.key().id()))
                                                   item_delete.append(z.key().id())
                               
                                       
                                       
                                       for category in category_delete :
                                           #logging.info('delete category : ' + str(category))
                                           mcm = MenuCategoryModel.get_by_id(category)
                                           mcm.delete()
                          
                                       for item in item_delete :
                                           #logging.info('delete item : ' + str(item))
                                           mim = MenuItemModel.get_by_id(item)
                                           mim.delete()
                                           
                       mm.delete()
    
       
                    
                    
    
    