from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .views import RegisterUserView, LoginUserView, ProfileDeleteView, EditProfileView

UserModel = get_user_model()

class AccountsViewsTest(TestCase):

    def setUp(self):
        self.test_user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-create.html')
        

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-login.html')
        
        

    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit.html')
        

