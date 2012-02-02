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
from app.model.main.manager.category import *
from app.model.main.manager.item import *

class Edit:
    
    def GET(self,id):
            
            user = users.get_current_user()
            isadmin = users.is_current_user_admin()
            
            if(user):
                
                re = RestaurantEdit()
                rem = re.getRestaurantEditModel()
                restaurant_selected = re.isRestaurantSelected()
                
                restr = Restaurant()
                restaurant_id = rem.current_model_edit_id
                
                r = restr.getRestaurant(restaurant_id)
                
                #all menus take restaurant id
                menu = Menu()
                m = re.getMenuList()
                if not m :
                    m = menu.getMenuFromParentKey(restaurant_id)
                    re.addMenuList(m)
                    
                mcount = len(m)
                
                #menu single
                ms = MenuModel.get_by_id(int(id))
                
                #update edit model
                re.addMenuId(id)
                re.addMenuName(ms.name)
                
                #reset category id name
                re.resetCatId()
                re.resetCatName()
                
                #model links
                r_name_id = re.getRestaurantIdNameList()
                m_name_id = re.getMenuIdNameList()
                
                #category
                c = Category()
                categories = re.getCategoryList()
                if not categories :
                    categories = c.getCategory(id)
                    re.addCategoryList(categories)
                
                #item
                i = Item()
                items = []
                
                for key, value in categories :
                    items.append( ( str(value.key().id()) + '|' + value.category , i.getItemsFromCategoryParent(key)))
                    #logging.info(str(value.key().id()) + '|' + value.category + ' --------- ' + str(i.getItemsFromCategoryParent(key)) )
                            
                
                # sanity check
                # for key, value in items.items() :
                #    logging.info(str(key) + ' --------->' )
                #     for x in value :
                #             logging.info('hi' + str(x.itemName))
                
                
                nest = main_view.manager.menu.view(r,sorted(m.iteritems()),ms,
                                                   categories,mcount, items)
                
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
                
            else:
                return web.seeother('/')
            
            