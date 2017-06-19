from django.db import models

# Create your models here.
class IntSetting(models.Model):
    key = models.CharField(max_length=255)
    value = models.IntegerField(default=0)
    date_modified = models.DateTimeField('date modified')
    
