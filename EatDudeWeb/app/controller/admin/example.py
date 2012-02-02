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
from config import admin_view

test_form = form.Form( 
    form.Textbox('number',
                 form.notnull,
                 form.regexp('^-?\d+$', 'Not a number.'),
                 form.Validator('Not greater than 10.', lambda x: int(x)>10),
                 description='Enter a number greater than 10:'
                 ))

class AddMenu:
    def GET(self):
                nest = admin_view.addmenu(test_form)
                return admin_view.index(nest)
            
    def POST(self): 
            if not test_form.validates():
                nest = admin_view.addmenu(test_form)
                return admin_view.index(nest)
            else:
                number = test_form['number'].value
                if int(number) % 2:
                    return "Your number %s is odd." % number
                else:
                    return "Your number %s is even." % number
