from turtle import position
from django.db import models


class Position(models.Model):
    position=models.CharField(max_length=50)



class Employee(models.Model):

    Full_Name = models.CharField( max_length=50)
    emp_code = models.CharField( max_length=3)
    mobile = models.CharField( max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    



    def __str__(self):
        return self.Full_Name



# Create your models here.
