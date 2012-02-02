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

class View:
    
    def GET(self,entity):
            user = users.get_current_user()
            if(user):
                    
                    if entity=='restaurant' :
                        nest = main_view.manager.view.restaurant()
                    elif entity=='menu' :
                        nest = main_view.manager.view.menu()
                    elif entity=='category' :
                        nest = main_view.manager.view.category()
                    elif entity=='item' :
                        nest = main_view.manager.view.item()
                    else :
                        nest = main_view.manager.error()

                    return main_view.user.profile(nest,user)
        
            else:
                return main_view.manager.error()