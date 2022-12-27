from django.http import HttpResponse


def convert_txt(shop_cart):
    file_name = 'shopping_cart.txt'
    shopping_cart = []
    for ing in shop_cart:
        name = ing['ingredient__name']
        measurement_unit = ing['ingredient__measurement_unit']
        amount = ing['ingredient_total']
        shopping_cart.append(f'{name} ({measurement_unit}) - {amount}')
    content = '\n'.join(shopping_cart)
    response = HttpResponse(content, content_type='text/plain,charset=utf8')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
