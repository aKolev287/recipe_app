# acc/views.py 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.urls import reverse_lazy # for easier navigation
from django.contrib.auth import mixins as auth_mixins
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required # for function based views 

from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from .forms import CustomUserCreationForm

# password: H3lo_W0r1d_12

# Validate the user
UserModel = get_user_model()

# Register a user
class RegisterUserView(views.CreateView):
    template_name = 'accounts/profile-create.html'
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy('details-profile')

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

#class Profile(auth_mixins.LoginRequiredMixin, views.ListView):
#    model = UserModel
#    template_name = 'accounts/profile-details.html'

class ProfileDeleteView(auth_mixins.LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'  
    success_url = reverse_lazy('index')

def profile_edit(request):
    return render(request, 'accounts/profile-edit.html',)

def profile_delete(request):
    return render(request, 'accounts/profile-delete.html',)

def profile_details(request):
    
    return render(request, 'accounts/profile-details.html')