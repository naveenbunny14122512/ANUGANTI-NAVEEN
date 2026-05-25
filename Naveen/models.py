from django.db import models
# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=200)
    marks1=models.IntegerField()
    marks2=models.IntegerField()
    marks3=models.IntegerField()
    marks4=models.IntegerField()
    total=models.IntegerField()
    total_avg=models.FloatField()
    Grade=models.CharField(max_length=100)

# def __str__(self):

#     return f"{self.Name} {self.marks1} {self.marks2} {self.marks3} {self.marks4} {self.total} {self.total_avg} {self.Grade}"
    def __str__(self):

        return f"Name:{self.Name} Total:{self.total} Grade:{self.Grade}"