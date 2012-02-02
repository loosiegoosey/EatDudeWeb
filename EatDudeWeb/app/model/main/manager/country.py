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

class Country :
        
                   def add(self,country):
                                            
                            countrymodel = db.GqlQuery("SELECT * from CountryModel")
                            country_id = 0
                            cm = CountryModel()
                            flag = False
                        
                            for c in countrymodel:
                                if c.countrycode == country :
                                    country_id = c.key().id()
                                    flag = True
                                    
                            
                            if not flag :  
                                cm.countrycode = country
                                cm.active = False
                                cm.restaurant_count = 0
                                cm.put()
                                country_id = cm.key().id()
                                
                            return country_id
                        
                        
                                
                   def getCountries(self):
                    out = {}
                    c = CountryModel()
        
                    for c in CountryModel.all() :
                            if c.active and c.restaurant_count > 0:
                                out[c.key().id()] = c.countrycode
                            
                    return out
                           
                       
                      
                                                    