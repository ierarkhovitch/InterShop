from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
from image_cropping.fields import ImageRatioField, ImageCropField
from prj.settings import BASE_URL


class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'


class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    geo_location = models.CharField(max_length=250, default='')
    address = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'


class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = ImageCropField(upload_to='product', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    cropping = ImageRatioField('image', '100x100')

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'

    @property
    def get_small_image(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_url)

    @property
    def get_small_image_url(self):
        return BASE_URL + get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.cropping,
            'crop': 'smart',
        }).url

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Store(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class Order(models.Model):
    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='new', choices=STATUS)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
