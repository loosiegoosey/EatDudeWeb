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

from google.appengine.ext import db

#search
class CountryModel(db.Model):
    active = db.BooleanProperty()
    restaurant_count = db.IntegerProperty()
    countrycode = db.StringProperty()
    
class StateModel(db.Model):
    name = db.StringProperty()
    active = db.BooleanProperty()
    restaurant_count = db.IntegerProperty()
    countrymodel = db.ReferenceProperty(CountryModel, collection_name='states')

class CityModel(db.Model):
    name = db.StringProperty()
    active = db.BooleanProperty()
    restaurant_count = db.IntegerProperty()
    statemodel = db.ReferenceProperty(StateModel, collection_name='cities')
    

#data 
class RestaurantModel(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    country = db.StringProperty()
    country_id = db.StringProperty()
    city = db.StringProperty()
    city_id = db.StringProperty()
    phone = db.PhoneNumberProperty()
    address = db.PostalAddressProperty()
    state = db.StringProperty()
    state_id = db.StringProperty()
    active = db.BooleanProperty()
    default_restaurant = db.BooleanProperty() #first added is set to default
    profiles = db.ListProperty(db.Key)
    citymodel = db.ReferenceProperty(CityModel, collection_name = 'restaurants')
    
class MenuModel(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    active = db.BooleanProperty()
    restaurantmodel = db.ReferenceProperty(RestaurantModel, collection_name = 'menus')
    
class MenuCategoryModel(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    order = db.IntegerProperty()
    category = db.StringProperty()
    active = db.BooleanProperty()
    menumodel = db.ReferenceProperty(MenuModel, collection_name = 'categories')
    
class MenuItemModel(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    order = db.IntegerProperty()
    itemName = db.StringProperty()
    itemDesc = db.StringProperty(multiline=True)
    itemPrice = db.StringProperty()
    itemNumber = db.StringProperty()
    active = db.BooleanProperty()
    menucategorymodel = db.ReferenceProperty(MenuCategoryModel, collection_name = 'items')
    
#user profile
class UserProfileModel(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    nickname = db.StringProperty()
    invited = db.BooleanProperty()
    active = db.BooleanProperty()
    
#edit
class RestaurantEditModel(db.Model):
    current_model_edit_id = db.StringProperty()
    current_model_name = db.StringProperty()
    current_model_menu_id = db.StringProperty()
    current_model_menu_name = db.StringProperty()
    current_cat_id = db.StringProperty()
    current_cat_name = db.StringProperty()

#invite
class InvitationModel(db.Model):
    invitation_code = db.StringProperty()
    restaurant_key = db.StringProperty()
    
    