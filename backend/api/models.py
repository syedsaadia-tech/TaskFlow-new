from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    project_id = models.CharField(max_length=100)
    member_id = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.title