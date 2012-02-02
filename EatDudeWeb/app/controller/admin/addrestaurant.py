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
from web import form
from google.appengine.ext import db
from google.appengine.api import users

from dbModel import *
from app.model.admin.restaurant import *

from config import admin_view

addrestaurant_form = form.Form(
                         form.Textbox(
                                      'Name',
                                      form.notnull,
                                      description='Name'
                                      ),
                         form.Textbox(
                                      'City',
                                      form.notnull,
                                      description='City'
                                      ),
                         form.Textbox(
                                      'State'
                                      ),
                         form.Textbox(
                                      'Address'
                                      ),
                        form.Textbox(
                                      'Phone',
                                      form.notnull,
                                      description='Phone'
                                      )
                         )

class AddRestaurant:
    def GET(self):
                nest = admin_view.addrestaurant(addrestaurant_form)
                return admin_view.index(nest)
            
    def POST(self): 
            if not addrestaurant_form.validates():
                nest = admin_view.addrestaurant(addrestaurant_form)
                return admin_view.index(nest)
            else:
                data = web.input()
                r = Restaurant()
                r.add(data.Name,
                           data.City, 
                           data.Phone, 
                           data.Address, 
                           data.State)
                return web.seeother('/admin/')
