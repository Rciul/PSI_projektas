# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StockKeepingUnit.group'
        db.alter_column(u'stock_info_stockkeepingunit', 'group', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))
        # Adding field 'Orderfailure.date'
        db.add_column(u'stock_info_orderfailure', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime.now(), blank=True),
                      keep_default=False)

        # Adding field 'Orderfailure.amount'
        db.add_column(u'stock_info_orderfailure', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=3),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'StockKeepingUnit.group'
        raise RuntimeError("Cannot reverse this migration. 'StockKeepingUnit.group' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'StockKeepingUnit.group'
        db.alter_column(u'stock_info_stockkeepingunit', 'group', self.gf('django.db.models.fields.CharField')(max_length=32))
        # Deleting field 'Orderfailure.date'
        db.delete_column(u'stock_info_orderfailure', 'date')

        # Deleting field 'Orderfailure.amount'
        db.delete_column(u'stock_info_orderfailure', 'amount')


    models = {
        u'stock_info.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '96', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'shipping_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'})
        },
        u'stock_info.loginfo': {
            'Meta': {'object_name': 'LogInfo'},
            'brutto_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'measurement_unit': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'net_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'shelf_life_period': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock_info.StockKeepingUnit']", 'null': 'True'}),
            'units_per_pallet': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'units_per_parcel': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'stock_info.operation': {
            'Meta': {'object_name': 'Operation'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock_info.Customer']", 'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'operation_date': ('django.db.models.fields.DateField', [], {}),
            'operation_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock_info.StockKeepingUnit']"})
        },
        u'stock_info.orderfailure': {
            'Meta': {'object_name': 'Orderfailure'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock_info.Operation']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'stock_info.stockbalance': {
            'Meta': {'object_name': 'StockBalance'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock_info.StockKeepingUnit']", 'null': 'True'})
        },
        u'stock_info.stockkeepingunit': {
            'Meta': {'object_name': 'StockKeepingUnit'},
            'base_units': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'measurement_unit': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'net_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'stock_keeping_unit_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'traditional_trade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'units_per_pallet': ('django.db.models.fields.IntegerField', [], {}),
            'units_per_parcel': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['stock_info']