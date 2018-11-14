from django.db import models

class Timecard(models.Model):
    duration = models.TextField()
    project_id = models.TextField()
    user_id = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title