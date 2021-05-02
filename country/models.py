from django.db import models


class City(models.Model):
    ''' City model has attribute for city,state,country'''
    city=models.CharField(max_length=50,blank= False,default='')
    state=models.CharField(max_length=50,blank=False,default="")
    country=models.CharField(max_length=50,blank=False,default="")
    

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering=('city',)

class Image(models.Model):    
    image_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images' )
    


   
