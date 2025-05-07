from django import template

register = template.Library()


@register.filter(name='truncate5')
def truncate5(value):
    result = value[0:5]
    return result


@register.filter(name='t_n')
def truncate_n(value, n):
    result = value[0:n]
    return result

# register.filter('truncate5', truncate5)
# register.filter('t_n', truncate_n)
