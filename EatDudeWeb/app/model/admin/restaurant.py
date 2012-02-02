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

from dbModel import RestaurantModel
from dbModel import UserProfileModel

from google.appengine.ext import db
from google.appengine.api import users

class Restaurant :
        
                   def add(self,
                                  name, 
                                  city,
                                  phone, 
                                  address, 
                                  state):
                                        rm = RestaurantModel()
                                        rm.author = users.get_current_user()
                                        # date is inserted auto
                                        rm.name = name
                                        rm.city = city
                                        rm.phone = phone
                                        rm.address = address
                                        rm.state = state
                                        rm.active = False
                                        rm.put()
                    
                    
                   def getRestaurantFromID(self,id):
                        restaurantmodel = db.GqlQuery("SELECT * from RestaurantModel")
                        restaurant = RestaurantModel()
                        
                        for restaurantmodels in restaurantmodel:
                            if restaurantmodels.key().id() == id :
                                restaurant = restaurantmodels
                                                           
                        return  restaurant
                    
                               
                   def getRestaurantName(self):
                        out = {}
                        restaurant = db.GqlQuery("SELECT * from RestaurantModel")
                        for restaurants in restaurant:
                            out[restaurants.key().id()] = restaurants.name
                                                        
                        return  sorted(out.iteritems())
       
                    
                    
    
    