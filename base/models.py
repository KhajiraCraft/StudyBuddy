from django.db import models

# Create your models here.
# models.Models inherits from the django models class
class Room(models.Model):
    # host =
    # topic = 
    name = models.CharField(max_length=200)
    # By default, null = False, which means you will always need a value. Setting it to true means it can be empty. Setting it to blank means it can be empty if being used in a form
    description = models.TextField(null=True, blank=True) 
    # participants =
    #the auto_now = True ensures that the time is set to the current time whenever an action is performed e.g a save. It gives a timestamp 
    updated = models.DateTimeField(auto_now = True)

    #auto_now_add will only take a snapshot once when the record is created
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    # user =
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)

    #auto_now_add will only take a snapshot once when the record is created
    created = models.DateTimeField(auto_now_add = True)
# This below is to return the first 50 characters. We do not want to cram the django admin panel
    def __str__(self):
        return self.body[0:50]