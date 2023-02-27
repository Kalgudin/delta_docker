from datetime import datetime
from jinja2 import Template

import requests

COUNT = 25

# for id in range(43287149, 43287349):
#     url_history = f'https://wbx-content-v2.wbstatic.net/price-history/{id}.json'
#     try:
#         all_prices = requests.get(url_history).json()
#         print(all_prices)
#     except Exception as ex:
#         print(f'Новый товар( {id} ), нет средней цены(ошибка - {ex})')


all_prices = [{'dt': 1662854400, 'price': {'RUB': 30733}}, {'dt': 1663459200, 'price': {'RUB': 34100}}, {'dt': 1664064000, 'price': {'RUB': 31400}}, {'dt': 1664668800, 'price': {'RUB': 27850}}, {'dt': 1665273600, 'price': {'RUB': 28000}}, {'dt': 1665878400, 'price': {'RUB': 32425}}, {'dt': 1666483200, 'price': {'RUB': 32033}}, {'dt': 1667088000, 'price': {'RUB': 32936}}, {'dt': 1667692800, 'price': {'RUB': 33400}}, {'dt': 1668297600, 'price': {'RUB': 33709}}, {'dt': 1668902400, 'price': {'RUB': 35340}}, {'dt': 1669507200, 'price': {'RUB': 35914}}, {'dt': 1670112000, 'price': {'RUB': 35865}}, {'dt': 1670716800, 'price': {'RUB': 33060}}, {'dt': 1671321600, 'price': {'RUB': 34012}}, {'dt': 1671926400, 'price': {'RUB': 35843}}, {'dt': 1672531200, 'price': {'RUB': 34971}}]
print(len(all_prices))
if len(all_prices) > 4:
    all_prices = all_prices[-4:]
print(all_prices)
# print(all_prices[-2:])
print(datetime.now().timestamp())

cat_js = {'childs': [{'childs': [{'id': 130457,
                         'name': 'Блузки',
                         'parent': 130456,
                         'query': 'kind=2&subject=41&ext=31142;31138',
                         'shard': 'new_year1',
                         'url': '/catalog/novyy-god/vecherniy-obraz/bluzki'}],
              'id': 130456,
              'name': 'Вечерний образ',
              'parent': 128518,
              'query': 'kind=2;1&subject=41;1429;225;155;157;2649;177;149;69;184;185;38;11&ext=31142;31138',
              'shard': 'new_year1',
              'url': '/catalog/novyy-god/vecherniy-obraz'}],
  'id': 128518,
  'landing': True,
  'name': 'Новый год',
  'query': 'subject=1;2;213;257;270;1590&ext=26830;31138;31142;67470',
  'seo': 'Каталог товаров на Новый год',
  'shard': 'blackhole',
  'url': '/catalog/novyy-god'}

req = 'https://wbx-content-v2.wbstatic.net/price-history/39490881.json'
prod_js = {"__sort":78751,"ksort":55000,"ksale":0,"time1":4,"time2":43,"dist":556,"id":39490881,
           "root":29706341,"kindId":2,"subjectId":38,"subjectParentId":1,
           "name":"Юбка прямая кожаная миди кожаная черная",
           "brand":"CHELER","brandId":233715,"siteBrandId":243715,"supplierId":194813,
           "sale":21,"priceU":280000,"salePriceU":221200,"averagePrice":117600,"pics":10,
           "rating":5,"feedbacks":2127,
           "colors":[{"name":"черный","id":0}],
           "sizes":[{"name":"40","origName":"40","rank":6001,"optionId":80031320,"wh":507,"sign":"5WUbprPO51yebwDTBYkwmx+kSAs="},{"name":"42","origName":"42","rank":6401,"optionId":80031321,"wh":507,"sign":"SmZIriHt03vDewi3ihhSai3m/Cs="},{"name":"44","origName":"44","rank":6801,"optionId":80031322,"wh":507,"sign":"7AJ89H8cU7hdlVi0uOiAUDtc6fk="},{"name":"46","origName":"46","rank":7201,"optionId":80031323,"wh":507,"sign":"owoMPhOIOKq3AEkfKr0HteJZLUc="},{"name":"48","origName":"48","rank":7601,"optionId":80031324,"wh":117986,"sign":"Am/sA+9AdZ0aGqUzIh2zgAqOAXU="},{"name":"50","origName":"50","rank":8001,"optionId":103832221,"wh":507,"sign":"fvGkDfBWUdxMF5YCU6o1etlBB5Y="},{"name":"52","origName":"52","rank":8301,"optionId":211935245,"wh":117986,"sign":"zxIfO1h9nOI5YNOG7ahPu+JD6Ww="},{"name":"54","origName":"54","rank":8501,"optionId":211935246,"wh":117986,"sign":"27Ekkzy2mj+2x7931GzSXXjEeEI="}],
           "diffPrice":'false'}

url_OK = 'https://catalog.wb.ru/catalog/blazers_wamuses/catalog?appType=1&curr=rub&dest=-1075831,-77677,-398551,12358499&locale=ru&page=19&sort=popular&spp=0&kind=2&subject=149;155;156;209;225'
url_NT = 'https://catalog.wb.ru/catalog/presets/women_clothes/catalog?appType=1&curr=rub&dest=-1075831,-77677,-398551,12358499&locale=ru&page=1&sort=popular&spp=0&preset=1001'
url_BA = 'https://catalog.wb.ru/catalog/{shard}/catalog?appType=1&curr=rub&dest=-1075831,-77677,-398551,12358499&locale=ru&page={page}&sort=popular&spp=0&{query}'

context = {'category': "<QuerySet [<Category: Мужчинам>, <Category: Аксессуары>,...(remaining elements truncated)...']>, ",
           'form': "<SearchForm bound=False, valid=Unknown, fields=(search)>, ",
           'is_paginated': True,
           'object_list': "<QuerySet [<Product: подгузники-трусики 12-17 кг, 5р, 15 шт>, <Product: комбинезон для новорождённых мальчика или девочки утепленный>, ]",
           'page_obj':" <Page 1 of 72>, ",
           'paginator': "<django.core.paginator.Paginator object at 0x000001FB7DDDECD0>",
           'products':" <QuerySet [<Product: подгузники-трусики 12-17 кг, 5р, 15 шт>, <Product: комбинезон для новорождённых мальчика или девочки утепленный>, ]",
           'title': 'Delta',
           'view': "<delta.views.ViewProducts object at 0x000001FB7DAE1890>"}
context2 = '''{
 'category': <QuerySet [<Category: Мужчинам>, <Category: Аксессуары>, <Category: Детям>, <Category: Электроника>, <Category: Автотовары>, <Category: Женщинам>, <Category: Экспресс-доставка>, <Category: Цифровые товары>, <Category: Дом>, <Category: Игрушки>, <Category: Книги>, <Category: Красота>, <Category: Обувь>, <Category: Спорт>, <Category: Ювелирные изделия>, <Category: Бренды  >, <Category: Сад и дача>, <Category: Канцтовары>, <Category: Зоотовары>, <Category: Продукты>, '...(remaining elements truncated)...']>,
 'form': <SearchForm bound=True, valid=True, fields=(search)>,
 'products': <QuerySet [<Product: подгузники-трусики 12-17 кг, 5р, 15 шт>, <Product: подгузники-трусики m 6-11 кг 58 шт>, <Product: подгузники для детей m 6-11кг 64 шт>, <Product: подгузники для детей до 5 кг 90 шт>, <Product: подгузники-трусики s 4-8 кг 62 шт>, <Product: подгузники-трусики m 6-11 кг 74 шт>, <Product: подгузники-трусики l 9-14 кг 56 шт>, <Product: трусики-подгузники elite soft (3) 6-11кг, 108 шт>, <Product: трусики-подгузники для детей размер xxl 15-28 кг 32 шт>, <Product: подгузники-трусики happy junior, размер 5(11-18 кг), 40 шт>, <Product: подгузники - трусики детские happy maxi, размер 4 (8- 14 кг)…>, <Product: подгузники-трусики детские размер m для детей весом 6-11 кг…>, <Product: подгузники трусики киоши размер l размер 4 для детей весом о…>, <Product: подгузники-трусики детские размер xl для детей весом 12-18 к…>, <Product: подгузники-трусики детские размер xxl для детей весом 16+ кг…>, <Product: трусики - подгузники ультратонкая серия детские для мальчико…>, <Product: трусики - подгузники ультратонкая серия детские для мальчико…>, <Product: трусики - подгузники детские одноразовые для мальчиков и дев…>, <Product: подгузники трусики детские размер 4 l>, <Product: подгузники трусики детские ночные 6 размер xxl 15-20кг, 34шт>, '...(remaining elements truncated)...']>,
 'title': 'Delta'
 
 'is_paginated': True,
 'object_list': "<QuerySet [<Product://///
 'page_obj':" <Page 1 of 72>, ",
 'paginator': "<django.core.paginator.Paginator object at 0x000001FB7DDDECD0>",
 'view': "<delta.views.ViewProducts object at 0x000001FB7DAE1890>"
 
 
 }'''





uuu = 'https://catalog.wb.ru/catalog/***/catalog?appType=1&curr=rub&dest=-1075831,-77677,-398551,12358499&locale=ru&page=1&sort=popular&spp=0&'