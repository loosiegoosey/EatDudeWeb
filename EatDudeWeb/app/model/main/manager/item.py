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
from google.appengine.ext import db
from google.appengine.api import users

class Item :
        
                   def add(self,
                                  itemName,
                                  itemDesc,
                                  itemPrice,
                                  itemNumber,
                                  id):
                                        
                                        #get order
                                        order = Item.getCount(self,id)
                       
                                        category = MenuCategoryModel.get_by_id(int(id))
                                        
                                        mim = MenuItemModel()
                                        mim.author = users.get_current_user()
                                        # date is inserted auto
                                        mim.order = order
                                        mim.itemName = itemName
                                        mim.itemDesc = itemDesc
                                        mim.itemPrice = itemPrice
                                        mim.itemNumber = itemNumber
                                        mim.active = False
                                        mim.menucategorymodel = category
                                        mim.put()
                                        
                    
                   def update(self,
                                  itemName,
                                  itemDesc,
                                  itemPrice,
                                  itemNumber,
                                  category_id,
                                  item_id):
                       
                                        category = MenuCategoryModel.get_by_id(int(category_id))
                                        
                                        mim = MenuItemModel.get_by_id(int(item_id))
                                        mim.author = users.get_current_user()
                                        # date is inserted auto
                                        mim.itemName = itemName
                                        mim.itemDesc = itemDesc
                                        mim.itemPrice = itemPrice
                                        mim.itemNumber = itemNumber
                                        mim.active = False
                                        mim.menucategorymodel = category
                                        mim.put()
                                        
                                        
                                        
                                        
                   def getItemsFromCategoryParent(self,id):
                            out = []
                            mcm = MenuCategoryModel.get_by_id(int(id))
                            
                            #return all items
                            item = mcm.items
                            
                            #sorted(feeds, key=operator.attrgetter('timestamp'), reverse=True)
                            for items in sorted(item,key=operator.attrgetter('order'), reverse= False) :
                                out.append(items)
                            
                            return out
                        
                        
                   def delete(self,id):
                       
                        mim = MenuItemModel.get_by_id(int(id))
                        mim.delete()
                
                
                    
                   def getCount(self,cat_id):
                        mcm = MenuCategoryModel.get_by_id(int(cat_id))
                        item_count = mcm.items.count()
                        
                        # + 1 no 0's
                        return item_count + 1
                
                
                
                   def updateOrder(self,order,category_id,item_id):
                        
                        mcm = MenuCategoryModel.get_by_id(int(category_id))
                        items = mcm.items
                        
                        mcm = MenuItemModel.get_by_id(int(item_id))
                        current_order = mcm.order
                        
                        in_case_error_items = {}
                        for x in items :
                            in_case_error_items[x.key().id()] = x.order
                            
                        #logging.info('change ' + str(current_order) + ' order to '  + order)
                        
                        #logging.info('original-order -------------------------------------------------------')
                        #for i in items :
                             #logging.info(str(i.key().id()) + ' | ' + i.itemName + ' = order : ' + str(i.order))
                        
                        #logging.info('modified -------------------------------------------------------')
                        
                        
                        for i in items :
                            try:
                                
                                 #normal = str(i.key().id()) + ' | ' + i.itemName + ' = order : ' + str(i.order)
                             
                                 if int(current_order) == int(i.order):
                                     #logging.info(normal + '-o-> ' + str(order) )
                                     Item.addUpdatedOrder(self, i.key().id(), int(order))
                              
                                 if int(i.order) < int(current_order) and int(i.order) > int(order) :
                                     logging.info('')  
                                 elif int(i.order) < int(current_order) and not int(i.order) == int(order) :
                                     #logging.info(normal + ' - do nothing1')
                                     logging.info('')
                                 
                                 if int(i.order) < int(current_order) and int(i.order) == int(order):
                                      #logging.info(normal + '-+-> ' + str(int(i.order) + 1) )
                                      Item.addUpdatedOrder(self, i.key().id(), int(i.order) + 1)
                             
                                 if int(i.order) > int(current_order) and int(i.order) > int(order):
                                     #logging.info(normal + ' - do nothing2')
                                     logging.info('')
                                 elif int(i.order) > int(current_order) :
                                     #logging.info(normal + '- - -> ' + str(int(i.order) - 1) )
                                     Item.addUpdatedOrder(self, i.key().id(), int(i.order) - 1)
                                 
                                 if int(i.order) > int(order) and int(i.order) < int(current_order) :
                                     #logging.info(normal + '- -> ' + str(int(i.order) + 1) )
                                     Item.addUpdatedOrder(self, i.key().id(), int(i.order) + 1)
                                     
                            except :
                                for key,value in in_case_error_items.iteritems() :
                                    Item.addUpdatedOrder(self,key,value)
                                raise
                                
                                
                                
               
                   def addUpdatedOrder(self,id,order):
                            mim = MenuItemModel.get_by_id(int(id))
                            order_if_error = mim.order
                            mim.order = order
                            try :
                                mim.put()
                            except :
                                mim.order = order_if_error
                                mim.put()
                                raise
       
                    
                    
    
    