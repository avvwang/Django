from django.db import models

# Create your models here.


class movie(models.Model):
    title=models.CharField(max_length=100)
    like=models.IntegerField()
    recommend=models.IntegerField()
    comment=models.IntegerField()
