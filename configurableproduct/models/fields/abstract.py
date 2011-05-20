#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from django.db import models
from django.utils.translation import ugettext_lazy as _


# ---- Field models ---
class ProductAbstractField(models.Model):
    class Meta(object):
        abstract = True
        app_label = 'configurableproduct'

    name = models.CharField(max_length=200, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name

class ProductAbstractFieldThrough(models.Model):
    class Meta(object):
        abstract = True
        ordering = ['order']
        app_label = 'configurableproduct'

    product = models.ForeignKey('configurableproduct.CProduct')
    order = models.IntegerField(default=0, verbose_name=_('Ordering'))