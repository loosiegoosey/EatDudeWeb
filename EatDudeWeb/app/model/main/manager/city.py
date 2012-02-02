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

from dbModel import RestaurantModel

class City :
        
                   def add(self,city,state_id):
                                        
                                           #citymodel = db.GqlQuery("SELECT * from CityModel")
                                           city_id=0
                                           citymodel = db.GqlQuery("SELECT FROM CityModel WHERE name = :1", str(city.strip().lower()))
                                           statemodel = StateModel.get_by_id(int(state_id))
                                           cm = CityModel()
                                           flag = False
                                           
                                           for c in citymodel :
                                                 if c.name.strip().lower() == city.strip().lower() :
                                                     city_id = c.key().id()
                                                     flag = True
                                           
                                           if not flag :
                                               cm.name = city.strip().lower()
                                               cm.active = False
                                               cm.restaurant_count = 0
                                               cm.statemodel = statemodel
                                               #cm.restaurant.append(r.key())
                                               cm.put()
                                               city_id = cm.key().id()
                                               
                                           return city_id
                                    
                                               
                   def getCities(self):
                       out = {}
                       c = CityModel()
                       count=0
        
                       for c in CityModel.all() :
                            if c.active and c.restaurant_count > 0 :
                                out[c.key().id()] = c.name
                            
                       return out
                   
                   
                   
                   def getCitiesByState(self,id):
                       out = {}
                       s = StateModel.get_by_id(int(id))
                       if s :
                           q = s.cities
                           for c in q:
                               if c.active and c.restaurant_count > 0 :
                                   out[c.key().id()] = c.name
                            
                       return out
                                               
                                               
                                               