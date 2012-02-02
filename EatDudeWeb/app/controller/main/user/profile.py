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

from config import main_view
from google.appengine.api import users

from google.appengine.api import memcache
from google.appengine.ext import db

from app.model.main.user.profile import *
from app.model.main.manager.restaurant import *
from app.model.main.manager.restaurantedit import *

class UserProfile:
    
    def GET(self):
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if user :
            # if exists set editModel back to none
            #this should only be set when restaurant is selected
            rem = RestaurantEdit()
            rem.resetRestaurantEditModel()
            rem.resetMenuId()
            rem.resetMenuName()
        
            restaurant_selected = rem.isRestaurantSelected()
            r_name_id = rem.getRestaurantIdNameList()
            m_name_id = rem.getMenuIdNameList()
        
            #get restaurant(s)
            r = Restaurant()
            restaurants = r.getRestaurantsInProfile()
            
            #is profile active
            p = Profile()
            profile = p.getProfile()
            
            #if you're here you saw the invite page
            upm = UserProfileModel.get_by_key_name(user.user_id())
            if not upm.invited :
                upm.invited = True
                upm.put()
                        
            
            if not profile.active :
                return 'account error - this account in innactive please contact admin - eatdude@live.com'
            else :
                
                nest = main_view.user.profile_main(sorted(restaurants.iteritems()))
                return main_view.user.profile(nest,user,isadmin,restaurant_selected,
                                                sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        
        else:
               return web.seeother('/')
           
           