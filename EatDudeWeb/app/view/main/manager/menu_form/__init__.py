from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def categoryForm (form, menu_id):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h3>Categories</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="hidden" id="menu_id" value="', escape_(menu_id, False), u'" name="menu_id" />\n'])
    extend_([u'<input type="submit" value="Add Categories" />\n'])
    extend_([u'</form>\n'])

    return self

categoryForm = CompiledTemplate(categoryForm, 'app\\view\\main\\manager\\menu_form\\categoryForm.html')
join_ = categoryForm._join; escape_ = categoryForm._escape

# coding: utf-8
def index (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h3>Select Restaurant</h3>\n'])
    extend_([u'<form name="test" method="POST"> \n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="hidden" id="menu_id" value="" name="menu_id" />\n'])
    extend_([u'<input type="submit" value="Create Menu" />\n'])
    extend_([u'</form>\n'])

    return self

index = CompiledTemplate(index, 'app\\view\\main\\manager\\menu_form\\index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def itemForm (form, menu_id, mcm_names):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h3>Items</h3>\n'])
    extend_([u'<form name="test" method="POST">\n'])
    extend_([u'<table><tr><th><label for="category_name">category name</label></th><td><select id="category_name" name="category_name"> ', escape_(mcm_names, False), u' </select></td></tr></table>\n'])
    if not form.valid:
        extend_([u'<p>Sorry, your input was invalid.</p>\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'<input type="hidden" id="menu_id" value="', escape_(menu_id, False), u'" name="menu_id" />\n'])
    extend_([u'<input type="submit" value="Add Item" />\n'])
    extend_([u'</form>\n'])

    return self

itemForm = CompiledTemplate(itemForm, 'app\\view\\main\\manager\\menu_form\\itemForm.html')
join_ = itemForm._join; escape_ = itemForm._escape

