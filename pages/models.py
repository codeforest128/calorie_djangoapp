from django.db import models


class CalorieData(models.Model):
    id = models.AutoField(primary_key=True)
    calorie = models.IntegerField(default=0)
    pub_date = models.DateField()
# Create your models here.

