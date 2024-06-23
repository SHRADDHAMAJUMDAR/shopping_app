from django import template 
  
register = template.Library() 
@register.filter()
def getvalbykey(dict,key):
    key=str(key)
    return dict.get(key)