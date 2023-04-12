from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:pk>/comment/',
         views.add_comment, name="addcomment"),

]
