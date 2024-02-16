from rest_framework import serializers
from store.models import User, Product,Category,Cart,CartOrderItem,CartOrder,Gallery,Size, Color,Specification,Notification, ProductFaq,Review,WishList,Coupon
from vendor.models import Vendor

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
    def __init__(self, *args, **kwargs):
        super(ProductSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CartSerailizer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CartSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CartOrderSerailizer(serializers.Serializer):
    class Meta:
        model = CartOrder
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CartOrderSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CartOrderItemSerailizer(serializers.Serializer):
    class Meta:
        model = CartOrderItem
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CartOrderItemSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class ProductFaqSerailizer(serializers.Serializer):
    class Meta:
        model = ProductFaq
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProductFaqSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class VendorSerailizer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(VendorSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class ReviewSerailizer(serializers.Serializer):
    class Meta:
        model = Review
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ReviewSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class WishListSerailizer(serializers.Serializer):
    class Meta:
        model = WishList
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(WishListSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CouponSerailizer(serializers.Serializer):
    class Meta:
        model = Coupon
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CouponSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class NotificationSerailizer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(NotificationSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3




