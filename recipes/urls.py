from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-recipe', views.create_recipe, name="create-recipe"),

    # path('recipes/<slug:slug>', views.recipe_detail, name='recipe_detail'),

]
