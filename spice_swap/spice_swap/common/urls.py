from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('breakfast/', views.breakfast_recipes, name='breakfast'),
    path('lunch/', views.lunch_recipes, name='lunch'),
    path('dinner/', views.dinner_recipes, name='dinner'),
    path('snacks/', views.snacks_recipes, name='snacks'),
    path('main_dish/', views.main_dish_recipes, name='main_dish'),
    path('desserts/', views.desserts, name='desserts'),
    path('feedback/', views.feedback_page, name='feedback-page'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)