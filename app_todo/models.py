from django.db import models
from django.utils import timezone


class Todo(models.Model):
    content = models.CharField(max_length=1000)
    completed = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} : {} : Completed:{} : {}".format(self.id, self.content, self.completed, self.created_date)
