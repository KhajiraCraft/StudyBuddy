from django.db import models

# Create your models here.
# models.Models inherits from the django models class
class Room(models.Model):
    # host =
    # topic = 
    name = models.CharField(max_lenth=200)
    # By default, null = False, which means you will always need a value. Setting it to true means it can be empty. Setting it to blank means it can be empty if being used in a form
    description = models.TextField(null=True, blank=True) 
    # participants =
    #the auto_now = True ensures that the time is set to the current time whenever an action is performed e.g a save. It gives a timestamp 
    updated = models.DateTimeField(auto_now = True)

    #auto_now_add will only take a snapshot once when the record is created
    created = models.DateTimeField(auto_now_add = True)