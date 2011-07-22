#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from abstract import *
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError
from django.conf import settings
import uuid
import os

#noinspection PyUnusedLocal
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(getattr(settings, 'PRODUCT_IMAGE_UPLOAD_TO', 'products/'), filename)


class ProductImageField(ProductAbstractField):
    class Meta(object):
        verbose_name = _('Product field - image')
        verbose_name_plural = _('Product fields - image')
        app_label = 'configurableproduct'


class ProductImage(ProductAbstractFieldThrough):
    class Meta(ProductAbstractFieldThrough.Meta):
        verbose_name = _('Product image field')
        verbose_name_plural = _('Product image field')
        app_label = 'configurableproduct'

    description = models.CharField(max_length=200, verbose_name=_('Description'), blank=True, null=True)
    value = ImageField(verbose_name=_('File'), upload_to=get_file_path)
    field = models.ForeignKey(ProductImageField, verbose_name=_('Field'))

    def admin_thumbnail(self):
        try:
            return '<img src="%s">' % get_thumbnail(self.value, '100x100', crop='center').url
        except IOError:
            return 'IOError'
        except ThumbnailError, ex:
            return 'ThumbnailError, %s' % ex.message

    admin_thumbnail.short_description = _('Thumbnail')
    admin_thumbnail.allow_tags = True


class TypeImage(TypeAbstractFieldTrhough):
    class Meta(TypeAbstractFieldTrhough.Meta):
        verbose_name = _('Image field')
        verbose_name_plural = _('Image fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey(ProductImageField, verbose_name=_('Field'))