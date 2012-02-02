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
  #home
  '/', 'app.controller.main.index.Index',
  #user
  '/user/','app.controller.main.user.profile.UserProfile',
  '/invite/','app.controller.main.user.invite.CheckInvite',
  '/user/restaurant','app.controller.main.user.restaurant.Restaurant',
  '/user/menu','app.controller.main.user.menu.Menu',
  '/user/item','app.controller.main.user.item.Item',
  '/user/category','app.controller.main.user.category.Category',
  '/user/admin','app.controller.main.user.admin.Admin',
  #manager
  '/manager/help','app.controller.main.manager.help.Help',
  '/manager/add/(.*)','app.controller.main.manager.add.add.Add',
  #'/manager/view/(.*)','app.controller.main.manager.view.view.View',
  '/manager/edit/(.*)','app.controller.main.manager.edit.edit.Edit',
  '/manager/edititem/(.*)','app.controller.main.manager.edit.edititem.EditItem',
  '/manager/additem/(.*)','app.controller.main.manager.add.additem.AddItem',
  '/manager/editcategory/(.*)','app.controller.main.manager.edit.editcategory.EditCategory',
  '/manager/editmenu/(.*)','app.controller.main.manager.edit.editmenu.EditMenu',
  '/manager/delete/(.*)','app.controller.main.manager.delete.delete.Delete',
  '/manager/main/view/(.*)','app.controller.main.manager.main.view.Edit',
  '/manager/menu/view/(.*)','app.controller.main.manager.menu.view.Edit',
  #util
  #'/util/(.*)','app.controller.main.util.Util',
  
  #xml
  '/example_xml/(.*)', 'app.controller.main.example_xml.ExampleXML',
  '/xml/app_message/(.*)','app.controller.main.xml1.app_message.Serve',
  '/xml/country/(.*)','app.controller.main.xml1.country.Serve',
  '/xml/state/(.*)','app.controller.main.xml1.state.Serve',
  '/xml/city/(.*)','app.controller.main.xml1.city.Serve',
  '/xml/restaurant/(.*)','app.controller.main.xml1.restaurant.Serve'
)

app = web.application(urls, globals())

def main():
    app.cgirun()
    
if __name__ == '__main__':
    main()
    
