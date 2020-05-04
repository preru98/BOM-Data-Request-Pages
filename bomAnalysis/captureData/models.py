from django.db import models
from django.utils import timezone

# Create your models here.

class data(models.Model):

    pub_time=models.DateTimeField(auto_now=True)

    pressure_avg=models.FloatField()
    pressure_min=models.FloatField()
    pressure_max=models.FloatField()

    wind_speed_avg=models.FloatField()
    wind_speed_min=models.FloatField()
    wind_speed_max=models.FloatField()

    def __str__(self):
        record='Time -> {}  |  Pressure -> Avg. : {} | Min. : {} | Max. : {}  Wind Speed -> Avg. : {} | Min. : {} | Max. : {} '.format(str(self.pub_time),str(self.pressure_avg), str(self.pressure_min), str(self.pressure_max), str(self.wind_speed_avg), str(self.wind_speed_min), str(self.wind_speed_max))
        return record

#constructor
#=data(pressure_avg=,pressure_min=,pressure_max=,wind_speed_avg=,wind_speed_min=,wind_speed_max


