from django import forms
from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
    )

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'category',
            'ingredients',
            'instructions',
        ]
        labels = {
            'title': 'Recipe Title',
            'description': 'Recipe Description',
            'category': 'Category',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'instructions': forms.Textarea(attrs={'rows': 10}),
        }
