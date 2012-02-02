from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def additem (form,category_id,category_name):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>add item to ', escape_(category_name, False), u' category</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'<input type="hidden" name="category_id" id="category_id" value="', escape_(category_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

additem = CompiledTemplate(additem, 'app\\view\\main\\manager\\add\\additem.html')
join_ = additem._join; escape_ = additem._escape

# coding: utf-8
def category (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Add a Category</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="Add Category" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

category = CompiledTemplate(category, 'app\\view\\main\\manager\\add\\category.html')
join_ = category._join; escape_ = category._escape

# coding: utf-8
def item (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Add a Menu Item</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="Add Item" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

item = CompiledTemplate(item, 'app\\view\\main\\manager\\add\\item.html')
join_ = item._join; escape_ = item._escape

# coding: utf-8
def menu (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Add a Menu</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="hidden" id="menu_id" value="" name="menu_id" />\n'])
    extend_([u'<input type="submit" value="Create Menu" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

menu = CompiledTemplate(menu, 'app\\view\\main\\manager\\add\\menu.html')
join_ = menu._join; escape_ = menu._escape

# coding: utf-8
def restaurant (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Add a Restaurant</h3>\n'])
    extend_([u'Add the restaurant details for your menus.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="Add Restaurant" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

restaurant = CompiledTemplate(restaurant, 'app\\view\\main\\manager\\add\\restaurant.html')
join_ = restaurant._join; escape_ = restaurant._escape

