from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
from .models import Order

fake_db = [
    {'id': 1, 'title': 'Анжделина Джоли', 'content': 'Биография Анжделины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'Биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

menu = [
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
]


def start(request):
    return render(request, 'trainapp/start.html', context={'title': 'Главная Страница',
                                                           'menu': menu,
                                                           'posts': fake_db})


def about(request):
    data = {'title': 'About us', 'content': 'Here is to be some info about us in the near future'}
    return render(request, 'trainapp/about.html', context=data)


def contact(request):
    data = {'title': 'Our contacts', 'content': 'Here is to be our contact information'}
    return render(request, 'trainapp/contact.html', context=data)


def login(request):
    return HttpResponse('<h1> Authorization page </h1>')


def post(request, post_id):
    return HttpResponse(f'Пост с id: {post_id}')


def order_list(request):
    today = datetime.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    last_7_days = Order.objects.filter(order_date__gte=last_week)
    last_30_days = Order.objects.filter(order_date__gte=last_month)
    last_365_days = Order.objects.filter(order_date__gte=last_year)

    context = {
        'last_7_days': orders_last_7_days,
        'last_30_days': orders_last_30_days,
        'last_365_days': orders_last_365_days,
    }

    return render(request, 'filterorders.html', context)

