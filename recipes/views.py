from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.all()

    return render(request, 'index.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.category = form.cleaned_data['category']
            recipe.save()
            return redirect('add_recipe_to_category', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'createrecipe.html', {'form': form})
