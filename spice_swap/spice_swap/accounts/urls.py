from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit-profile'),
    path('delete_profile/<int:pk>/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('details_profile/<slug:username>/', views.profile_details, name='details-profile'),
    path('custom-login-redirect/', views.custom_login_redirect, name='custom-login-redirect'),
]
