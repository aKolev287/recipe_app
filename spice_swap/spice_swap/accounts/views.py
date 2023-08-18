from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.urls import reverse_lazy # for easier navigation
from django.contrib.auth import mixins as auth_mixins
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required # for function based views 
from django.views.generic.edit import UpdateView
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.views.decorators.csrf import csrf_protect
from spice_swap.recipes.models import Recipe, Save
from .forms import CustomUserCreationForm

# K4a9a556QEA
# The user Model
UserModel = get_user_model()

# Register a user
class RegisterUserView(views.CreateView):
    template_name = 'accounts/profile-create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('custom-login-redirect')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result
    
# Login the user
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/profile-login.html'

# Logout the user
class LogoutUserView(auth_views.LogoutView):
    pass

# delete the user
class ProfileDeleteView(auth_mixins.LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'  
    success_url = reverse_lazy('index')

# Edit the profile
class EditProfileView(auth_mixins.LoginRequiredMixin, UpdateView):
    model = get_user_model() 
    fields = ['first_name', 'last_name', 'username', 'email']  
    template_name = 'accounts/profile-edit.html'  
    success_url = reverse_lazy('details-profile') 

    def get_object(self, queryset=None):
        return self.request.user  # Retrieve the user object

    def form_valid(self, form):
        response = super().form_valid(form)
        
        return response
    
def profile_delete(request):
    return render(request, 'accounts/profile-delete.html',)

@login_required
def profile_details(request, username):
    user = get_object_or_404(UserModel, username=username)
    recipes = Recipe.objects.filter(user=user)  # Get user's recipes
    saved_recipes = Save.objects.filter(user=user).select_related('recipe')
    context = {
        'user': user,
        'recipes': recipes,
        'saved_recipes': saved_recipes
    }
    return render(request, 'accounts/profile-details.html', context)

# Custom login redirects because global settings are stupid and the lambda function didn't work (or I didn't know how to fix it otherwise)
def custom_login_redirect(request):
    username = request.user.username
    return redirect('details-profile', username=username)