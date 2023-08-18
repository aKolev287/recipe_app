from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from .models import Recipe, Tag, Comment, Like, Save
from .views import create_recipe, recipe_list, recipe_detail, like_recipe, save_recipe, delete_recipe, edit_recipe
from .forms import RecipeForm, CommentForm

User = get_user_model()

class RecipeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.tag = Tag.objects.create(name='Test Tag')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
            user=self.user
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            comment='Test Comment'
        )
        self.like = Like.objects.create(
            user=self.user,
            recipe=self.recipe
        )
        self.save = Save.objects.create(
            user=self.user,
            recipe=self.recipe
        )

    def test_recipe_model(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.user, self.user)
        # Add more tests for other fields

    def test_comment_model(self):
        self.assertEqual(str(self.comment), f"Comment by {self.user.username} on {self.recipe.title}")

    def test_like_model(self):
        self.assertEqual(self.like.user, self.user)
        self.assertEqual(self.like.recipe, self.recipe)

    def test_save_model(self):
        self.assertEqual(str(self.save), f"{self.user.username} saved {self.recipe.title}")

class RecipeViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.tag = Tag.objects.create(name='Test Tag')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
            user=self.user
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            comment='Test Comment'
        )
        self.like = Like.objects.create(
            user=self.user,
            recipe=self.recipe
        )
        self.save = Save.objects.create(
            user=self.user,
            recipe=self.recipe
        )

    def test_create_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create-recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/create_recipe.html')


    def test_like_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('like-recipe', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after like
        self.assertEqual(self.recipe.like_set.count(), 0)  # Ensure like was deleted


class RecipeFormTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')


    def test_invalid_recipe_form(self):
        # Submitting the form without required fields should be invalid
        form = RecipeForm(data={})
        self.assertFalse(form.is_valid())

class CommentFormTest(TestCase):

    def test_valid_comment_form(self):
        form_data = {
            'comment': 'Test Comment',
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        # Submitting the form without the comment field should be invalid
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())