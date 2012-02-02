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

from app.model.main.manager.restaurantedit import *
from app.model.main.manager.restaurant import *
from app.model.main.manager.menu import *

class Edit:
    
    def GET(self,id):
    
            user = users.get_current_user()
            isadmin = users.is_current_user_admin()
            
            if(user):
                
                rem = RestaurantEditModel.get_by_key_name(users.get_current_user().user_id())
                if not rem :
                    rem.addRestaurantEditModel()
                
                re = RestaurantEdit()
                
                #reset menu
                re.resetMenuId()
                re.resetMenuName()
                
                #add restaurant name id
                re.addRestaurantNameId(id)
                
                #menus   
                menu = Menu()
                m = re.getMenuList()
                if not m :
                    m = menu.getMenuFromParentKey(id)
                    re.addMenuList(m)
                    
                mcount = len(m)
                    
                r_name_id = re.getRestaurantIdNameList()
                m_name_id = re.getMenuIdNameList()
                
                restaurant_selected = re.isRestaurantSelected()
                nest = main_view.manager.main.view(sorted(m.iteritems()),mcount)
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                
            else:
                return web.seeother('/')
            
