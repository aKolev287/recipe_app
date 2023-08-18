from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipe'),
    path('list/', views.recipe_list, name='recipe-list'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('like/<int:recipe_id>/', views.like_recipe, name='like-recipe'),
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete-recipe'),
    path('<int:recipe_id>/edit/', views.edit_recipe, name='edit-recipe'),
    path('save/<int:recipe_id>/', views.save_recipe, name='save-recipe'),
    

]
