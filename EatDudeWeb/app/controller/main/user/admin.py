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
import hashlib
import logging

from web import form
from config import main_view
from google.appengine.api import users
from app.model.main.manager.restaurantedit import *
from app.model.main.manager.country import *
from app.model.main.manager.city import *
from app.model.main.manager.state import *

active_form = form.Form(
                              form.Dropdown('active', [])
                              )
class Admin:
        
    def GET(self): 
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if(isadmin):
            re = RestaurantEdit()
            rem = re.getRestaurantEditModel()
            current_restaurant_id = rem.current_model_edit_id
            r = RestaurantModel().get_by_id(int(current_restaurant_id))
        
            restaurant_selected = re.isRestaurantSelected()
            r_name_id = re.getRestaurantIdNameList()
            m_name_id = re.getMenuIdNameList()
        
            active_form.active.args = []
            if not r.active :
                active_form.active.args.append( ('0',str(r.active)) )
                active_form.active.args.append( ('1','True') )
            else :
                active_form.active.args.append( ('1',str(r.active)) )
                active_form.active.args.append( ('0','False') )
            
            nest = main_view.user.admin(active_form)
            return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        else:
               return web.seeother('/')
          
           
    def POST(self):
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if(isadmin):
            re = RestaurantEdit()
            rem = re.getRestaurantEditModel()
            current_restaurant_id = rem.current_model_edit_id
            r = RestaurantModel().get_by_id(int(current_restaurant_id))
        
            restaurant_selected = re.isRestaurantSelected()
            r_name_id = re.getRestaurantIdNameList()
            m_name_id = re.getMenuIdNameList()
            
            
            
            
            
            validateForm = active_form()
            if not validateForm.validates():
                nest = main_view.user.admin(validateForm)
                return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                      sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
            else:
                data = web.input()
                if data.active == '0':
                    r.active = False
                else:
                    r.active = True;
                    
                r.put()
                
                country_id = r.country_id
                state_id = r.state_id
                city_id = r.city_id
                
                
                com = CountryModel()
                co = com.get_by_id(int(country_id))
                rc = co.restaurant_count
                if data.active == '0':
                    if not rc == 0:
                        co.restaurant_count = rc - 1
                else:
                    co.restaurant_count = rc + 1
                    
                co.put()
                
                
                sm = StateModel()
                s = sm.get_by_id(int(state_id))
                rc = s.restaurant_count
                if data.active == '0':
                    if not rc == 0:
                        s.restaurant_count = rc - 1
                else:
                    s.restaurant_count = rc + 1
                    
                s.put()
                
                
                cm = CityModel()
                c = cm.get_by_id(int(city_id))
                rc = c.restaurant_count
                if data.active == '0':
                    if not rc == 0:
                        c.restaurant_count = rc - 1
                else:
                   c.restaurant_count = rc + 1
                    
                c.put()
                
                
                
                active_form.active.args = []
                if not r.active :
                    active_form.active.args.append( ('0',str(r.active)) )
                    active_form.active.args.append( ('1','True') )
                else :
                    active_form.active.args.append( ('1',str(r.active)) )
                    active_form.active.args.append( ('0','False') )
                
                
                
                
                nest = main_view.user.admin(active_form)
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                
        else:
               return web.seeother('/')
        
           
           
           