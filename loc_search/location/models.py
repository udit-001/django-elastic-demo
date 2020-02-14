from django.db import models

class City(models.Model):
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    place_name = models.CharField(max_length=255, blank=True, null=True)
    admin_name1 = models.CharField(max_length=255, blank=True, null=True)
    admin_code1 = models.CharField(max_length=255, blank=True, null=True)
    admin_name2 = models.CharField(max_length=255, blank=True, null=True)
    admin_code2 = models.CharField(max_length=255, blank=True, null=True)
    admin_name3 = models.CharField(max_length=255, blank=True, null=True)
    admin_code3 = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(max_length=255, blank=True, null=True)
    longitude = models.FloatField(max_length=255, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return self.postal_code
