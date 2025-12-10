from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')

    def __str__(self):
        return self.title