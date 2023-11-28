from django.db import models
from accounts.models import UserAccount  # この行を追加


class Task(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)  # この行を追加
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
