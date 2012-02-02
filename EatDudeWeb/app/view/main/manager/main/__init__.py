from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def view (m,mcount):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="menu_container">\n'])
    extend_([u'\n'])
    extend_([u'<p>\n'])
    extend_([u'<div id="menu">\n'])
    extend_([u'        <div id="menu_head">you have ', escape_(mcount, False), u' menu :</div>\n'])
    extend_([u'\n'])
    if m :
        extend_([u'    click on the menu you wish to edit<br />\n'])
        for key,value in loop.setup(m):
            extend_(['    ', u'<a href="/manager/menu/view/', escape_(key, False), u'" >', escape_(value.name, False), u'</a> <br />\n'])
            extend_(['    ', u'\n'])
    else :
        extend_([u'    You currently have no menus for this restaurant. <a href="/manager/add/menu" >click here</a> and add a menu.\n'])
        extend_([u'\n'])
        extend_([u'\n'])
    if not mcount == 0 :
        extend_([u'    <br />\n'])
        extend_([u'    add another <a href="/manager/add/menu">menu >></a>\n'])
        extend_([u'\n'])
        extend_([u'\n'])
    extend_([u'</div>\n'])
    extend_([u'</p>\n'])
    extend_([u'</div>\n'])

    return self

view = CompiledTemplate(view, 'app\\view\\main\\manager\\main\\view.html')
join_ = view._join; escape_ = view._escape

