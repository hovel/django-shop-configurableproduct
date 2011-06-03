====================================
Configurable product for Django-shop
====================================

This plugin allow you to:

* Define product types in django admin interface with custom set of fields
* Add custom fields to products

Supported field types
=====================

* Float field
* Char field
* Image field (with preview in admin via sorl.thumbnail)
* Boolean field (NullBooleanField)

How to use it
=============

* Install from bitbucket or pypi
* If you want to define static fields for all product types (i.e. size, ...):

 * Create a subclass of configurableproduct.models.CProduct
 * Write admin class based on configurableproduct.admin.CProductAdmin

* If you want to use CProduct model directly, set `ENABLE_CPRODUCT_ADMIN` to `True` in your settings file.
* You can access custom fields via `productfloat_set`, `productchar_set`,... as::

   product_object.productchar_set.all()[0].value

* You can access ordered list of custom fields via `product_object.field_list` property

