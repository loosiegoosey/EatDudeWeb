from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def category (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select category to edit</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="edit" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

category = CompiledTemplate(category, 'app\\view\\main\\manager\\edit\\category.html')
join_ = category._join; escape_ = category._escape

# coding: utf-8
def editcategory (form,category_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Edit Category</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'<input type="hidden" name="category_id" id="category_id" value="', escape_(category_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

editcategory = CompiledTemplate(editcategory, 'app\\view\\main\\manager\\edit\\editcategory.html')
join_ = editcategory._join; escape_ = editcategory._escape

# coding: utf-8
def edititem (form,item_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Edit Item</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'<input type="hidden" name="item_id" id="item_id" value="', escape_(item_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

edititem = CompiledTemplate(edititem, 'app\\view\\main\\manager\\edit\\edititem.html')
join_ = edititem._join; escape_ = edititem._escape

# coding: utf-8
def editmenu (form,menu_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Edit Menu</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'<input type="hidden" name="menu_id" id="menu_id" value="', escape_(menu_id, False), u'" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

editmenu = CompiledTemplate(editmenu, 'app\\view\\main\\manager\\edit\\editmenu.html')
join_ = editmenu._join; escape_ = editmenu._escape

# coding: utf-8
def item (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select item to edit</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="edit item" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

item = CompiledTemplate(item, 'app\\view\\main\\manager\\edit\\item.html')
join_ = item._join; escape_ = item._escape

# coding: utf-8
def item_categories (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>item category</h3>\n'])
    extend_([u'What category is the item in?\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="get items" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

item_categories = CompiledTemplate(item_categories, 'app\\view\\main\\manager\\edit\\item_categories.html')
join_ = item_categories._join; escape_ = item_categories._escape

# coding: utf-8
def menu (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select menu to edit</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="edit" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

menu = CompiledTemplate(menu, 'app\\view\\main\\manager\\edit\\menu.html')
join_ = menu._join; escape_ = menu._escape

# coding: utf-8
def restaurant (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="save changes" />\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

restaurant = CompiledTemplate(restaurant, 'app\\view\\main\\manager\\edit\\restaurant.html')
join_ = restaurant._join; escape_ = restaurant._escape

# coding: utf-8
def select_items (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>select item</h3>\n'])
    extend_([u'Select item to edit.\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" value="edit item" />\n'])
    extend_([u'\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])

    return self

select_items = CompiledTemplate(select_items, 'app\\view\\main\\manager\\edit\\select_items.html')
join_ = select_items._join; escape_ = select_items._escape

