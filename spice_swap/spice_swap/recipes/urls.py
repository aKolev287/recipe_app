from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipe'),
    path('list/', views.recipe_list, name='recipe-list'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
]
