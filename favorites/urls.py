from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites, name="favorites"),
    # path('recipes/<slug:slug>', views.recipe_detail, name='recipe_detail'),

]
