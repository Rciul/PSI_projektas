# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from decimal import Decimal

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        print 'Importing customers'
        h = open('export.dsv')
        Customer = orm.Customer
        content = h.read()
        h.close()
        lines = content.split('\n')
        customers = []
        for l in lines[1:-1]:
            items = l.split(';')
            if len(items) < 4:
                continue
            customer = Customer()
            customer.customer_id = items[0].strip('"')
            customer.name = items[1].strip('"')
            customer.city = items[2].strip('"')
            customer.region = items[3].strip('"')
            customer.type = items[4].strip('"')
            try:
                customer.shipping_limit = int(items[5].strip(''))
            except:
                customer.shipping_limit = 0
            try:
                customer.address = items[6].strip('"')
            except:
                pass
            customers.append(customer)
        Customer.objects.bulk_create(customers)
        print 'Importing sku'
        h = open('exportsku.dsv')
        SKU = orm.StockKeepingUnit
        content = h.read()
        h.close()
        lines = content.split('\n')
        skus = []
        for l in lines[1:]:
            items = l.split(';')
            if len(items) < 4:
                continue
            sku = SKU()
            sku.stock_keeping_unit_id = items[0].strip('"')
            sku.group = items[1].strip('"')
            sku.description = items[2].strip('"')
            sku.measurement_unit = items[3].strip('"')
            sku.base_units = Decimal(items[4])
            try:
                sku.units_per_parcel = int(items[5])
            except:
                sku.units_per_parcel = 0
            try:
                sku.units_per_pallet = int(items[6])
            except:
                sku.units_per_pallet = 0
            sku.manufacturer = items[7].strip('"')
            sku.country_of_origin = items[8].strip('"')
            sku.traditional_trade = items[9] <> '0'
            sku.location = items[10].strip('"')
            try:
                sku.net_weight = Decimal(items[11])
            except:
                pass
            skus.append(sku)
        SKU.objects.bulk_create(skus)
        print 'Importing stock balance'
        h = open('exportsb.dsv')
        StockBalance = orm.StockBalance
        content = h.read()
        h.close()
        lines = content.split('\n')
        sbs = []
        for l in lines[1:-1]:
            if len(items) < 2:
                continue
            items = l.split(';')
            sb = StockBalance()
            if items[0].strip('"'):
                sku = SKU.objects.filter(stock_keeping_unit_id=items[0].strip('"'))
                if sku.count() > 0:
                    sku = sku[0]
                    sb.stock_keeping_unit = sku
            sb.description = items[1].strip('"')
            try:
                sb.quantity = Decimal(items[2])
            except:
                pass
            sbs.append(sb)
        StockBalance.objects.bulk_create(sbs)
        print 'Importing log'
        h = open('exportli.dsv')
        LogInfo = orm.LogInfo
        content = h.read()
        h.close()
        lines = content.split('\n')
        lis = []
        for l in lines[1:-1]:
            try:
                items = l.split(';')
                li = LogInfo()
            
                if items[0].strip('"'):
                    sku = SKU.objects.filter(stock_keeping_unit_id=items[0].strip('"'))
                    if sku.count() > 0:
                        sku = sku[0]
                        li.stock_keeping_unit = sku
                li.description = items[1][1:-1]
                try:
                    li.net_weight = Decimal(items[2])
                except:
                    pass
                try:
                    li.brutto_weight = Decimal(items[3])
                except:
                    pass
                try:
                    li.units_per_parcel = int(items[4])
                except:
                    pass
                try:
                    li.units_per_pallet = int(items[5])
                except:
                    pass
                try:
                    li.shelf_life_period = int(items[6])
                except:
                    pass
                try:
                    li.measurement_unit = items[7].strip('"')
                    li.location = items[8].strip('"')
                except:
                    pass
                li.save()
            except:
                pass
        LogInfo.objects.bulk_create(lis)
        print 'Importing opers'
        h = open('exporto.dsv')
        Oper = orm.Operation
        content = h.read()
        h.close()
        lines = content.split('\n')
        ops = []
        for l in lines[1:-1]:
            items = l.split(';')
            if len(items) < 2:
                continue
            oper = Oper()
            oper.document = items[0].strip('"')
            oper.direction = items[1].strip('"')
            if items[2].strip('"'):
                sku = SKU.objects.filter(stock_keeping_unit_id=items[2].strip('"'))
                if sku.count() > 0:
                    sku = sku[0]
                    oper.stock_keeping_unit = sku
            try:
                oper.quantity = Decimal(items[3])
            except:
                pass
            oper.location = items[4].strip('"')
            try:
                oper.date = datetime.datetime.strptime(items[5],'%m-%b-%y')
            except:
                pass
            
            if len(items) > 6 and items[6].strip('"'):
                customers = Customer.objects.filter(customer_id=items[6].strip('"'))
                if customers.count() > 0:
                    cust = customers[0]
                    oper.customer = cust
            try:
                oper.operation_id = items[7].strip('"')
            except:
                pass
            ops.append(oper)
        Oper.objects.bulk_create(ops)

            
    def backwards(self, orm):
        "Write your backwards methods here."

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
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'operation_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '3'}),
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
    symmetrical = True
