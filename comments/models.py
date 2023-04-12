from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # name = models.CharField(max_length=100)
    # email = models.EmailField(blank=True)
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.recipe} by {self.user}"
