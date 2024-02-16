from rest_framework import serializers
from .models import User, Product,Category,Cart,CartOrderItem,CartOrder,Gallery,Size, Color,Specification


class CategorySerailizer(serializers.Serializer):
    
    class Meta:
        model = Category
        feilds = "__all__"
class ProductSerailizer(serializers.Serializer):
    
    class Meta:
        model = Product
        feilds = "__all__"
class ColorSerailizer(serializers.Serializer):
    
    class Meta:
        model = Color
        feilds = "__all__"
class GallerySerializer(serializers.Serializer):
    class Meta:
        model=Gallery
        feilds = '__all__'
class SpecificationSerializer(serializers.Serializer):
    class Meta:
        model = Specification
        feilds = "__all__"
class SizeSerializer(serializers.Serializer):
    class Meta:
        model=Size
        feilds="__all__"
class ProductSerailizer(serializers.Serializer):
    gallery = GallerySerializer(many=True,read_only=True)
    color = ColorSerailizer(many=True,read_only=True)
    specification = SpecificationSerializer(many=True,read_only=True)
    size = SizeSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        feilds = [
            'id',
            'description',
            'category',
            'price',
            'old_price',
            'shipping amount',
            'stock_qty',
            'in_stock',
            'status',
            'featured',
            'views',
            'rating',
            'vendor',
            'gallery',
            'color',
            'specification',
            'size'
            'pid',
            'slug',
            'date'
        ],






