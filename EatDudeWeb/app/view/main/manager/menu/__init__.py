from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def view (r,m,ms,c,mcount,i):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="menu_container">\n'])
    extend_([u'\n'])
    extend_([u'<p>\n'])
    extend_([u'<div id="menu">\n'])
    extend_([u'<div id="menu_head">menus for ', escape_(r.name, False), u' :\n'])
    extend_([u'\n'])
    for key,value in loop.setup(m):
        extend_([u'    | <a href="/manager/menu/view/', escape_(key, False), u'" >', escape_(value.name, False), u'</a>\n'])
        extend_([u'\n'])
    extend_([u'</div>        \n'])
    extend_([u'<h1>', escape_(r.name, False), u'</h1>\n'])
    extend_([u'<h2>', escape_(r.phone, False), u'</h2>\n'])
    extend_([u'<address>', escape_(r.address, False), u'</address>\n'])
    extend_([u'<address>', escape_(r.city, False), u', ', escape_(r.state, False), u'</address>\n'])
    extend_([u'<div id="edit"> <a href="/manager/edit/restaurant" >  << edit </a> </div>\n'])
    extend_([u'<hr />\n'])
    extend_([u'\n'])
    extend_([u'<h3>menu : ( ', escape_(ms.name, False), u' )</h3>\n'])
    extend_([u'<div id="edit"> <a href="/manager/editmenu/', escape_(ms.key().id(), False), u'" > << edit </a> </div>\n'])
    extend_([u'<hr />\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    if not c :
        extend_([u'    <h2>Add a Category</h2>\n'])
        extend_([u'    add some categories - i.e. ( salads, beverages, appetizers )\n'])
        extend_([u'    <div id="edit"> <a href="/manager/add/category" > << add </a> </div>\n'])
        extend_([u'<hr />\n'])
        extend_([u'\n'])
    else :
        for key, value in loop.setup(i):
            extend_(['    ', u'\n'])
            extend_(['    ', u'<div class="category"><h2 class="category">  ', escape_(key.split('|')[1], False), u'</h2> ( <a href="/manager/editcategory/', escape_(key.split('|')[0], False), u'"> edit </a> )</div>\n'])
            extend_(['    ', u'<div class="mainitem">\n'])
            extend_(['    ', u'\n'])
            for x in loop.setup(value):
                extend_(['    ', u'    <div class="item">\n'])
                if x.itemNumber :
                    extend_(['    ', u'<div class="number">( # ', escape_(x.itemNumber, False), u' )</div> <br />\n'])
                    extend_(['    ', u'\n'])
                extend_(['    ', u'<h3 class="item">', escape_(x.itemName, False), u'</h3> ( <a href="/manager/edititem/', escape_(x.key().id(), False), u'" > edit </a> ) <br />\n'])
                extend_(['    ', escape_(x.itemDesc, False), u' <br />\n'])
                extend_(['    ', escape_(x.itemPrice, False), u' <br />\n'])
                extend_(['    ', u'</div>\n'])
            extend_(['    ', u'</div>\n'])
            extend_(['    ', u'\n'])
            if value == [] :
                extend_(['    ', u'    no items added for this category yet -<a href="/manager/additem/', escape_(key.split('|')[0], False), u'" > add one >></a>\n'])
            extend_(['    ', u'<hr  />\n'])
            extend_(['    ', u'\n'])
    extend_([u'</div>\n'])
    extend_([u'</p>\n'])
    extend_([u'</div>\n'])

    return self

view = CompiledTemplate(view, 'app\\view\\main\\manager\\menu\\view.html')
join_ = view._join; escape_ = view._escape

