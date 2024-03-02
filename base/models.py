from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Admin(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class FaceImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self): 
	    return self.name

class Status(models.Model):
    uid = models.CharField(max_length=1000)
    emotion = models.CharField(max_length=200)
    
    def __str__(self): 
	    return self.uid
 
class Student_Emotion(models.Model):
    uid = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    curious = models.IntegerField(default=0)
    confusion = models.IntegerField(default=0)
    boredom = models.IntegerField(default=0)
    hopefullness = models.IntegerField(default=0)
    
    def __str__(self):
        return self.uid
    
class Summary(models.Model):
    name = models.CharField(max_length=100)
    curious = models.CharField(max_length=5)
    confusion = models.CharField(max_length=5)
    boredom = models.CharField(max_length=5)
    hopefullness = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name
 