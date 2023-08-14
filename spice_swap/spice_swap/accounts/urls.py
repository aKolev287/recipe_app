from django.urls import path

from .views import RegisterUserView, profile_edit, profile_delete, LoginUserView, profile_details, LogoutUserView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('edit_profile/', profile_edit, name='edit-profile'),
    path('delete_profile/<int:pk>/', ProfileDeleteView.as_view(), name='delete-profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('details_profile/', profile_details, name='details-profile'),
]