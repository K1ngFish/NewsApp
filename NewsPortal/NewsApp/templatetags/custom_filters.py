from django import template


register = template.Library()

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.


@register.filter()
def censor(value):
    banned_words = ['преступлениях', 'России', 'стратегии']

    if not isinstance (value, str):
        raise TypeError(f"Недопустимое значение '{type(value)}' Нужно ввести строковое значение")
    words = value.replace(',', '').split()
    for word in words:
        if word in banned_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value
