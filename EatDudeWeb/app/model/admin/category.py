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

class Category :
        
                   def add(self,
                                  category,
                                  id):
                                        
                                            x = category.split('\r\n')
                                            for category_name in x :
                                                menu = MenuModel.get_by_id(int(id))
                                                cm = MenuCategoryModel()
                                                cm.author = users.get_current_user()
                                                # date is inserted auto
                                                cm.category = str(category_name)
                                                cm.active = False
                                                cm.menumodel = menu
                                                cm.put()
                       
                   """                                                           
                   def getCategoryName(self,
                                                            id):
                        out = {}
                        mm = MenuModel.get_by_id(int(id))
                        # categories = collection name in MenuCategoryModel
                        for x in mm.categories :
                                out[x.key().id()] = x.category
                                
                        return  sorted(out.iteritems())
                    """
                    #make it a string instead
                    #<option value="47">Taco Bell</option>
                   def getCategoryName(self,
                                                            id):
                        out = ''
                        mm = MenuModel.get_by_id(int(id))
                        # categories = collection name in MenuCategoryModel
                        for x in mm.categories :
                                out += '<option value="' + str(x.key().id()) + '">' + str(x.category) + '</option>'
                                
                        return  out
                    
                    
                   def getCategoriesFromParentMenu(self,
                                                                                        id):
                            out = []
                            mm = MenuModel.get_by_id(int(id))
                            
                            #return all categories
                            category = mm.categories
                            for categories in category :
                                out.append(categories)
                            
                            return out
                    
                    
    
    