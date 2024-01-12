from django.db import models
from user.models import User

# Create your models here.
class Room(models.Model):
    room_no = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    description = models.TextField()
    type = models.ForeignKey('RoomType',on_delete=models.SET_NULL,null=True)

class RoomType(models.Model):
    name = models.CharField(max_length=300)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=300)
    number = models.IntegerField()
    photo = models.ImageField(upload_to='employee_image')
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)