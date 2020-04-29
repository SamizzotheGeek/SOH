from django.db import models

# Create your models here.
class events(models.Model):
    event_name =  models.CharField(max_length=200) 
    event_date = models.DateTimeField('Event Date: ')
    
    def __str__(self):
        return self.event_name

