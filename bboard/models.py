from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    content = models.TextField(null=True, blank=True, verbose_name = 'Description')
    price = models.FloatField(null=True, blank=True, verbose_name = 'Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Ads'
        verbose_name = 'Ad'
        ordering = ['-published']

    
 
