from django import template


register = template.Library()


@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def div(value, arg):
    return value / arg

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def add(value, arg):
    return value + arg

@register.filter(name='stringify')
def stringify(value):
    return str(value)

@register.filter(name='lower')
def lower(value):
    return value.lower()

# Фильтр для цензуры имейла. Используется в html шаблоне через user.email|censor
@register.filter(name='censor_email')
def censor_email(email):
    local_part, domain = email.split('@')
    if len(local_part) > 2:
        censored_local = local_part[0] + '*' * (len(local_part) - 2) + local_part[-1]
    else:
        censored_local = local_part[0] + '*'
    return f'{censored_local}@{domain}'

@register.filter(name='censor_phone_number')
def censor_phone_number(phone):
    censored_phone = phone[:5] + ('*' * (len(phone[5:-2]))) + phone[-2:]
    return censored_phone

# Возвращает имя аттрибута объекта
@register.filter
def get_attr(obj, attr_name):
    print('РАБОТАЕТ GET_ATTR', attr_name , getattr(obj, attr_name))
    return getattr(obj, attr_name, None)

# Возвращает булево значение, есть ли у объекта есть аттрибут
@register.filter
def has_attr(obj, attr_name):
    print('РАБОТАЕТ HAS_ATTR', attr_name, hasattr(obj, attr_name))
    return hasattr(obj, attr_name)


