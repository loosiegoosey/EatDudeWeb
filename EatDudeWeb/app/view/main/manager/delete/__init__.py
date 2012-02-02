from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def category (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select category to delete</h3>\n'])
    extend_([u'This will also delete all items in this category.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="delete selected category" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

category = CompiledTemplate(category, 'app\\view\\main\\manager\\delete\\category.html')
join_ = category._join; escape_ = category._escape

# coding: utf-8
def item (form,restaurant_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h2>Delete this item</h2>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="Delete" />\n'])
    extend_([u'<input type="hidden" name="restaurant_id" id="restaurant_id" value="', escape_(restaurant_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

item = CompiledTemplate(item, 'app\\view\\main\\manager\\delete\\item.html')
join_ = item._join; escape_ = item._escape

# coding: utf-8
def menu (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select menu to delete</h3>\n'])
    extend_([u'This will also delete all categories and items for this menu.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="delete selected menu" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

menu = CompiledTemplate(menu, 'app\\view\\main\\manager\\delete\\menu.html')
join_ = menu._join; escape_ = menu._escape

# coding: utf-8
def restaurant (form,restaurant_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h2>Delete this restaurant</h2>\n'])
    extend_([u'This will also delete all menus,categories and items for this restaurant.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="delete this restaurant" />\n'])
    extend_([u'<input type="hidden" name="restaurant_id" id="restaurant_id" value="', escape_(restaurant_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

restaurant = CompiledTemplate(restaurant, 'app\\view\\main\\manager\\delete\\restaurant.html')
join_ = restaurant._join; escape_ = restaurant._escape

# coding: utf-8
def select_items (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select item to delete</h3>\n'])
    extend_([u'delete item\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="delete selected item" />\n'])
    extend_([u'\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

select_items = CompiledTemplate(select_items, 'app\\view\\main\\manager\\delete\\select_items.html')
join_ = select_items._join; escape_ = select_items._escape

