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
import logging # logging.info('')

from dbModel import RestaurantModel
from dbModel import RestaurantEditModel

from google.appengine.ext import db
from google.appengine.api import users

from app.model.main.manager.restaurant import *

from google.appengine.api import memcache

#store edit model in memcache
#memcache hack - if memcache throws an error use datastore
#mc_error() returns True in error event - nothing (gets) from memcache

class RestaurantEdit :

                   def addRestaurantEditModel(self):
                        
                                rem = RestaurantEditModel(key_name= users.get_current_user().user_id())
                                rem.current_model_edit_id = '0'
                                rem.current_model_name = '0'
                                rem.current_model_menu_id = '0'
                                rem.current_model_menu_name = '0'
                                rem.current_cat_id = '0'
                                rem.current_cat_name = '0'
                                
                                
                                x = memcache.get("rem")
                                #set the mc_error hack
                                memcache.add("mc_error",False)
                                if x is not None:
                                    if not memcache.replace("rem",rem) :
                                        memcache.replace("cache_error_occured",True)
                                        memcache.replace("mc_error",True)
                                else :
                                    if not memcache.add("rem",rem) :
                                        memcache.replace("cache_error_occured",True)
                                        memcache.replace("mc_error",True)
                                
                                        
                                rem.put()
                    
                   
                   
                   
                        
                   def getRestaurantEditModel(self):
                     rem = memcache.get("rem")
                     if rem is not None and not RestaurantEdit.mc_err(self):
                            return rem
                     else:
                            r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            if not memcache.add("rem", r):
                                memcache.replace("mc_error",True)
                                
                     return r
                 
                      
                   def addRestaurantNameId(self,id):
                       r = RestaurantModel.get_by_id(int(id))
                       r_name = r.name
                       
                       rem = memcache.get("rem")
                       if rem is not None :
                           rem.current_model_edit_id = id
                           rem.current_model_name = r_name
                           if not memcache.add("rem",rem) :
                               memcache.replace("mc_error",True)
                       
                       m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                       m.current_model_edit_id = id
                       m.current_model_name = r_name
                       m.put()
                    
                    
                   def addMenuId(self,id):
                            rem = memcache.get("rem")
                            if rem is not None :
                                rem.current_model_menu_id = id
                                if not memcache.add("rem",rem):
                                    memcache.replace("mc_error",True)
                               
                            m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            m.current_model_menu_id = id
                            m.put()
                            

                   def addCatId(self,id):
                            rem = memcache.get("rem")
                            if rem is not None :
                                rem.current_cat_id = id
                                if not memcache.add("rem",rem):
                                    memcache.replace("mc_error",True)
                               
                            m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            m.current_cat_id = id
                            m.put()
                   
                   
                   def getMenuId(self):
                       rem = memcache.get("rem")
                       if rem is not None and not RestaurantEdit.mc_err(self) :
                           return rem.current_model_menu_id
                       else :
                           m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                           if m :
                               return m.current_model_menu_id
                       
                       
                   def getCatId(self):
                       rem = memcache.get("rem")
                       if rem is not None and not RestaurantEdit.mc_err(self) :
                           return rem.current_cat_id
                       else :
                           m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                           if m :
                               return m.current_cat_id       
                           
                       
                       
                   def addMenuName(self,name):
                            rem = memcache.get("rem")
                            if rem is not None :
                                rem.current_model_menu_name = name
                                if not memcache.add("rem",rem) :
                                    memcache.replace("mc_error",True)
                                    
                            m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            m.current_model_menu_name = name
                            m.put()
                            
                            
                            
                            
                            
                            
                   def addCatName(self,name):
                            rem = memcache.get("rem")
                            if rem is not None :
                                rem.current_cat_name = name
                                if not memcache.add("rem",rem) :
                                    memcache.replace("mc_error",True)
                                    
                            m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            m.current_cat_name = name
                            m.put()
                            
                            
                            
                            
                   def getCatName(self):
                       rem = memcache.get("rem")
                       if rem is not None and not RestaurantEdit.mc_err(self) :
                           return rem.current_cat_name
                       else:
                           r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                           return r.current_cat_name
                       
                       
                       
                                        
                       
                   def resetMenuId(self):
                      rem = memcache.get("rem")
                      if rem is not None and not RestaurantEdit.mc_err(self) :
                          rem.current_model_menu = '0'
                          if not memcache.replace("rem",rem) :
                              memcache.replace("mc_error",True)
                      
                      m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                      if m:
                          m.current_model_menu_id = '0'
                          m.put()
                          
                    
                   def resetCatId(self):
                      rem = memcache.get("rem")
                      if rem is not None and not RestaurantEdit.mc_err(self) :
                          rem.current_cat_id = '0'
                          if not memcache.replace("rem",rem) :
                              memcache.replace("mc_error",True)
                      
                      m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                      if m:
                          m.current_cat_id = '0'
                          m.put()
                          
                          
                          
                          
                 
                   def resetCatName(self):
                      rem = memcache.get("rem")
                      if rem is not None and not RestaurantEdit.mc_err(self) :
                          rem.current_cat_name = '0'
                          if not memcache.replace("rem",rem) :
                              memcache.replace("mc_error",True)
                      
                      m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                      if m:
                          m.current_cat_name = '0'
                          m.put() 
                          
                          
                          
                          
                          
                   
                   def resetMenuName(self):
                      rem = memcache.get("rem")
                      if rem is not None and not RestaurantEdit.mc_err(self) :
                          rem.current_model_menu_name = '0'
                          if not memcache.replace("rem",rem) :
                              memcache.replace("mc_error",True)
                      
                      m = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                      if m:
                          m.current_model_menu_name = '0'
                          m.put()
                          
                          
                          
                          
                          
                          
                      
                   def getRestaurantEditId(self):
                       
                       rem = memcache.get("rem")
                       if rem is not None and not RestaurantEdit.mc_err(self) :
                           return rem.current_model_edit_id
                       else:
                           r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                           return r.current_model_edit_id
                   
                   
                   
                   
                   
                   
                    
                   def resetRestaurantEditModel(self):
                       rem = memcache.get("rem")
                       if rem is not None :
                           rem.current_model_edit_id = '0'
                           rem.current_model_name = '0'
                           rem.current_model_menu_id= '0'
                           rem.current_model_menu_name = '0'
                           rem.current_cat_id = '0'
                           rem.current_cat_name = '0'
                           
                           if not memcache.replace("rem",rem) :
                               memcache.replace("mc_error",True)
                           
                       r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                       if r :
                           r.current_model_edit_id = '0'
                           r.current_model_name = '0'
                           r.current_model_menu_id= '0'
                           r.current_model_menu_name = '0'
                           r.current_cat_id = '0'
                           r.current_cat_name = '0'
                           r.put()
                           
                           



                   def isRestaurantSelected(self):
                            rem = memcache.get("rem")
                            result = True
                       
                            if rem is not None and not RestaurantEdit.mc_err(self) :
                               if str(rem.current_model_edit_id) == '0' :
                                   result = False
                            else :
                               r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                               if r :
                                   if str(r.current_model_edit_id) == '0' :
                                       result = False
                                  
                            return result
                   
                   
                   
                   
                   
                   
                   
                           
                   def getRestaurantIdNameList(self):
                        out = {}
                        rem = memcache.get("rem")
                        if rem is not None and not RestaurantEdit.mc_err(self) :
                            out[rem.current_model_edit_id] = rem.current_model_name
                        else :
                            r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            if r :
                                out[r.current_model_edit_id] = r.current_model_name
                                                        
                        return  out
                    
                    
                    
                    
                   def getMenuIdNameList(self):
                        out = {}
                        
                        rem = memcache.get("rem")
                        if rem is not None and not RestaurantEdit.mc_err(self) :
                            out[rem.current_model_menu_id] = rem.current_model_menu_name
                        else :
                            r = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                            if r :
                                out[r.current_model_menu_id] = r.current_model_menu_name
                                                      
                        return  out
                    

                  
                   #menu model
                   def addMenuList(self,menus):
                        rem = memcache.get("rem")
                        if rem is not None  :
                            rem.menus = menus
                            if not memcache.add("rem",rem):
                                memcache.replace("mc_error",True)
                   
                   
                   def getMenuList(self):
                       try :
                           
                           rem = memcache.get("rem")
                           if rem is not None and not RestaurantEdit.mc_err(self) :
                               return rem.menus
                           else :
                               return False
                           
                       except :
                           return False
                           
                       
                       
                       
                  #category model
                   def addCategoryList(self,categories):
                        rem = memcache.get("rem")
                        if rem is not None  :
                            rem.categories = categories
                            if not memcache.add("rem",rem):
                                memcache.replace("mc_error",True)
                   
                   
                   def getCategoryList(self):
                       rem = memcache.get("rem")
                       if rem is not None and not RestaurantEdit.mc_err(self) :
                           return rem.categories
                       else :
                           return False
                       
                    
                    
                    
                   #cache error
                   def mc_err(self):
                       out = False
                       mce = memcache.get("mc_error")
                       if mce is not None :
                           out = mce
                       else :
                            if not memcache.add("mc_error",False):
                                out = True
                                
                       return out
                       
                           
                           
                           
                                        
                   
                       
                       
                       
                       
                        
                        