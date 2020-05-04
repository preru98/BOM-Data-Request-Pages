from django.db import models

# Create your models here.

class data(models.Model):

    pub_date=models.DateField(auto_now=True)
    pub_time=models.DateTimeField(auto_now=True)
    pressure_avg=models.FloatField()
    pressure_min=models.FloatField()
    pressure_max=models.FloatField()

    wind_speed_avg=models.FloatField()
    wind_speed_min=models.FloatField()
    wind_speed_max=models.FloatField()


