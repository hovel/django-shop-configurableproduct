#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from abstract import *
from django.utils.translation import ugettext_lazy as _

class ProductFloatField(ProductAbstractField):
    class Meta(object):
        verbose_name = _('Product field - float')
        verbose_name_plural = _('Product fields - float')
        app_label = 'configurableproduct'
        

class ProductFloat(ProductAbstractFieldThrough):
    class Meta(ProductAbstractFieldThrough.Meta):
        verbose_name = _('Float field')
        verbose_name_plural = _('Float fields')
        app_label = 'configurableproduct'

    value = models.FloatField(verbose_name=_('Value'), default=None, null=True, blank=True)
    field = models.ForeignKey(ProductFloatField, verbose_name=_('Field'))
    

class TypeFloat(TypeAbstractFieldTrhough):
    class Meta(TypeAbstractFieldTrhough.Meta):
        verbose_name = _('Float field')
        verbose_name_plural = _('Float fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey(ProductFloatField, verbose_name=_('Field'))