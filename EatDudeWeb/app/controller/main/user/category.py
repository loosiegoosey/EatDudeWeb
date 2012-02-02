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

from config import main_view
from google.appengine.api import users
from app.model.main.manager.restaurantedit import *

class Category:
    
    def GET(self):
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        rem = RestaurantEdit()
        restaurant_selected = rem.isRestaurantSelected()
        r_name_id = rem.getRestaurantIdNameList()
        m_name_id = rem.getMenuIdNameList()
        
        if(users.get_current_user()):
                nest = main_view.user.category()
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
        else:
               return main_view.user.profile_error()