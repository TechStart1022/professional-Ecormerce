from django.db import models

from userauths.models import User

class Vendor(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vendor', blank=True, null=True, default='vendor.jpg')
    name = models.CharField(max_length=100, help_text='shop name',null=True, blank=True)
    description = models.CharField(max_length=100, help_text='shop description', null=True, blank=True)
    mobile = models.CharField(max_length=100, help_text='Mobile number', null=True, blank=True)
    active = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True,max_length=500)

    class Meta:
        verbose_name_plural = 'vendors'


# Create your models here.
