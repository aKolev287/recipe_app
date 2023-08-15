from django.urls import path

from .views import RegisterUserView, EditProfileView , profile_delete, LoginUserView, profile_details, LogoutUserView, ProfileDeleteView, custom_login_redirect

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('edit_profile/', EditProfileView.as_view(), name='edit-profile'),
    path('delete_profile/<int:pk>/', ProfileDeleteView.as_view(), name='delete-profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('details_profile/<slug:username>/', profile_details, name='details-profile'),
    path('custom-login-redirect/', custom_login_redirect, name='custom-login-redirect'),
]
