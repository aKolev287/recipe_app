from django import forms
from .models import Recipe, Tag

class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Allow tags to be optional
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image', 'tags']
