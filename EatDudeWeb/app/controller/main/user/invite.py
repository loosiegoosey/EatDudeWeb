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
from web import form

from google.appengine.api import memcache
from google.appengine.ext import db

from dbModel import UserProfileModel

from app.model.main.user.profile import *
from app.model.main.manager.restaurant import *
from app.model.main.manager.restaurantedit import *
from app.model.main.manager.invite import *

invite_form = form.Form(
                              form.Textbox(
                              'invite_code',
                              form.notnull,
                              description='invite code : ')
                )

class CheckInvite:
                
    def GET(self):
        user = users.get_current_user()
        #check if invited form has been submitted or clicked thru
        if user :
                
                if not users.is_current_user_admin():
                    upm = UserProfileModel.get_by_key_name(user.user_id())
                    if not upm.invited :
                        return main_view.user.invite(invite_form)
                    else :
                        return web.seeother('/user/')
                else :
                    return web.seeother('/user/')
        
        else:
               return web.seeother('/')
        
           
    def POST(self):
        user = users.get_current_user()
        isadmin = users.is_current_user_admin()
        
        if user :
                validateForm = invite_form()
                if not validateForm.validates():
                    return main_view.user.invite(validateForm)
                
                else :
                    data = web.input()
                    i = Invite()
                    
                    restaurant_keyname = i.checkIfCodeExists(data.invite_code)
                    if restaurant_keyname :
                        rm = RestaurantModel.get(restaurant_keyname)
                        
                        # add profile to restaurant
                        if not users.is_current_user_admin():
                            p = UserProfileModel()
                            current_profile = p.get_by_key_name(users.get_current_user().user_id())
                            if current_profile.key() not in rm.profiles:
                                rm.profiles.append(current_profile.key())
                                rm.put()
                               
                        upm = UserProfileModel.get_by_key_name(user.user_id())
                        upm.invited = True
                        upm.put()
                        
                        return web.seeother('/user/')
                    else:
                        return 'invitation code failed'
        
        else:
               return web.seeother('/')
           
           