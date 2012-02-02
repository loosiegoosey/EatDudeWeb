from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def admin (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Active</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

admin = CompiledTemplate(admin, 'app\\view\\main\\user\\admin.html')
join_ = admin._join; escape_ = admin._escape

# coding: utf-8
def category():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<ul>\n'])
    extend_([u'<h3>category</h3>\n'])
    extend_([u'<li><a href="/manager/add/category">add category</a></li>\n'])
    extend_([u'<li><a href="/manager/edit/category">edit category</a></li>\n'])
    extend_([u'<li><a href="/manager/delete/category">delete category</a></li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'\n'])
    extend_([u'</div>\n'])

    return self

category = CompiledTemplate(category, 'app\\view\\main\\user\\category.html')
join_ = category._join; escape_ = category._escape

# coding: utf-8
def invite (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'])
    extend_([u'<title>-</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'\n'])
    extend_([u'welcome to the menu builder\n'])
    extend_([u'if <em>you have an invite id</em> enter it in the form below.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="submit code" />\n'])
    extend_([u'</form>\n'])
    extend_([u'\n'])
    extend_([u'if <em>you do not have an invite code</em> <a href="/user/">continue here >></a>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

invite = CompiledTemplate(invite, 'app\\view\\main\\user\\invite.html')
join_ = invite._join; escape_ = invite._escape

# coding: utf-8
def item():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<ul>\n'])
    extend_([u'<h3>item</h3>\n'])
    extend_([u'<li><a href="/manager/add/item">add item</a></li>\n'])
    extend_([u'<li><a href="/manager/edit/item">edit item</a></li>\n'])
    extend_([u'<li><a href="/manager/delete/item">delete item</a></li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'\n'])
    extend_([u'</div>\n'])

    return self

item = CompiledTemplate(item, 'app\\view\\main\\user\\item.html')
join_ = item._join; escape_ = item._escape

# coding: utf-8
def menu():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<ul>\n'])
    extend_([u'<h3>menu</h3>\n'])
    extend_([u'<li><a href="/manager/add/menu">add menu</a></li>\n'])
    extend_([u'<li><a href="/manager/edit/menu">edit menu</a></li>\n'])
    extend_([u'<li><a href="/manager/delete/menu">delete menu</a></li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'\n'])
    extend_([u'</div>\n'])

    return self

menu = CompiledTemplate(menu, 'app\\view\\main\\user\\menu.html')
join_ = menu._join; escape_ = menu._escape

# coding: utf-8
def profile (nest,user,isadmin,restaurant_selected,r,m):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<?xml version="1.0" encoding="UTF-8"?>\n'])
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'])
    extend_([u'<link rel="stylesheet" type="text/css" href="/css/main.css"/>\n'])
    extend_([u'<title>admin</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'\n'])
    extend_([u'<div id="top"> <a href="/">Home</a> | <a href="/user/" > Dashboard</a> | <a href="/manager/help">Help</a> | logged in as : ', escape_(user, False), u' </div>\n'])
    extend_([u'<div id="topnav">\n'])
    extend_([u'        \n'])
    extend_([u'    <!-- now editing -->\n'])
    for key,value in loop.setup(r):
        if value != '0' :
            extend_(['            ', u'            you are now editing - <a href="/manager/main/view/', escape_(key, False), u'" >', escape_(value, False), u'</a>\n'])
            extend_(['            ', u'\n'])
    if m :
        for key,value in loop.setup(m):
            if value != '0' :
                extend_(['            ', u'    > <a href="/manager/menu/view/', escape_(key, False), u'" >', escape_(value, False), u'</a>\n'])
                extend_(['            ', u'\n'])
    extend_([u'</div>\n'])
    extend_([u'\n'])
    if restaurant_selected :
        extend_(['        ', u'    <div id="nav">Edit Options > <a href="/user/restaurant">Restaurant</a> | <a href="/user/menu">Menu</a>\n'])
        if isadmin :
            extend_(['            ', u'| <a href="/user/admin">Admin</a>\n'])
            extend_(['            ', u'\n'])
    if not m :
        extend_(['    ', u'</div>\n'])
        extend_(['    ', u'\n'])
    for key,value in loop.setup(m):
        if value != '0' :
            extend_(['            ', u'     | <a href="/user/category">Category</a> | <a href="/user/item">Item</a></div>\n'])
            extend_(['            ', u'\n'])
            extend_(['            ', u'\n'])
            extend_(['            ', u'\n'])
    extend_([escape_(nest, False), u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

profile = CompiledTemplate(profile, 'app\\view\\main\\user\\profile.html')
join_ = profile._join; escape_ = profile._escape

# coding: utf-8
def profile_error():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h1>ERROR</h1>\n'])
    extend_([u'</div>\n'])

    return self

profile_error = CompiledTemplate(profile_error, 'app\\view\\main\\user\\profile_error.html')
join_ = profile_error._join; escape_ = profile_error._escape

# coding: utf-8
def profile_main (r):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    if r :
        extend_([u'    <p><h3>Restaurants</h3>\n'])
        extend_([u'click on a restaurant to start<br />\n'])
        for key,value in loop.setup(r):
            extend_([u'        <a href="/manager/main/view/', escape_(key, False), u'"><h1> > ', escape_(value, False), u'</h1></a></p>\n'])
            extend_([u'\n'])
        extend_([u'add another <a href="/manager/add/restaurant">restaurant ></a>\n'])
        extend_([u'\n'])
    else :
        extend_([u'    <h3>Add a Restaurant</h3>\n'])
        extend_([u'    Start <a href="/manager/add/restaurant" >here</a>.\n'])
    extend_([u'</div>\n'])

    return self

profile_main = CompiledTemplate(profile_main, 'app\\view\\main\\user\\profile_main.html')
join_ = profile_main._join; escape_ = profile_main._escape

# coding: utf-8
def restaurant(restaurant_selected):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    if restaurant_selected :
        extend_([u'    <ul>\n'])
        extend_([u'    <h3>restaurant</h3>\n'])
        extend_([u'    <li><a href="/manager/edit/restaurant">edit restaurant</a></li>\n'])
        extend_([u'    <li><a href="/manager/delete/restaurant">delete restaurant</a></li>\n'])
        extend_([u'    <li>backup restaurant</li>\n'])
        extend_([u'    <li>import from backup</li>\n'])
        extend_([u'    </ul>\n'])
        extend_([u'\n'])
    extend_([u'</div>\n'])

    return self

restaurant = CompiledTemplate(restaurant, 'app\\view\\main\\user\\restaurant.html')
join_ = restaurant._join; escape_ = restaurant._escape

