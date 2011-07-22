# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProductBooleanField'
        db.create_table('configurableproduct_productbooleanfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('configurableproduct', ['ProductBooleanField'])

        # Adding model 'ProductBoolean'
        db.create_table('configurableproduct_productboolean', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.CProduct'])),
            ('value', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductBooleanField'])),
        ))
        db.send_create_signal('configurableproduct', ['ProductBoolean'])

        # Adding model 'ProductCharField'
        db.create_table('configurableproduct_productcharfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('configurableproduct', ['ProductCharField'])

        # Adding model 'ProductChar'
        db.create_table('configurableproduct_productchar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.CProduct'])),
            ('value', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductCharField'])),
        ))
        db.send_create_signal('configurableproduct', ['ProductChar'])

        # Adding model 'ProductFloatField'
        db.create_table('configurableproduct_productfloatfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('configurableproduct', ['ProductFloatField'])

        # Adding model 'ProductFloat'
        db.create_table('configurableproduct_productfloat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.CProduct'])),
            ('value', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductFloatField'])),
        ))
        db.send_create_signal('configurableproduct', ['ProductFloat'])

        # Adding model 'ProductImageField'
        db.create_table('configurableproduct_productimagefield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('configurableproduct', ['ProductImageField'])

        # Adding model 'ProductImage'
        db.create_table('configurableproduct_productimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.CProduct'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('value', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductImageField'])),
        ))
        db.send_create_signal('configurableproduct', ['ProductImage'])

        # Adding model 'ProductType'
        db.create_table('configurableproduct_producttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('configurableproduct', ['ProductType'])

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

        # Adding model 'CProduct'
        db.create_table('configurableproduct_cproduct', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['configurableproduct.ProductType'])),
        ))
        db.send_create_signal('configurableproduct', ['CProduct'])


    def backwards(self, orm):
        
        # Deleting model 'ProductBooleanField'
        db.delete_table('configurableproduct_productbooleanfield')

        # Deleting model 'ProductBoolean'
        db.delete_table('configurableproduct_productboolean')

        # Deleting model 'ProductCharField'
        db.delete_table('configurableproduct_productcharfield')

        # Deleting model 'ProductChar'
        db.delete_table('configurableproduct_productchar')

        # Deleting model 'ProductFloatField'
        db.delete_table('configurableproduct_productfloatfield')

        # Deleting model 'ProductFloat'
        db.delete_table('configurableproduct_productfloat')

        # Deleting model 'ProductImageField'
        db.delete_table('configurableproduct_productimagefield')

        # Deleting model 'ProductImage'
        db.delete_table('configurableproduct_productimage')

        # Deleting model 'ProductType'
        db.delete_table('configurableproduct_producttype')

        # Removing M2M table for field char_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_char_fields')

        # Removing M2M table for field float_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_float_fields')

        # Removing M2M table for field boolean_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_boolean_fields')

        # Removing M2M table for field image_fields on 'ProductType'
        db.delete_table('configurableproduct_producttype_image_fields')

        # Deleting model 'CProduct'
        db.delete_table('configurableproduct_cproduct')


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
