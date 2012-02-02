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

import google.appengine.ext.db

from config import main_view

from xml.etree import ElementTree as xml

from dbModel import *
from app.model.main.manager.restaurant import *
from app.model.main.manager.category import *
from app.model.main.manager.menu import *
from app.model.main.manager.item import *


class ExampleXML:
    def GET(self,id):
        
        restaurant = Restaurant().getRestaurantFromID(int(id))
        
        restaurant_key = str(restaurant.key())
        restaurant_id = str(restaurant.key().id())
        restaurant_name = restaurant.name
        restaurant_phone = restaurant.phone
        restaurant_address = restaurant.address
        
        m = Menu()
        menu = m.getMenuFromParentKey(restaurant_id)
        
        
        #write xml
        root = xml.Element("restaurant", 
                           name= restaurant_name , 
                           id= restaurant_id, 
                           phone= restaurant_phone , 
                           address= restaurant_address)
        
        for k,v in menu.iteritems() :
            
            categories = Category().getCategoriesFromParentMenu(str(k))
            child = xml.SubElement(root, "menu", name= v.name , id= str(k))
        
            for category in categories :
                        child2 = xml.SubElement(child, "category", name= category.category , 
                                                id= str(category.key().id()))
                        
                        items = Item().getItemsFromCategoryParent(category.key().id())
                        
                        #no empty elements
                        for i in items :
                            if not i.itemDesc :
                                i.itemDesc = ' ';
                            if not i.itemPrice :
                                i.itemPrice = ' ';
                            if not i.itemNumber :
                                i.itemNumber = ' ';
        
                        #item
                        for i in items :
                                item = xml.SubElement(child2, "item", name= i.itemName, 
                                                      id= str( i.key().id()))
        
                                child4 = xml.Element("desc")
                                child4.text = i.itemDesc
        
                                child5 = xml.Element("price")
                                child5.text = i.itemPrice
        
                                child6 = xml.Element("number")
                                child6.text = i.itemNumber
        
                                item.append(child4)
                                item.append(child5)
                                item.append(child6)
                        
        web.header('Content-Type', 'text/xml')
        #return main_view.example_xml(xml.tostring(root, encoding='us-ascii'))
        return main_view.example_xml(xml.tostring(root, encoding="utf-8"))
        
    