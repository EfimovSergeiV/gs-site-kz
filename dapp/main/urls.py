"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from main.views import *
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageView.as_view()),

    # Роутинг приложений
    path('a/', admin.site.urls),
    path('c/', include('catalog.urls')),
    path('o/', include('orders.urls')),
    path('c/', include('content.urls')),
    path('u/', include('user.urls')),
    # path('s/', include('services.urls')),
    # path('f/', include('forum.urls')),
    # path('sber/', include('sber.urls')),
    # path('dreamkas/', include('dreamkas.urls')),

    # Пользовательский опыт
    path('auth/', AuthTokenView.as_view()),                 # Авторизация - Вход
    path('logout/', LogoutView.as_view()),                  # Авторизация - Выход
    path('signup/', SignUpView.as_view()),                  # Подробная регистрация
    path('u/profile/', UserProfileView.as_view()),          # Информация о пользователе
    path('u/change/', ChangeUserView.as_view()),            # Изменить инфо пользователя    
    path('u/reset/', RestoreUserPassword.as_view()),        # Восстановить пароль

    # path('subscriebe/', SubscriebeUserView.as_view()),    # Быстрая регистрация

    # Поиск местоположения пользователя
    path('location/', LocationFromIPView.as_view()),      
    path('coordinates/', LocationFromCoordinateView.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))



admin.site.site_header = 'Администрирование приложения'
admin.site.index_title = 'Интернет магазин Главный сварщик'
admin.site.site_title = 'Администрирование приложения'