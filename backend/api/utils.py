from django.http import HttpResponse


def convert_txt(shop_cart):
    file_name = 'shopping_cart.txt'
    shopping_cart = []
    shopping_cart.append('Спасибо, что пользуетесь Foodgram.')
    shopping_cart.append('Ваш сводный список ингредиентов для покупки:')
    for ing in shop_cart:
        name = ing.get('ingredient__name')
        measurement_unit = ing.get('ingredient__measurement_unit')
        amount = ing.get('ingredient_total')
        shopping_cart.append(f'{name} ({measurement_unit}) - {amount}')
    content = '\n'.join(shopping_cart)
    response = HttpResponse(content, content_type='text/plain,charset=utf8')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
