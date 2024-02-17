from django.db import models
from django.utils.text import slugify
from userauths.models import User, Profile
from vendor.models import Vendor
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField
from django.dispatch import receiver
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
    in_stock=models.BooleanField(default=True)

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
    def product_rating(self):
        product_rating = Review.objects.filter(product=self).aggregate(avg_rating=models.Avg("rating"))
        return product_rating['avg_rating']
    def gallery(self):
        return Gallery.objects.filter(product=self)
    def size(self):
        return Size.objects.filter(product=self)
    def specification(self):
        return Specification.objects.filter(product=self)
    def rating_count(self):
        return Review.objects.filter(product=self)
    def color(self):
        return Color.objects.filter(product=self)
    def save(self,*args, **kwargs):
        self.rating= self.product_rating()
        super(Product,self).save(*args,**kwargs)


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Gallery',default='gallery.jpg')
    active =models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add = True)
    pid = ShortUUIDField(unique=True, length=10, alphabet="abcdefg12345")

    def __str__(self):
        return self.product.title
    class Meta:
        verbose_name_plural = "Product images"
class Specification(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    color_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=0)
    price=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    sub_total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    shipping_amount=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    service_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    tax_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    country=models.CharField(max_length=100)
    size=models.CharField(max_length=100, blank=True,null=True)
    color=models.CharField(max_length=100, blank=True,null=True)
    cart_id=models.CharField(max_length=100, blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cart_id} - {self.product.title}"

class CartOrder(models.Model):
    PAYMENT_STATUS = (
        ("paid", "Paid"),
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("published", "Published"),
    )   
    ORDER_STATUS = (
        ("pending", "Pending"),
        ("Fulfilled", "Fulfilled"),
        ("cancelled", "Cancelled"),
    )   
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True)
    buyer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    sub_total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    service_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    tax_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)

    payment_status=models.CharField(choices=PAYMENT_STATUS,max_length=100,default="pending")
    order_status=models.CharField(choices=ORDER_STATUS,max_length=100, default='pending')

    initial_total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    saved=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    full_name=models.CharField(max_length=100, blank=True,null=True)
    email=models.CharField(max_length=100, blank=True,null=True)
    mobile=models.CharField(max_length=100, blank=True,null=True)
    address=models.CharField(max_length=100, blank=True,null=True)
    city=models.CharField(max_length=100, blank=True,null=True)
    state=models.CharField(max_length=100, blank=True,null=True)
    country=models.CharField(max_length=100, blank=True,null=True)

    oid = ShortUUIDField(unique=True, length=10,max_length=20,alphabet="abcdefghijk")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.oid
    
class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)

    qty=models.PositiveIntegerField(default=0)
    price=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    sub_total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    shipping_amount=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    service_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    tax_fee=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    country=models.CharField(max_length=100)

    size=models.CharField(max_length=100,blank=True)
    color=models.CharField(max_length=100,blank=True)


    initial_total=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    saved=models.DecimalField(decimal_places=2,max_digits=12,default=0.00)
    oid = ShortUUIDField(unique=True, length=10,max_length=20,alphabet="abcdefghijk")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.oid
# Create your models here.
class Coupon(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    user_by = models.ManyToManyField(User, blank=True)
    code = models.CharField(max_length=100)
    discount = models.IntegerField(default=1)
    active = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code
class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order = models.ForeignKey(CartOrder,on_delete=models.SET_NULL,null=True,blank=True)
    order_item = models.ForeignKey(CartOrderItem, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.order:
            return self.order.oid
        else:
            return f"notification - {self.pk}"
class WishList(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
class ProductFaq(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    email=models.EmailField(null=True,blank=True)
    question=models.CharField(max_length=100)
    answer=models.TextField(null=True,blank=True)
    active=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Product FAQs"

class Review(models.Model):
    RATING= (
        (1, "1 star"),
        (2, "2 star"),
        (3, "3 star"),
        (4, "4 star"),
        (5, "5 star"),
    )   
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(default=None,choices=RATING)
    reply = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Product Reviews & Rating"

    def profile(self):
        return Profile.objects.get(user=self.user)
    
@receiver(post_save,sender=Review)
def update_product_rating(sender,instance,**kwargs):
    if instance.product:
        instance.product.save()





