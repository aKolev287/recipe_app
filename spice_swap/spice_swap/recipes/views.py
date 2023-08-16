from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CommentForm
from .models import Recipe, Comment, Like

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
    comments = Comment.objects.filter(recipe=recipe)
    comment_form = CommentForm()
    like_count = recipe.like_set.count()

    user_has_liked_recipe = False
    if request.user.is_authenticated:
        user_has_liked_recipe = Like.objects.filter(user=request.user, recipe=recipe).exists()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe-detail', recipe_id=recipe_id)
        
    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
        'like_count': like_count,
        'user_has_liked_recipe': user_has_liked_recipe,
        }
    return render(request, 'recipes/recipe_detail.html', context)

@login_required
def like_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    like = Like.objects.filter(user=user, recipe=recipe).first()
    # Check if the user has already liked the recipe
    if not Like.objects.filter(user=user, recipe=recipe).exists():
        Like.objects.create(user=user, recipe=recipe)
    if like:
        like.delete() 
    return redirect('recipe-detail', recipe_id=recipe_id)