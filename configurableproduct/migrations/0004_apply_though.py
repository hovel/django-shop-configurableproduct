# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field char_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_char_fields')

        # Removing M2M table for field float_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_float_fields')

        # Removing M2M table for field boolean_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_boolean_fields')

        # Removing M2M table for field image_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_image_fields')


    def backwards(self, orm):
        
        # Adding M2M table for field char_fields on 'ProductType'
        db.create_table('configurableproduct_producttype_char_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('producttype', models.ForeignKey(orm['configurableproduct.producttype'], null=False)),
            ('productcharfield', models.ForeignKey(orm['configurableproduct.productcharfield'], null=False))
        ))
        db.create_unique('configurableproduct_producttype_char_fields', ['producttype_id', 'productcharfield_id'])

        # Adding M2M table for field float_fields on 'ProductType'
        db.create_table('configurableproduct_producttype_float_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('producttype', models.ForeignKey(orm['configurableproduct.producttype'], null=False)),
            ('productfloatfield', models.ForeignKey(orm['configurableproduct.productfloatfield'], null=False))
        ))
        db.create_unique('configurableproduct_producttype_float_fields', ['producttype_id', 'productfloatfield_id'])

        # Adding M2M table for field boolean_fields on 'ProductType'
        db.create_table('configurableproduct_producttype_boolean_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('producttype', models.ForeignKey(orm['configurableproduct.producttype'], null=False)),
            ('productbooleanfield', models.ForeignKey(orm['configurableproduct.productbooleanfield'], null=False))
        ))
        db.create_unique('configurableproduct_producttype_boolean_fields', ['producttype_id', 'productbooleanfield_id'])

        # Adding M2M table for field image_fields on 'ProductType'
        db.create_table('configurableproduct_producttype_image_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('producttype', models.ForeignKey(orm['configurableproduct.producttype'], null=False)),
            ('productimagefield', models.ForeignKey(orm['configurableproduct.productimagefield'], null=False))
        ))
        db.create_unique('configurableproduct_producttype_image_fields', ['producttype_id', 'productimagefield_id'])


    models = {
        'configurableproduct.cproduct': {
            'Meta': {'object_name': 'CProduct', '_ormbases': ['shop.Product']},
            'boolean_fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['configurableproduct.ProductBooleanField']", 'through': "orm['configurableproduct.ProductBoolean']", 'symmetrical': 'False'}),
            'char_fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['configurableproduct.ProductCharField']", 'through': "orm['configurableproduct.ProductChar']", 'symmetrical': 'False'}),
            'float_fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['configurableproduct.ProductFloatField']", 'through': "orm['configurableproduct.ProductFloat']", 'symmetrical': 'False'}),
            'image_fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['configurableproduct.ProductImageField']", 'through': "orm['configurableproduct.ProductImage']", 'symmetrical': 'False'}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.productboolean': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductBoolean'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductBooleanField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.CProduct']"}),
            'value': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'configurableproduct.productbooleanfield': {
            'Meta': {'object_name': 'ProductBooleanField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productchar': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductChar'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductCharField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.CProduct']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'configurableproduct.productcharfield': {
            'Meta': {'object_name': 'ProductCharField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productfloat': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductFloat'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductFloatField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.CProduct']"}),
            'value': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'configurableproduct.productfloatfield': {
            'Meta': {'object_name': 'ProductFloatField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductImage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductImageField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.CProduct']"}),
            'value': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        },
        'configurableproduct.productimagefield': {
            'Meta': {'object_name': 'ProductImageField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.producttype': {
            'Meta': {'object_name': 'ProductType'},
            'boolean_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductBooleanField']", 'null': 'True', 'through': "orm['configurableproduct.TypeBoolean']", 'blank': 'True'}),
            'char_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductCharField']", 'null': 'True', 'through': "orm['configurableproduct.TypeChar']", 'blank': 'True'}),
            'float_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductFloatField']", 'null': 'True', 'through': "orm['configurableproduct.TypeFloat']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductImageField']", 'null': 'True', 'through': "orm['configurableproduct.TypeImage']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'configurableproduct.typeboolean': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeBoolean'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductBooleanField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typechar': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeChar'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductCharField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typefloat': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeFloat'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductFloatField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typeimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeImage'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductImageField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['configurableproduct']
