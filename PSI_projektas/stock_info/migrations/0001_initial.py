# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('stock_info_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=96, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('shipping_limit', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
        ))
        db.send_create_signal('stock_info', ['Customer'])

        # Adding model 'StockBalance'
        db.create_table('stock_info_stockbalance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_keeping_unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.StockKeepingUnit'], null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal('stock_info', ['StockBalance'])

        # Adding model 'StockKeepingUnit'
        db.create_table('stock_info_stockkeepingunit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_keeping_unit_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('units_per_parcel', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('units_per_pallet', self.gf('django.db.models.fields.IntegerField')()),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('country_of_origin', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('traditional_trade', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('net_weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=3)),
        ))
        db.send_create_signal('stock_info', ['StockKeepingUnit'])

        # Adding model 'LogInfo'
        db.create_table('stock_info_loginfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_keeping_unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.StockKeepingUnit'], null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('net_weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=3)),
            ('brutto_weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=3)),
            ('units_per_parcel', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('units_per_pallet', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('shelf_life_period', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('measurement_unit', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('stock_info', ['LogInfo'])

        # Adding model 'Operation'
        db.create_table('stock_info_operation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('stock_keeping_unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.StockKeepingUnit'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('operation_date', self.gf('django.db.models.fields.DateField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.Customer'], null=True)),
            ('operation_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('stock_info', ['Operation'])

        # Adding model 'Orderfailute'
        db.create_table('stock_info_orderfailute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock_info.Operation'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stock_info', ['Orderfailute'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('stock_info_customer')

        # Deleting model 'StockBalance'
        db.delete_table('stock_info_stockbalance')

        # Deleting model 'StockKeepingUnit'
        db.delete_table('stock_info_stockkeepingunit')

        # Deleting model 'LogInfo'
        db.delete_table('stock_info_loginfo')

        # Deleting model 'Operation'
        db.delete_table('stock_info_operation')

        # Deleting model 'Orderfailute'
        db.delete_table('stock_info_orderfailute')


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
        'stock_info.orderfailute': {
            'Meta': {'object_name': 'Orderfailute'},
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
