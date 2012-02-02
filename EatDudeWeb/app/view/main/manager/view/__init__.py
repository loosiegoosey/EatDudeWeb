from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def category():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'category.html\n'])

    return self

category = CompiledTemplate(category, 'app\\view\\main\\manager\\view\\category.html')
join_ = category._join; escape_ = category._escape

# coding: utf-8
def item():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'item.html\n'])

    return self

item = CompiledTemplate(item, 'app\\view\\main\\manager\\view\\item.html')
join_ = item._join; escape_ = item._escape

# coding: utf-8
def menu():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'menu.html\n'])

    return self

menu = CompiledTemplate(menu, 'app\\view\\main\\manager\\view\\menu.html')
join_ = menu._join; escape_ = menu._escape

# coding: utf-8
def restaurant():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'restaurant.html\n'])

    return self

restaurant = CompiledTemplate(restaurant, 'app\\view\\main\\manager\\view\\restaurant.html')
join_ = restaurant._join; escape_ = restaurant._escape

