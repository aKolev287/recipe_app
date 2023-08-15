from django.shortcuts import render
from spice_swap.recipes.models import Recipe

def index(request):
    # highest_rated_recipes = Recipe.objects.order_by('-rating')[:5]
    newest_recipes = Recipe.objects.order_by('-date')[:5]
    context = {
    #    'highest_rated_recipes': highest_rated_recipes,
        'newest_recipes': newest_recipes,
    }
    return render(request, 'common/index.html', context)
