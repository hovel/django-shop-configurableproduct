# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TypeImage'
        db.create_table('configurableproduct_typeimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductType'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductImageField'])),
        ))
        db.send_create_signal('configurableproduct', ['TypeImage'])

        # Adding model 'TypeBoolean'
        db.create_table('configurableproduct_typeboolean', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductType'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductBooleanField'])),
        ))
        db.send_create_signal('configurableproduct', ['TypeBoolean'])

        # Adding model 'TypeFloat'
        db.create_table('configurableproduct_typefloat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductType'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductFloatField'])),
        ))
        db.send_create_signal('configurableproduct', ['TypeFloat'])

        # Adding model 'TypeChar'
        db.create_table('configurableproduct_typechar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductType'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductCharField'])),
        ))
        db.send_create_signal('configurableproduct', ['TypeChar'])


    def backwards(self, orm):
        
        # Deleting model 'TypeImage'
        db.delete_table('configurableproduct_typeimage')

        # Deleting model 'TypeBoolean'
        db.delete_table('configurableproduct_typeboolean')

        # Deleting model 'TypeFloat'
        db.delete_table('configurableproduct_typefloat')

        # Deleting model 'TypeChar'
        db.delete_table('configurableproduct_typechar')


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
            'boolean_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductBooleanField']", 'null': 'True', 'blank': 'True'}),
            'char_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductCharField']", 'null': 'True', 'blank': 'True'}),
            'float_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductFloatField']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductImageField']", 'null': 'True', 'blank': 'True'}),
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
