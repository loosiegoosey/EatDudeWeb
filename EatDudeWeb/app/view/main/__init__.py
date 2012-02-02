from web.template import CompiledTemplate, ForLoop, TemplateResult

import manager, user, xml
# coding: utf-8
def example_xml (code):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<?xml version="1.0"?>\n'])
    extend_([escape_(code, False), u'\n'])

    return self

example_xml = CompiledTemplate(example_xml, 'app\\view\\main\\example_xml.xml')
join_ = example_xml._join; escape_ = example_xml._escape

# coding: utf-8
def index (name,greeting,hasprofile,latest_restaurants):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" \n'])
    extend_([u'"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'])
    extend_([u'<title>Eat Dude - Mobile Restaurant Menus</title>\n'])
    extend_([u'<link href="/css/public.css" rel="stylesheet" type="text/css" />\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<div id="container">\n'])
    extend_([u'        \n'])
    extend_([u'    <div id="header">&nbsp;</div>\n'])
    extend_([u'<div id="main">\n'])
    extend_([u'                <div id="left">&nbsp;</div>\n'])
    extend_([u'                        <div id="stage">\n'])
    extend_([u'            <p><a href="http://www.eatdude.com"><img src="/css/images/eatdude.gif" alt="eat dude" border="0" longdesc="eat dude mobile restaurant menus" /></a>\n'])
    extend_([u'              </p>\n'])
    extend_([u'            <p>', escape_(greeting, False), u'\n'])
    if hasprofile:
        extend_(['            ', u'         | <a href="/invite/">my account</a>\n'])
        extend_(['            ', u'\n'])
    extend_([u'            </p>\n'])
    extend_([u'            <div id="intro" class="listone">\n'])
    extend_([u'            Use our <strong>free</strong> version of EatDude! to ... <br />\n'])
    extend_([u'            <p>\n'])
    extend_([u'            <em>Restaurant Patrons</em> : Put your favorite take-out <strong>menu</strong> on your phone. </p>\n'])
    extend_([u'            <p>\n'])
    extend_([u'            <em>Restaurant Owners</em> : Use our menu builder and management app to make your restaurant menu available to <strong>mobile</strong> devices. </p>\n'])
    extend_([u'              <h4>Latest Menus  :</h4>\n'])
    extend_([u'              <div id="latest">\n'])
    extend_([u'              <p>\n'])
    extend_([u'              <ul>\n'])
    for key,value in loop.setup(latest_restaurants):
        extend_(['              ', u'                      <li>', escape_(key, False), u' - ', escape_(value, False), u'</li>\n'])
    extend_([u'              </ul>\n'])
    extend_([u'              </p>\n'])
    extend_([u'              </div>\n'])
    extend_([u'              \n'])
    extend_([u'            </div>\n'])
    extend_([u'            <p><a href="/android.html" title="android app">android app</a> | <a href="/iphone.html" title="iphone app">iphone app</a> | <a href="/support.html" title="support">support</a> | <a href="/about.html" title="about">about</a></p>\n'])
    extend_([u'</div>\n'])
    extend_([u'\n'])
    extend_([u'                <div id="right">&nbsp;</div>\n'])
    extend_([u'            \n'])
    extend_([u'            \n'])
    extend_([u'        </div><!--/main-->\n'])
    extend_([u'        \n'])
    extend_([u'    <div id="foot">\n'])
    extend_([u'      <div id="poweredby">\n'])
    extend_([u'        <p>&nbsp;</p>\n'])
    extend_([u'        <p><a href="http://code.google.com/appengine/" title="google app engine" target="_blank">google app engine</a> | <a href="http://webpy.org/" title="webpy" target="_blank">webpy</a> | <a href="http://developer.android.com" title="android" target="_blank">android</a> | <a href="http://wileynet.com" title="android" target="_blank">wileynet</a></p>\n'])
    extend_([u'      </div>\n'])
    extend_([u'      <p>&copy; 2011 eatdude.com 1.0</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'\n'])
    extend_([u'</div><!--/container-->\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, 'app\\view\\main\\index.html')
join_ = index._join; escape_ = index._escape

