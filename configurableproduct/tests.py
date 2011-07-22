from django.test import TestCase
from models import CProduct
from models import ProductType
from models import ProductCharField, ProductChar
from models import TypeChar

#TODO Tests for other fields

class SimpleTest(TestCase):

    def setUp(self):
        self.pcf = ProductCharField(name='test char field')
        self.pcf.save()
        self.product_type = ProductType(name='test type')
        self.product_type.save()
        TypeChar.objects.create(field=self.pcf, type=self.product_type, order=2)

    def test_product_type(self):
        """
        Test for product type fields creation during product save
        """
        product = CProduct(type=self.product_type)
        product.save()
        self.assertEqual(product.productchar_set.all()[0].field, self.pcf)
        self.assertEqual(product.productchar_set.all()[0].order, 2)



