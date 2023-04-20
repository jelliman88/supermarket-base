from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    json_data = models.JSONField(default=list)
    current_order = models.BooleanField(default=True)
    completed = models.CharField(max_length=10, default='pending')
    urgent = models.BooleanField(default=False)



