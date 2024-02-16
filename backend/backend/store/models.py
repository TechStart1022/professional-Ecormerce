from django.db import models
from django.utils.text import slugify
from userauths.models import User, Profile
from vendor.models import Vendor
from shortuuid.django_fields import ShortUUIDField
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category',default='category.jpg', blank=True, null=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Category'
        ordering = ['title']
class Product(models.Model):
    STATUS = (
        ("draft", "Draft"),
        ("disabled", "Disabled"),
        ("in_review", "In-Review"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product',default='product.jpg', blank=True, null=True)  
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    old_price = models.DecimalField(decimal_places=2, max_digits=12,default = 0.00)
    shipping_amount = models.DecimalField(decimal_places=2,max_digits=12,default=0.00)

    stock_qty = models.PositiveIntegerField(default=1)
    instock=models.BooleanField(default=True)

    status=models.CharField(max_length=255,choices=STATUS,default="published")

    featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    pid = ShortUUIDField(unique=True,length=10,alphabet="abcdefg12345")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        if self.slug=='' or self.slug==None:
            self.slug=slugify(self.name)
        super(Product,self).save(*args, **kwargs)
    def __str__(self):
        return self.title


        


# Create your models here.
