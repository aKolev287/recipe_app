from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            form.save_m2m()  # Save tags
            return redirect('recipe-list')
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipes/create_recipe.html', context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)
