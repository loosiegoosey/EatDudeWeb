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

from config import main_view
from google.appengine.api import users
from app.model.main.user.profile import *

from app.model.main.manager.restaurantedit import *
from app.model.main.manager.restaurant import *

from dbModel import RestaurantEditModel

class Index:
    def GET(self):
        
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        r = Restaurant()
        latest_restaurants = r.getLatestRestaurants()

        hasprofile = 0
                
        if user:
                    hasprofile = users.get_current_user().user_id()
                    
                    greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                                (user.nickname(), users.create_logout_url("/")))
            
                    p = Profile()
                    profile = p.getProfile()
            
                    if not profile:
                        p.add()
                        
                    rem = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                    if not rem :
                        re = RestaurantEdit()
                        re.addRestaurantEditModel()
                        
                    
                        
        else:
                    greeting = ("<a href=\"%s\">Sign in or register</a>." %
                                users.create_login_url("/"))

        return main_view.index("Grasshopper",greeting,hasprofile,
                               sorted(latest_restaurants.iteritems()))
    
    