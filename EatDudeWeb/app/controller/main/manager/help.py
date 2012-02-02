import web

from google.appengine.api import users

from config import main_view

from app.model.main.user.profile import *
from app.model.main.manager.restaurant import *
from app.model.main.manager.restaurantedit import *

class Help :
    
    def GET(self):
        
            user = users.get_current_user()
            isadmin = users.is_current_user_admin()
            
            re = RestaurantEdit()
            rem = re.getRestaurantEditModel()
            
            current_restaurant_id = rem.current_model_edit_id
            current_menu_id = rem.current_model_menu_id
            
            restaurant_selected = re.isRestaurantSelected()
            m_name_id = re.getMenuIdNameList()
            r_name_id = re.getRestaurantIdNameList()
                    
            
            nest = main_view.manager.help()
                  
            if(user):
                return main_view.user.profile(nest,user,isadmin,restaurant_selected, 
                                                  sorted(r_name_id.iteritems()),sorted(m_name_id.iteritems()))
            else:
                 return web.seeother('/')
        