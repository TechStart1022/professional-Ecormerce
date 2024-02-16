from django.contrib import admin
from store.models import Category, Product,Size, Color,Gallery,Specification



class GalleryInline(admin.TabularInline):
    model=Gallery

class SizeInline(admin.TabularInline):
    model=Size
class SpecificationInline(admin.TabularInline):
    model=Specification
class ColorInline(admin.TabularInline):
    model=Color
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','category','shipping_amount','stock_qty','in_stock','vendor','featured']
    list_editable=['featured']
    list_filter=['date']
    search_fields=['title']
    inlines=[GalleryInline,SpecificationInline,SizeInline,ColorInline]
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Gallery)
# Register your models here.
