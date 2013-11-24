# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customers'
        db.create_table(u'customers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customerid', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'CUSTOMERID', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=96L, db_column=u'NAME', blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'CITY', blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'REGION', blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'TYPE', blank=True)),
            ('shippinglimit', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'SHIPPINGLIMIT', decimal_places=30, max_digits=67)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'ADDRESS', blank=True)),
        ))
        db.send_create_signal(u'oracle', ['Customers'])

        # Adding model 'Loginfo'
        db.create_table(u'loginfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skuid', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'SKUID', blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'DESCRIPTION', blank=True)),
            ('netweight', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'NETWEIGHT', decimal_places=3, max_digits=11)),
            ('bruttoweight', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'BRUTTOWEIGHT', decimal_places=3, max_digits=11)),
            ('unitsperparcel', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'UNITSPERPARCEL', decimal_places=0, max_digits=7)),
            ('unitsperpallet', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'UNITSPERPALLET', decimal_places=0, max_digits=7)),
            ('shelflifeperiod', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'SHELFLIFEPERIOD', decimal_places=0, max_digits=7)),
            ('mu', self.gf('django.db.models.fields.CharField')(max_length=8L, db_column=u'MU', blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'LOCATION', blank=True)),
        ))
        db.send_create_signal(u'oracle', ['Loginfo'])

        # Adding model 'Operations'
        db.create_table(u'operations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'DOCUMENT')),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'DIRECTION')),
            ('skuid', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'SKUID')),
            ('qty', self.gf('django.db.models.fields.DecimalField')(db_column=u'QTY', decimal_places=3, max_digits=12)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'LOCATION')),
            ('customerid', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'CUSTOMERID', blank=True)),
            ('operationid', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'ID', decimal_places=30, max_digits=67)),
        ))
        db.send_create_signal(u'oracle', ['Operations'])

        # Adding model 'Sku'
        db.create_table(u'sku', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skuid', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'SKUID')),
            ('skugroup', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'SKUGROUP', blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'DESCRIPTION', blank=True)),
            ('mu', self.gf('django.db.models.fields.CharField')(max_length=8L, db_column=u'MU', blank=True)),
            ('baseunits', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'BASEUNITS', decimal_places=0, max_digits=4)),
            ('unitsperparcel', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'UNITSPERPARCEL', decimal_places=0, max_digits=7)),
            ('unitsperpallet', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'UNITSPERPALLET', decimal_places=0, max_digits=7)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'MANUFACTURER', blank=True)),
            ('countryoforigin', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'COUNTRYOFORIGIN', blank=True)),
            ('traditionaltrade', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'TRADITIONALTRADE', decimal_places=0, max_digits=2)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'LOCATION', blank=True)),
            ('netweight', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'NETWEIGHT', decimal_places=3, max_digits=11)),
        ))
        db.send_create_signal(u'oracle', ['Sku'])

        # Adding model 'StockBalance'
        db.create_table(u'stock_balance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skuid', self.gf('django.db.models.fields.CharField')(max_length=20L, db_column=u'SKUID', blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'DESCRIPTION', blank=True)),
            ('qty', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column=u'QTY', decimal_places=3, max_digits=12)),
        ))
        db.send_create_signal(u'oracle', ['StockBalance'])


    def backwards(self, orm):
        # Deleting model 'Customers'
        db.delete_table(u'customers')

        # Deleting model 'Loginfo'
        db.delete_table(u'loginfo')

        # Deleting model 'Operations'
        db.delete_table(u'operations')

        # Deleting model 'Sku'
        db.delete_table(u'sku')

        # Deleting model 'StockBalance'
        db.delete_table(u'stock_balance')


    models = {
        u'oracle.customers': {
            'Meta': {'object_name': 'Customers', 'db_table': "u'customers'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'ADDRESS'", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'CITY'", 'blank': 'True'}),
            'customerid': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'CUSTOMERID'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '96L', 'db_column': "u'NAME'", 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'REGION'", 'blank': 'True'}),
            'shippinglimit': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'SHIPPINGLIMIT'", 'decimal_places': '30', 'max_digits': '67'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'TYPE'", 'blank': 'True'})
        },
        u'oracle.loginfo': {
            'Meta': {'object_name': 'Loginfo', 'db_table': "u'loginfo'"},
            'bruttoweight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'BRUTTOWEIGHT'", 'decimal_places': '3', 'max_digits': '11'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'DESCRIPTION'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'LOCATION'", 'blank': 'True'}),
            'mu': ('django.db.models.fields.CharField', [], {'max_length': '8L', 'db_column': "u'MU'", 'blank': 'True'}),
            'netweight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'NETWEIGHT'", 'decimal_places': '3', 'max_digits': '11'}),
            'shelflifeperiod': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'SHELFLIFEPERIOD'", 'decimal_places': '0', 'max_digits': '7'}),
            'skuid': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'SKUID'", 'blank': 'True'}),
            'unitsperpallet': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'UNITSPERPALLET'", 'decimal_places': '0', 'max_digits': '7'}),
            'unitsperparcel': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'UNITSPERPARCEL'", 'decimal_places': '0', 'max_digits': '7'})
        },
        u'oracle.operations': {
            'Meta': {'object_name': 'Operations', 'db_table': "u'operations'"},
            'customerid': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'CUSTOMERID'", 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'DIRECTION'"}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'DOCUMENT'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'LOCATION'"}),
            'operationid': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'ID'", 'decimal_places': '30', 'max_digits': '67'}),
            'qty': ('django.db.models.fields.DecimalField', [], {'db_column': "u'QTY'", 'decimal_places': '3', 'max_digits': '12'}),
            'skuid': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'SKUID'"})
        },
        u'oracle.sku': {
            'Meta': {'object_name': 'Sku', 'db_table': "u'sku'"},
            'baseunits': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'BASEUNITS'", 'decimal_places': '0', 'max_digits': '4'}),
            'countryoforigin': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'COUNTRYOFORIGIN'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'DESCRIPTION'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'LOCATION'", 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'MANUFACTURER'", 'blank': 'True'}),
            'mu': ('django.db.models.fields.CharField', [], {'max_length': '8L', 'db_column': "u'MU'", 'blank': 'True'}),
            'netweight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'NETWEIGHT'", 'decimal_places': '3', 'max_digits': '11'}),
            'skugroup': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'SKUGROUP'", 'blank': 'True'}),
            'skuid': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'SKUID'"}),
            'traditionaltrade': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'TRADITIONALTRADE'", 'decimal_places': '0', 'max_digits': '2'}),
            'unitsperpallet': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'UNITSPERPALLET'", 'decimal_places': '0', 'max_digits': '7'}),
            'unitsperparcel': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'UNITSPERPARCEL'", 'decimal_places': '0', 'max_digits': '7'})
        },
        u'oracle.stockbalance': {
            'Meta': {'object_name': 'StockBalance', 'db_table': "u'stock_balance'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'DESCRIPTION'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qty': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "u'QTY'", 'decimal_places': '3', 'max_digits': '12'}),
            'skuid': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'db_column': "u'SKUID'", 'blank': 'True'})
        }
    }

    complete_apps = ['oracle']