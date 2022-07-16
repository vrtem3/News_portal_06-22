from django import template


register = template.Library()


black_list_word = ['fuck', 'lol', 'bot', 'FUCK']


@register.filter()
def censor(value):
   if not isinstance(value, str):
       raise ValueError('Нельзя цензурировать НЕ строку')

   for word in black_list_word:
       value = value.replace(word[1:], '*' * (len(word)-1))

   return value
