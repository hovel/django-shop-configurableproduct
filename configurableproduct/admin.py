#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from django.contrib import admin
from models import CProduct
from models import ProductType
from models import ProductCharField, ProductChar
from models import ProductBooleanField, ProductBoolean
from models import ProductFloatField, ProductFloat
from models import ProductImageField, ProductImage
from sorl.thumbnail.admin.current import AdminImageWidget
from sorl.thumbnail.fields import ImageField
from django.conf import settings


class ProductCharInline(admin.TabularInline):
    model = ProductChar
    extra = 0
    can_delete = False
    fieldsets = [
            ['', {'fields': ['field', 'value', 'order']}]
    ]


class ProductBooleanInline(ProductCharInline):
    model = ProductBoolean


class ProductFloatInline(ProductCharInline):
    model = ProductFloat


class ProductImageInline(ProductCharInline):
    model = ProductImage
    formfield_overrides = {
        ImageField: {'widget': AdminImageWidget}
    }


class ProductTypeAdmin(admin.ModelAdmin):
    fieldsets = (
    ('', {'fields': ['name', 'char_fields', 'float_fields', 'boolean_fields', 'image_fields']}),
    )
    inlines = [ProductCharInline, ProductBooleanInline, ProductFloatInline, ProductImageInline]
    list_per_page = 100
    list_display = ('name',)
    search_fields = ('name',)


class CProductAdmin(admin.ModelAdmin):
    fieldsets = (
    ('', {'fields': ['type', 'name', 'slug', 'active']}),
    )
    inlines = [ProductCharInline, ProductBooleanInline, ProductFloatInline, ProductImageInline]
    prepopulated_fields = {'slug': ['name']}

admin.site.register(ProductCharField)
admin.site.register(ProductBooleanField)
admin.site.register(ProductFloatField)
admin.site.register(ProductImageField)
admin.site.register(ProductType, ProductTypeAdmin)

if getattr(settings, 'ENABLE_CPRODUCT_ADMIN', False):
    admin.site.register(CProduct, CProductAdmin)