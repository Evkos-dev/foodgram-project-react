# Foodgram - продуктовый помощник
### Описание проекта
Онлайн-сервис Foodgram («Продуктовый помощник») создан для кулинаров. В сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать в формате .txt сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Реализовано CI и CD проекта. При пуше изменений в главную ветку, проект автоматически тестируется на соотвествие требованиям PEP8. После успешного прохождения тестов, собирается образ web-контейнера и front-контейнера и автоматически размещается в облачном хранилище DockerHub. Размещенный образ автоматически разворачивается на боевом сервере вмете с контейнером веб-сервера nginx и базой данных PostgreSQL.

### Примеры запросов
- Рецепты (Получить список всех рецептов или отдельного рецепта по id, создать новый рецепт, редактировать или удалить рецепт по id для авторизованного пользователя)

  ###### Пример GET запроса:
  `"/api/recipes/{id}/"`
  ###### Пример ответа:
```
[
  {
    "id": 0,
    "tags": [
      {
        "id": 0,
        "name": "Завтрак",
        "color": "#E26C2D",
        "slug": "breakfast"
      }
    ],
    "author": {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": false
    },
    "ingredients": [
      {
        "id": 0,
        "name": "Картофель отварной",
        "measurement_unit": "г",
        "amount": 1
      }
    ],
    "is_favorited": true,
    "is_in_shopping_cart": true,
    "name": "string",
    "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
    "text": "string",
    "cooking_time": 1
  }
]
```
  
- Подписки (Получить список всех подписок, подписаться или отписаться)

  ###### Пример POST запроса:
  `/api/users/{id}/subscribe/`
  ###### Пример ответа:
```
[ 
  {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": true,
    "recipes": [
      {
        "id": 0,
        "name": "string",
        "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
        "cooking_time": 1
      }
    ],
    "recipes_count": 0
   }
]
```
  
- Пользователи (Получить список всех пользовтелей, получение информации об отдельном пользователе)  
  
- Регистрация пользователя (Получение, удаоение токена)

- Список покупок (Добавление и удаление рецепта из списка покупок, скачать список покупок)

### Стек технологий
- Python 3.7
- Django 3.2.16
- Django Rest Framework 3.14.0
- PostgreSQL
- gunicorn 20.1.0
- Nginx

### Документация к проекту
Документация для API после установки доступна по адресу `api/docs/redoc.html`.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Evkos-dev/foodgram-project-react.git`

`cd foodgram-project-react`

В директории infra/ создать файл .env с переменными окружения для работы с базой данных:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Запустить Docker-compose:

`docker-compose up`

Выпонить по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py import_ingredients ingredients.csv
docker-compose exec web python manage.py import_tags tags.csv
```

Остановить контейнер:
`docker-compose stop`

Проект доступен по адресу:
`http:///`

[![CI](https://github.com/Evkos-dev/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master)](https://github.com/Evkos-dev/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

### Об авторе

Я студент Яндекс.Практикума, обучаюсь Backend разработке на Python. Этот проект - учебный, где я реализовывал API сайта - продуктового помощника с помощью Django Rest Framework.
