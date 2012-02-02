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

from dbModel import *
from google.appengine.ext import db

from dbModel import InvitationModel
from google.appengine.api import users


class Invite :
        
        def checkIfCodeExists(self,code):
                                           
                    key = ''
                    id = ''
                    
                    invite_code = db.GqlQuery("SELECT FROM InvitationModel WHERE invitation_code = :1", code )
                                          
                    for x in invite_code :
                        key = x.restaurant_key
                        id = x.key().id()
                        
                        #if not users.is_current_user_admin():
                            #Invite.delete(self, id)
                                              
                    return key
                    
                
        def delete(self,id):
                im = InvitationModel.get_by_id(int(id))
                im.delete()
            
                                               
                                               
                                               
                                               