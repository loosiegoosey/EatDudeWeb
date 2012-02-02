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

from dbModel import UserProfileModel

from google.appengine.ext import db
from google.appengine.api import users

class Profile :
        
                   def add(self):
                       
                                        user = users.get_current_user().user_id()
                                        up = UserProfileModel(key_name=user)
                                        up.author = users.get_current_user()
                                        up.nickname = user
                                        up.invited = False
                                        up.active = True
                                        # date is inserted auto
                                        up.put()
                
                
                   def getProfile(self):
                        up = UserProfileModel()
                        profile = up.get_by_key_name(users.get_current_user().user_id())
                                                           
                        return  profile
       
                    
                    
    
    