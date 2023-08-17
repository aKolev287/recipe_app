from django.shortcuts import render
from spice_swap.recipes.models import Recipe, Tag
from django.db.models import Count

def index(request):
    highest_rated_recipes = Recipe.objects.annotate(num_likes=Count('like')).order_by('-num_likes')[:5]
    # highest_rated_recipes = Recipe.objects.order_by('-rating')[:5]
    newest_recipes = Recipe.objects.order_by('-date')[:5]
    context = {
        'highest_rated_recipes': highest_rated_recipes,
        'newest_recipes': newest_recipes,
    }
    return render(request, 'common/index.html', context)

def breakfast_recipes(request):
    tag = Tag.objects.get(name='Breakfast')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/breakfast.html', context)

def lunch_recipes(request):
    tag = Tag.objects.get(name='Lunch')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/lunch.html', context)

def dinner_recipes(request):
    tag = Tag.objects.get(name='Dinner')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/dinner.html', context)

def snacks_recipes(request):
    tag = Tag.objects.get(name='Snacks')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/snacks.html', context)


def main_dish_recipes(request):
    tag = Tag.objects.get(name='Main Dish')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/main_dish.html', context)

def desserts(request):
    tag = Tag.objects.get(name='Desserts')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/desserts.html', context)