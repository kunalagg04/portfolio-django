from django.db import models

# Create your models here

class Job(models.Model):
    #image and summary are parts of job.
    #https://docs.djangoproject.com/en/2.0/ref/models/fields/
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


#migrations actully setup our database