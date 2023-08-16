from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='./user_images/')
    tags = models.ManyToManyField(Tag, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    # Recipe likes
    likes = models.PositiveIntegerField(default=0)

    # Associate recipe with user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
