#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from abstract import *
from django.utils.translation import ugettext_lazy as _

class ProductBooleanField(ProductAbstractField):
    class Meta(object):
        verbose_name = _('Product field - boolean')
        verbose_name_plural = _('Product fields - boolean')
        app_label = 'configurableproduct'


class ProductBoolean(ProductAbstractFieldThrough):
    class Meta(ProductAbstractFieldThrough.Meta):
        verbose_name = _('Boolean field')
        verbose_name_plural = _('Boolean fields')
        app_label = 'configurableproduct'

    value = models.NullBooleanField(verbose_name=_('Value'), default=None, null=True, blank=True)
    field = models.ForeignKey(ProductBooleanField, verbose_name=_('Field'))


class TypeBoolean(TypeAbstractFieldTrhough):
    class Meta(TypeAbstractFieldTrhough.Meta):
        verbose_name = _('Boolean field')
        verbose_name_plural = _('Boolean fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey(ProductBooleanField, verbose_name=_('Field'))