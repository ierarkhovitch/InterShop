from django.contrib import admin
from market.models import Provider, Consumer, Category, Product, Order, OrderProduct, Store, SubCategory


class ProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Provider, ProviderAdmin)


class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer, ConsumerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']
admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_small_image']
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderProduct, OrderProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)
