# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Orderfailute'
        db.delete_table('stock_info_orderfailute')

        # Adding model 'Orderfailure'
        db.create_table('stock_info_orderfailure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.Operation'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stock_info', ['Orderfailure'])


    def backwards(self, orm):
        # Adding model 'Orderfailute'
        db.create_table('stock_info_orderfailute', (
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.Operation'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stock_info', ['Orderfailute'])

        # Deleting model 'Orderfailure'
        db.delete_table('stock_info_orderfailure')


    models = {
        'stock_info.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '96', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'shipping_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'})
        },
        'stock_info.loginfo': {
            'Meta': {'object_name': 'LogInfo'},
            'brutto_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'measurement_unit': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'net_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'shelf_life_period': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_info.StockKeepingUnit']", 'null': 'True'}),
            'units_per_pallet': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'units_per_parcel': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'stock_info.operation': {
            'Meta': {'object_name': 'Operation'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_info.Customer']", 'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'operation_date': ('django.db.models.fields.DateField', [], {}),
            'operation_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_info.StockKeepingUnit']"})
        },
        'stock_info.orderfailure': {
            'Meta': {'object_name': 'Orderfailure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_info.Operation']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'stock_info.stockbalance': {
            'Meta': {'object_name': 'StockBalance'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3'}),
            'stock_keeping_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_info.StockKeepingUnit']", 'null': 'True'})
        },
        'stock_info.stockkeepingunit': {
            'Meta': {'object_name': 'StockKeepingUnit'},
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'net_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '3'}),
            'stock_keeping_unit_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'traditional_trade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'units_per_pallet': ('django.db.models.fields.IntegerField', [], {}),
            'units_per_parcel': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['stock_info']