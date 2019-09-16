from django import template

register = template.Library() #register the filter

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

#register.filter('cut', cut) #the first is the name you want it to be called 
                            #and the second is the name of the funtion

