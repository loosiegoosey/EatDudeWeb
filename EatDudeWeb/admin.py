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
import config
import app.controller

urls = (
  '/admin/', 'app.controller.admin.index.Index',
  #'/admin/logout', 'app.controller.admin.logout.Logout',
  '/admin/addmenu', 'app.controller.admin.addmenu.AddMenu',
  '/admin/addrestaurant', 'app.controller.admin.addrestaurant.AddRestaurant'
)

app = web.application(urls, globals())

def main():
    app.cgirun()
    
if __name__ == '__main__':
    main()