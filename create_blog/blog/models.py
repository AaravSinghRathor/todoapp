from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_description = models.TextField()
    task_created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={"pk": self.pk})
