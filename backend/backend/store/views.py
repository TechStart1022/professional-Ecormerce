from django.shortcuts import render
from store.models import Product,Category,Cart,Tax
from userauths.models import User
from store.serializers import ProductSerailizer, CategorySerailizer, CartSerializer
from rest_framework import generics,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer
    permission_classes = [AllowAny]
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    permission_classes = [AllowAny]
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerailizer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs['slug']
        print(slug,'slug')
        return Product.objects.get(slug=slug)
    
class CartAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        payload = request.data

        product_id = payload['product_id']
        user_id = payload['user_id']
        qty = payload['qty']
        price =payload['price']
        shipping_amount=payload['shipping_amout']
        country=payload['country']
        size=payload['size']
        color=payload['color']
        cart_id=payload['cart_id']

        product=Product.objects.get(id=product_id)
        if user_id != 'underfined':
            user = User.objects.get(id=user_id)
        else:
            user = None
        tax = Tax.objects.filter(country=country).first()
        if country:
            tax_rate =tax.rate / 100
        else:
            tax_rate = 0
        
        cart = Cart.objects.filter(cart_id=cart_id,product_id=product_id).first()

        if cart:
            cart.product = product
            cart.user = user
            cart.qty = qty
            cart.sub_total = Decimal(price) * Decimal(qty)
            cart.shipping_amount = Decimal(shipping_amount) * Decimal(qty)
            cart.tax_fee = int(qty) * Decimal(tax_rate) 
            cart.color = color
            cart.size = size
            cart.country = country
            cart.cart_id = cart_id

            service_fee_percentage = 10 / 100
            cart.service_fee = service_fee_percentage * cart.sub_total

            cart.total = cart.sub_total + cart.shipping_amount + cart.tax_fee + cart.service_fee
            cart.save()
            
            return Response({'message':"Cart Updated Successfully"},status=status.HTTP_200_OK)
        else:
            cart = Cart()
            cart.product = product
            cart.user = user
            cart.qty = qty
            cart.sub_total = Decimal(price) * Decimal(qty)
            cart.shipping_amount = Decimal(shipping_amount) * Decimal(qty)
            cart.tax_fee = int(qty) * Decimal(tax_rate) 
            cart.color = color
            cart.size = size
            cart.country = country
            cart.cart_id = cart_id

            service_fee_percentage = 10 / 100
            cart.service_fee = service_fee_percentage * cart.sub_total

            cart.total = cart.sub_total + cart.shipping_amount + cart.tax_fee + cart.service_fee
            cart.save()

            return Response({'message':"Cart Created Successfully"},status=status.HTTP_201_CREATED)
                  


    

# Create your views here.
