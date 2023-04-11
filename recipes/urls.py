from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-recipe', views.create_recipe, name="create-recipe"),
    path('<int:recipe_id>', views.recipe_detail, name='recipedetail'),

]
