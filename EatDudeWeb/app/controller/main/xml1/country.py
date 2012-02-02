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
from app.model.main.manager.country import *


class Serve:
    def GET(self,id):
        
        root = xml.Element("country")
        
        if id == 'all' :
            c = Country()
            country = c.getCountries()
            
            for k,v in country.iteritems():
                info = xml.SubElement(root,"info", id=str(k), name=v)
            
        
        web.header('Content-Type', 'text/xml')
        return main_view.example_xml(xml.tostring(root, encoding='us-ascii'))
    