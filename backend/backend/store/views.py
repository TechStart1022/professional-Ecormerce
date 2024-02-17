from django.shortcuts import render
from store.models import Product,Category
from store.serializers import ProductSerailizer, CategorySerailizer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

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
    

# Create your views here.
