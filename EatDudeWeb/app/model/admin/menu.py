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
from dbModel import *
from google.appengine.ext import db
from google.appengine.api import users

class Menu:
    
        def add(self,name,id):
                            
                            restaurant = RestaurantModel.get_by_id(int(id))

                            mm = MenuModel()
                            mm.author = users.get_current_user()
                            # date is inserted auto
                            mm.name = name
                            mm.active = False
                            mm.restaurantmodel = restaurant
                            mm.put()
                            # return the menu_id
                            return mm.key().id()
        
        def getMenuFromParentKey(self,id):
                out = MenuModel()
                
                rm = RestaurantModel.get_by_id(int(id))
                menu = rm.menus
                for menus in menu :
                    #only one menu can be active
                    if menus.active == True :
                        out = menus
                        
                return out
    
       
                    
                    
    
    