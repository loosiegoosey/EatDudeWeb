from web.template import CompiledTemplate, ForLoop, TemplateResult

import add, delete, edit, main, menu, menu_form, view
# coding: utf-8
def error():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h1>error</h1>\n'])

    return self

error = CompiledTemplate(error, 'app\\view\\main\\manager\\error.html')
join_ = error._join; escape_ = error._escape

# coding: utf-8
def head (nest,user):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<?xml version="1.0" encoding="UTF-8"?>\n'])
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'])
    extend_([u'<link rel="stylesheet" type="text/css" href="/public/css/main.css"/>\n'])
    extend_([u'<title>Menu Manager</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<div id="top">hi ', escape_(user, False), u'</div>\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'        ', escape_(nest, False), u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

head = CompiledTemplate(head, 'app\\view\\main\\manager\\head.html')
join_ = head._join; escape_ = head._escape

# coding: utf-8
def help ():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="form1">\n'])
    extend_([u'<h3>Help</h3>\n'])
    extend_([u'If you have any questions or need help email <a href="mailto:admin@eatdude.com" />admin@eatdude.com</a> or phone 805-218-8451.\n'])
    extend_([u'</div>\n'])

    return self

help = CompiledTemplate(help, 'app\\view\\main\\manager\\help.html')
join_ = help._join; escape_ = help._escape

