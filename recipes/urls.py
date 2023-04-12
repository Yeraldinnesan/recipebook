from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-recipe', views.create_recipe, name="create-recipe"),
    path('search-recipe', views.search_recipe, name="searchrecipe"),
    # path('<int:recipe_id>', views.recipe_detail, name='recipedetail'),
    path('<int:pk>', views.recipe_detail, name='recipedetail'),

]
