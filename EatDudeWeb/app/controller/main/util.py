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

from web import form
from config import main_view
from google.appengine.api import users

from dbModel import *
from google.appengine.ext import db

from app.model.main.manager.restaurant import *
from app.model.main.manager.country import *
from app.model.main.manager.city import *
from app.model.main.manager.state import *
from app.model.main.manager.menu import *
from app.model.main.manager.category import *
from app.model.main.manager.item import *

from app.model.main.manager.restaurantedit import *


class Util:
            
    def GET(self,id):
        
        if(users.is_current_user_admin()):
                        
                        # us = 1001
                        # california = 2001
                        # SB = 3001
                        # ventura = 3002
                        
                        #andrias seafood 1010
                        #palace grill 6004
                        #majaraja 23001
                        #tacos jalisco 33012
                        
                        '''
                        rm = RestaurantModel()
                        r = rm.get_by_id(int(id))
                        r.country_id = '1001'
                        r.state_id = '2001'
                        r.city_id = '3001'
                        r.put()
                        return 'done'
                        '''
                        
                        """
                        sm = CityModel()
                        s = sm.get_by_id(int(id))
                        s.restaurant_count = 0
                        s.put()
                        
                        return 'done'
                        """
                        
                        
                        """
                        mm = MenuModel.get_by_id(int(id))
                        categories = mm.categories
                        
                        out = '<html>'
                        
                        for c in categories :
                            mcm = MenuCategoryModel.get_by_id(c.key().id())
                            items = mcm.items
                            out+= '*' + str(mcm.category) + '<br />'
                            order = 1
                            for x in items :
                                out+=str(x.key().id()) + ' --- ' + x.itemName
                                mim = MenuItemModel.get_by_id(int(x.key().id()))
                                mim.order = order
                                mim.put()
                                order = order + 1
                                out+= ' --- done. <br />'
                            out+='------------------------------------<br /><br />'
                            
                        out+='</html>'
                        
                        return out
                        """
                        
                        
                        #6005 palace grill lunch menu
                        #2008 palace grill dinner menu
                        #4017 andria's
                        
                        """
                        mm = MenuModel.get_by_id(int(id))
                        categories = mm.categories
                        out=''
                        order=1
                        
                        for x in categories :
                            out+='<html>'
                            out+= str(x.key().id()) + ' --- ' + x.category
                            mcm = MenuCategoryModel.get_by_id(int(x.key().id()))
                            mcm.order = order
                            mcm.put()
                            order = order + 1
                            out+= ' --- done. <br />'
                            out+='</html>'
                            
                        return out
                        """
                            
                        
        
        else:
                return web.seeother('/')