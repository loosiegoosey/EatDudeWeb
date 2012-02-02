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
                       
                                        category = MenuCategoryModel.get_by_id(int(id))
                                        
                                        mim = MenuItemModel()
                                        mim.author = users.get_current_user()
                                        # date is inserted auto
                                        mim.itemName = itemName
                                        mim.itemDesc = itemDesc
                                        mim.itemPrice = itemPrice
                                        mim.itemNumber = itemNumber
                                        mim.active = False
                                        mim.menucategorymodel = category
                                        mim.put()
                                        
                    
                   def getItemsFromCategoryParent(self,
                                                                                        id):
                            out = []
                            mcm = MenuCategoryModel.get_by_id(int(id))
                            
                            #return all items
                            item = mcm.items
                            for items in item :
                                out.append(items)
                            
                            return out
       
                    
                    
    
    