from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment, Recipe
from .forms import CommentForm

# Create your views here.


@login_required
def add_comment(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipedetail', pk=recipe.pk)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(recipe=recipe)
    return render(request, 'recipedetail.html', {'form': form, 'comments': comments})
