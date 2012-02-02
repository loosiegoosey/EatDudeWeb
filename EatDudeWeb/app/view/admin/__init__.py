from web.template import CompiledTemplate, ForLoop, TemplateResult

import menu_form
# coding: utf-8
def addrestaurant (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="Add Restaurant" />\n'])
    extend_([u'</form>\n'])

    return self

addrestaurant = CompiledTemplate(addrestaurant, 'app\\view\\admin\\addrestaurant.html')
join_ = addrestaurant._join; escape_ = addrestaurant._escape

# coding: utf-8
def index (nest):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<?xml version="1.0" encoding="UTF-8"?>\n'])
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'])
    extend_([u'<link rel="stylesheet" type="text/css" href="/public/css/admin.css"/>\n'])
    extend_([u'<title>admin</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<div id="top"><a href="https://appengine.google.com/" target="_blank">Google Apps Dashboard</a> | <a href="/_ah/login?continue=/admin/&action=Logout">logout</a> |\n'])
    extend_([u' <a href="http://localhost:8081/_ah/admin" target="_blank">local datastore</a> </div>\n'])
    extend_([u'Welcome to the admin.\n'])
    extend_([u'<ul><h3><a href="/admin/">Dashboard</a></h3>\n'])
    extend_([u'<li><a href="/admin/addrestaurant">add restaurant</a></li>\n'])
    extend_([u'<li><a href="/admin/addmenu">add menu</a></li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    if nest == 'nothing' :
        extend_([u'    <!-- /', escape_(nest, True), u' -->\n'])
    else :
        extend_([u'    ', escape_(nest, False), u'\n'])
        extend_([u'\n'])
        extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, 'app\\view\\admin\\index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def logout (logout):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<a href="', escape_(logout, False), u'">logout</a>\n'])

    return self

logout = CompiledTemplate(logout, 'app\\view\\admin\\logout.html')
join_ = logout._join; escape_ = logout._escape

