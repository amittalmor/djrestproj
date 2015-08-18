from django.db import models

class GeoAddress(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200,blank=True)
    street = models.CharField(max_length=200,blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        address = ''
        for field in ['street','city','country']:
            address = '%s %s' % (address, getattr(self,field,''))
        address = address.strip()
        return address
  
    