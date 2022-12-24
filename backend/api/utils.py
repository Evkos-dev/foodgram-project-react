from django.http import HttpResponse


def convert_txt(shop_list):
    file_name = 'shopping_list.txt'
    shopping_list = []
    for ing in shop_list:
        name = ing['ingredient__name']
        measurement_unit = ing['ingredient__measurement_unit']
        amount = ing['ingredient_total']
        shopping_list.append(f'{name} ({measurement_unit}) - {amount}')
    content = '\n'.join(shopping_list)
    response = HttpResponse(content, content_type='text/plain,charset=utf8')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
