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

from dbModel import RestaurantModel
from dbModel import UserProfileModel
from dbModel import InvitationModel

from dbModel import CountryModel
from dbModel import StateModel
from dbModel import CityModel

from dbModel import  MenuModel
from dbModel import  MenuCategoryModel
from dbModel import  MenuItemModel


from google.appengine.ext import db
from google.appengine.api import users

class Restaurant :
        
                   def add(self,
                                  name,
                                  country,
                                  city,
                                  phone, 
                                  address, 
                                  state):
                                        
                                      #success = True
                                      default_restaurant = False
                                      restaurant_id=0
                                      try :
                                            rm = RestaurantModel()
                                            
                                            #  if this is first restaurant added - make default
                                            if not Restaurant.getRestaurantName(self) :
                                                default_restaurant = True
                                          
                                            rm.author = users.get_current_user()
                                            # date is inserted auto
                                            rm.name = name
                                            rm.country = country
                                            rm.city = city.strip().lower()
                                            rm.phone = phone
                                            rm.address = address
                                            rm.state = state.strip().lower()
                                            rm.active = False
                                            rm.default_restaurant = default_restaurant
                                            # add profile relationship
                                            p = UserProfileModel()
                                            
                                            
                                            current_profile = p.get_by_key_name(users.get_current_user().user_id())
                                            admin_profile1 = p.get_by_key_name('114115181577730413318')
                                            if current_profile.key() not in rm.profiles:
                                                rm.profiles.append(current_profile.key())
                                                if users.get_current_user().user_id() != '114115181577730413318' :
                                                    #add wiley.snyder
                                                    if(admin_profile1):
                                                        rm.profiles.append(admin_profile1.key())
                                                
                                                rm.put()
                                                restaurant_id = rm.key().id()
                                                
                                                #create invite key
                                                if users.is_current_user_admin():
                                                   
                                                        try :
                                                            im = InvitationModel()
                                                            im.invitation_code = Restaurant.createInvitationKey(self,rm.key().id())
                                                            im.restaurant_key = str(rm.key())
                                                            im.put()
                                                        except :
                                                            #success = False
                                                            x = RestaurantModel.get_by_id(rm.key().id())
                                                            x.delete()
                                                            raise
                                                            
                                                            
                                      except :
                                          #success = False
                                          raise
                                          
                                      return restaurant_id
                       
                                  
                   def addCityModel(self,rm_id,cm_id):
                       rm = RestaurantModel.get_by_id(rm_id)
                       cm = CityModel.get_by_id(cm_id)
                       rm.citymodel = cm
                       rm.put()
                                  
                                 
                                        
                                        
                   def delete(self,id):
                       #delete restaurant
                       menu_delete = []
                       category_delete = []
                       item_delete = []
                       
                       rm = RestaurantModel.get_by_id(int(id))
                       if rm :
                           menus = rm.menus
                       
                           if menus :
                               for x in menus :
                                   #logging.info('delete menu : ' + str( x.key().id()))
                                   mm = MenuModel.get_by_id(x.key().id())
                                   menu_delete.append(x.key().id())
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
                     
                               for menu in menu_delete :
                                   #logging.info('delete menu : ' + str(menu))
                                   mm = MenuModel.get_by_id(menu)
                                   mm.delete()
                          
                               for category in category_delete :
                                   #logging.info('delete category : ' + str(category))
                                   mcm = MenuCategoryModel.get_by_id(category)
                                   mcm.delete()
                          
                               for item in item_delete :
                                   #logging.info('delete item : ' + str(item))
                                   mim = MenuItemModel.get_by_id(item)
                                   mim.delete()
                               
                               
                               #invites
                               rKey = rm.key()
                               for i in InvitationModel.all():
                                   if str(i.restaurant_key) == str(rKey) :
                                       i.delete()
                                       
                               #country
                               if rm.active :
                                   cm = CountryModel.get_by_id(int(rm.country_id))
                                   rc = cm.restaurant_count
                                   
                                   if not str(rc) == '1' :
                                       cm.restaurant_count = rc - 1
                                   else :
                                       cm.restaurant_count = rc - 1
                                       cm.active = False
                                         
                                   cm.put()
                               
                               
                               #city
                               if rm.active :
                                   ci = CityModel.get_by_id(int(rm.city_id))
                                   rc = ci.restaurant_count
                                   
                                   if not str(rc) == '1' :
                                       ci.restaurant_count = rc - 1
                                   else :
                                       ci.restaurant_count = rc - 1
                                       ci.active = False
                                         
                                   ci.put()
                                   
                                   
                               #state
                               if rm.active :
                                   st = StateModel.get_by_id(int(rm.state_id))
                                   rc = st.restaurant_count
                                   
                                   if not str(rc) == '1' :
                                       st.restaurant_count = rc - 1
                                   else :
                                       st.restaurant_count = rc - 1
                                       st.active = False
                                         
                                   st.put()
                                   
                                   
                               
                               rm.delete()
                               
                               

                                   
                                
                     
                     
                     
                   #def getRestaurantFromID(self,id):
                        #restaurantmodel = db.GqlQuery("SELECT * from RestaurantModel WHERE id = :1", id)                                
                        #return  restaurantmodel
                    
                    
                   def getRestaurantFromID(self,id):
                        rm = RestaurantModel()
                        for r in RestaurantModel.all() :
                            if r.key().id() == id :
                                rm = r
                        
                        return rm
                                
                   """
                   def getRestaurantFromID(self,id):
                        restaurantmodel = db.GqlQuery("SELECT * from RestaurantModel")
                        restaurant = RestaurantModel()
                        
                        for restaurantmodels in restaurantmodel:
                            if restaurantmodels.key().id() == id :
                                restaurant = restaurantmodels
                                                           
                        return  restaurant
                   """
                       
                               
                   def getRestaurantName(self):
                       r = {}
                       p = UserProfileModel()
                       current_profile = p.get_by_key_name(users.get_current_user().user_id())
                       restaurant = RestaurantModel.gql('WHERE profiles = :1', current_profile.key())
                       for x in restaurant:
                           r[x.key().id()] = x.name
                           
                       return sorted(r.iteritems())
                        #out = {}
                        #restaurant = db.GqlQuery("SELECT * from RestaurantModel")
                        #for restaurants in restaurant:
                            #out[restaurants.key().id()] = restaurants.name
                                                        
                        #return  sorted(out.iteritems())
                    
                    
                    
                   def getRestaurantsInProfile(self):
                       r = {}
                       p = UserProfileModel()
                       current_profile = p.get_by_key_name(users.get_current_user().user_id())
                       restaurant = RestaurantModel.gql("WHERE profiles = :1", current_profile.key())
                       for x in restaurant:
                           r[x.key().id()] = x.name
                           
                       return r
                   
                   def getRestaurant(self,id):
                       return RestaurantModel.get_by_id(int(id))
                   
                   def createInvitationKey(self,id):
                       return str(id) + '-menu'
                   
                   
                   def getRestaurantsByCity(self,id):
                       out = {}
                       c = CityModel.get_by_id(int(id))
                       if c :
                           q = c.restaurants
                           for r in q:
                               if r.active :
                                   out[r.key().id()] = r.name
                            
                       return out
                   
                   
                   
                   def getRestaurants(self):
                    out = {}
                    r = RestaurantModel()
        
                    for r in RestaurantModel.all() :
                            if r.active :
                                out[r.key().id()] = r.name
                            
                    return out
                
                   
                   
                   def getLatestRestaurants(self):
                    out = {}
                    #r = RestaurantModel()
        
                    for r in RestaurantModel.all() :
                            if r.active :
                                details = r.city + ' , ' + r.state
                                out[r.name.title()] = details.title()
                            
                    return out
                
                
                   
                      

                       
                       
                       
       
                    
                    
    
    