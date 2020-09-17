from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from rest_framework import serializers
from market.filters import ProductFilter



class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'get_small_image_url']


class ProductListView(GenericAPIView, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)