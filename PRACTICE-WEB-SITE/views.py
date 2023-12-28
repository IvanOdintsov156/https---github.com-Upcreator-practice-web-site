from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1>')

def about_practice(request):
    return HttpResponse('<h1>О практике</h1>')

def confidence(request):
    return HttpResponse('<h1>Страница конфиденциальности</h1>')
def contacts(request):
    return HttpResponse('<h1>Контакты</h1>')

def error_404(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')

def error_500(request):
    return HttpResponse('<h1>Внутренняя ошибка сервера</h1>')

def error_403(request, exception):
    return HttpResponse('<h1>Доступ запрещен</h1>')