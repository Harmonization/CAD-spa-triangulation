from django.db import models

# Create your models here.
class Triangulation(models.Model):
    # title = models.CharField(max_length=200)
    # body = models.TextField()
    h = models.FloatField(default=16)
    R = models.FloatField(default=7)
    N = models.IntegerField(default=23)
    # points = models.ExpressionList()

    def __str__(self):
        return f"h: {self.h}, R: {self.R}, N:{self.N}"