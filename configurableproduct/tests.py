from django.test import TestCase
from models import CProduct
from models import ProductType
from models import ProductCharField, ProductChar

#TODO Tests for other fields

class SimpleTest(TestCase):

    def setUp(self):
        self.pcf = ProductCharField(name='test char field')
        self.pcf.save()
        self.product_type = ProductType(name='test type')
        self.product_type.save()
        self.product_type.char_fields.add(self.pcf)

    def test_product_type(self):
        '''
        Test for product type fields creation during product save
        '''
        product = CProduct(type=self.product_type)
        product.save()
        self.assertEqual(product.productchar_set.all()[0].field, self.pcf)



