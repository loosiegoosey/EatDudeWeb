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

class State :
        
                   def add(self,state,id):
                                            
                                            statemodel = db.GqlQuery("SELECT * from StateModel")
                                            country = CountryModel.get_by_id(int(id))
                                            state_id=0
                                            
                                            sm = StateModel()
                                            flag = False
                                            
                                            for s in statemodel :
                                                 if s.name.strip().lower() == state.strip().lower() :
                                                     state_id= s.key().id()
                                                     flag = True
                                            
                                            
                                            if not flag :
                                                sm.name = state.strip().lower()
                                                sm.active = False
                                                sm.restaurant_count = 0
                                                sm.countrymodel = country
                                                sm.put()
                                                state_id= sm.key().id()
                                                
                                            return state_id
                                                
                                                
                         
                                                
                   def getStates(self):
                       out = {}
                       c = StateModel()
        
                       for c in StateModel.all() :
                            if c.active and c.restaurant_count > 0 :
                                out[c.key().id()] = c.name
                            
                       return out
                   
                   
                   
                   def getStatesByCountry(self,id):
                       out = {}
                       c = CountryModel.get_by_id(int(id))
                       
                       if c :
                           q = c.states
                           for s in q:
                               if s.active and s.restaurant_count > 0 :
                                   out[s.key().id()] = s.name
                            
                       return out
                   
                   