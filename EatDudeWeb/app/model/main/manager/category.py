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
import operator

from dbModel import *
from app.model.main.manager.restaurantedit import *

from google.appengine.ext import db
from google.appengine.api import users


class Category :
                       
                   def add(self,category):
                       
                       #get order
                       order = Category.getCount(self)
                       
                       #add category
                       rem = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                       menu_id = rem.current_model_menu_id
                   
                       menu = MenuModel.get_by_id(int(menu_id))
                       
                       mcm = MenuCategoryModel()
                       mcm.author = users.get_current_user()
                       mcm.order = order
                       mcm.category = category
                       mcm.active = True
                       mcm.menumodel = menu
                       mcm.put()
                       
                       
                       
                       
                       
                   def update(self,category,category_id):
                       
                       rem = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                       menu_id = rem.current_model_menu_id
                   
                       menu = MenuModel.get_by_id(int(menu_id))
                       
                       mcm = MenuCategoryModel.get_by_id(int(category_id))
                       mcm.author = users.get_current_user()
                       mcm.category = category
                       mcm.active = True
                       mcm.menumodel = menu
                       mcm.put()
                       
                       
                   def getCategory(self,id):
                       out = []
                
                       mm = MenuModel.get_by_id(int(id))
                       category = mm.categories
                       
                       for categories in sorted(category,key=operator.attrgetter('order'), reverse=False):
                            out.append( ( categories.key().id() , categories) )
                            #logging.info(str(categories.key().id()) + ' --- ' + str(categories) )
                        
                       return out
                   
                   def getCategoryNoId(self):
                       rem = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                       out = {}
                       
                       menu_id = 0
                       if rem :
                           menu_id = rem.current_model_menu_id
                       
                           if not menu_id == '0' :
                               mm = MenuModel.get_by_id(int(menu_id))
                               if mm:
                                   category = mm.categories
                                   for categories in category :
                                       out[categories.key().id()] = categories
                            
                       return out
                           
                           
                           
                   def delete(self,id):
                       #delete menu
                       #menu_delete = []
                       #category_delete = []
                       item_delete = []
                       
                       mcm = MenuCategoryModel.get_by_id(int(id))
                       items = mcm.items
                       
                       if items :
                            for z in items :
                                item_delete.append(z.key().id())
                          
                            for item in item_delete :
                                #logging.info('delete item : ' + str(item))
                                mim = MenuItemModel.get_by_id(item)
                                mim.delete()
                                           
                       mcm.delete()
                       
                    
                   def getCount(self):
                        re = RestaurantEdit()
                        menu_id = re.getMenuId()
                        mm = MenuModel.get_by_id(int(menu_id))
                        category_count = mm.categories.count()
                        
                        #plus 1 so no 0's
                        return category_count + 1
                    
                    
                   def updateOrder(self,order,category_id):
                        re = RestaurantEdit()
                        menu_id = re.getMenuId()
                        mm = MenuModel.get_by_id(int(menu_id))
                        cats = mm.categories
                        
                        mcm = MenuCategoryModel.get_by_id(int(category_id))
                        current_order = mcm.order
                        
                        in_case_error_cats = {}
                        for x in cats :
                            in_case_error_cats[x.key().id()] = x.order
                            
                        #logging.info('change ' + str(current_order) + ' order to '  + order)
                        
                        #logging.info('original-order -------------------------------------------------------')
                        #for c in cats :
                             #logging.info(str(c.key().id()) + ' | ' + c.category + ' = order : ' + str(c.order))
                        
                        #logging.info('modified -------------------------------------------------------')
                        
                        
                        for c in cats :
                            try:
                                 #normal = str(c.key().id()) + ' | ' + c.category + ' = order : ' + str(c.order)
                             
                                 if int(current_order) == int(c.order):
                                     #logging.info(normal + '-o-> ' + str(order) )
                                     Category.addUpdatedOrder(self, c.key().id(), int(order))
                              
                                 if int(c.order) < int(current_order) and int(c.order) > int(order) :
                                     logging.info('')  
                                 elif int(c.order) < int(current_order) and not int(c.order) == int(order) :
                                     #logging.info(normal + ' - do nothing1')
                                     logging.info('')
                                 
                                 if int(c.order) < int(current_order) and int(c.order) == int(order):
                                      #logging.info(normal + '-+-> ' + str(int(c.order) + 1) )
                                      Category.addUpdatedOrder(self, c.key().id(), int(c.order) + 1)
                             
                                 if int(c.order) > int(current_order) and int(c.order) > int(order):
                                     #logging.info(normal + ' - do nothing2')
                                     logging.info('')
                                 elif int(c.order) > int(current_order) :
                                     #logging.info(normal + '- - -> ' + str(int(c.order) - 1) )
                                     Category.addUpdatedOrder(self, c.key().id(), int(c.order) - 1)
                                 
                                 if int(c.order) > int(order) and int(c.order) < int(current_order) :
                                     #logging.info(normal + '- -> ' + str(int(c.order) + 1) )
                                     Category.addUpdatedOrder(self, c.key().id(), int(c.order) + 1)
                                     
                            except :
                                for key,value in in_case_error_cats.iteritems() :
                                    Category.addUpdatedOrder(self,key,value)
                                raise
                                
                                
                                
               
                   def addUpdatedOrder(self,id,order):
                            mcm = MenuCategoryModel.get_by_id(int(id))
                            order_if_error = mcm.order
                            mcm.order = order
                            try :
                                mcm.put()
                            except :
                                mcm.order = order_if_error
                                mcm.put()
                                raise
                            
                            
                   def getCategoriesFromParentMenu(self,
                                                                                        id):
                            out = []
                            mm = MenuModel.get_by_id(int(id))
                            
                            #return all categories
                            category = mm.categories
                            for categories in sorted(category,key=operator.attrgetter('order'), reverse=False):
                                out.append(categories)
                            
                            return out
                    
    
    