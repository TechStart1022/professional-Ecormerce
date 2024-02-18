from rest_framework import serializers
from store.models import User, Product,Category,Cart,CartOrderItem,CartOrder,Gallery,Size, Color,Specification,Notification, ProductFaq,Review,WishList,Coupon
from vendor.models import Vendor

class CategorySerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = "__all__"
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields = '__all__'
class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = "__all__"
class SizeSerializer(serializers.Serializer):
    class Meta:
        model=Size
        fields="__all__"
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True,validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['full_name','email','phone','password','password2']
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"Password","Not match password"})
#         return attrs
#     def create(self,validated_data):
#         user = User.objects.create(
#             full_name = validated_data['full_name'],
#             email = validated_data['email'],
#             phone = validated_data['phone']
#         )
#         email_user, mobile = user.email.split('@')
#         user.set_password(validated_data['password'])
#         user.save()
#         return user        
class ProductSerailizer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True)
    color = ColorSerializer(many=True)
    specification = SpecificationSerializer(many=True)
    size = SizeSerializer(many=True)
    class Meta:
        model = Product
        fields =['gallery']
        fields = [
            'id',
            'title',
            'image',
            'description',
            'category',
            'price',
            'old_price',
            'shipping_amount',
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
            'size',
            'pid',
            'slug',
            'date'
        ]
    def __init__(self, *args, **kwargs):
        super(ProductSerailizer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CartSerializer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
class CartOrderSerailizer(serializers.ModelSerializer):
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
class CartOrderItemSerailizer(serializers.ModelSerializer):
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
class ProductFaqSerailizer(serializers.ModelSerializer):
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
class VendorSerailizer(serializers.ModelSerializer):
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
class ReviewSerailizer(serializers.ModelSerializer):
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
class WishListSerailizer(serializers.ModelSerializer):
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
class CouponSerailizer(serializers.ModelSerializer):
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
class NotificationSerailizer(serializers.ModelSerializer):
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




