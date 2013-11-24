# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
import random
from PSI_projektas.oracle.models import Customers as OracleCustomer,\
    StockBalance as OracleStockBalance, Sku as SKU, Loginfo as OLI, Operations as OP

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        
        def create_sku(skuid):
            sku_count = SKU.objects.using('oracle').count()
            index = random.randint(0, sku_count-1)
            obj = SKU.objects.using('oracle')[index]
            obj.id = None
            obj.skuid = skuid          
            obj.save()
            
        def create_customer(customerid):
            sku_count = OracleCustomer.objects.using('oracle').count()
            index = random.randint(0, sku_count-1)
            obj = OracleCustomer.objects.using('oracle')[index]
            obj.id = None
            obj.customerid = customerid       
            obj.save()
        
        def move_customers():
            print 'Moving customers'
            Customer = orm.Customer
            customer_count = OracleCustomer.objects.using('oracle').count()
            for customer in OracleCustomer.objects.using('oracle').all():
                Customer.objects.create(customer_id=customer.customerid,
                                        name=customer.name,
                                        city=customer.city,
                                        type=customer.type,
                                        shipping_limit=customer.shippinglimit,
                                        address=customer.address)
                
                
        def move_stock_balance():
            print 'Moving stock balance'
            StockBalance = orm.StockBalance
            customer_count = OracleStockBalance.objects.using('oracle').count()
            i = 0
            last_printed = -1
            for balance in OracleStockBalance.objects.using('oracle').all():
                try:
                    StockBalance.objects.create(stock_keeping_unit_id=SKU.objects.using('oracle').get(skuid=balance.skuid).id,
                                                description=balance.description,
                                                quantity=balance.qty)
                except:
                    create_sku(balance.skuid)
                    StockBalance.objects.create(stock_keeping_unit_id=SKU.objects.using('oracle').get(skuid=balance.skuid).id,
                                                description=balance.description,
                                                quantity=balance.qty)
                
        def move_sku():
            print 'Moving stock keeping unit'
            sku = orm.StockKeepingUnit
            customer_count = SKU.objects.using('oracle').count()
            i = 0
            last_printed = -1
            for s in SKU.objects.using('oracle').all():
                sku.objects.create(stock_keeping_unit_id=s.skuid,
                                   group=s.skugroup,
                                   description=s.description,
                                   measurement_unit=s.mu or '',
                                   base_units=s.baseunits,
                                   units_per_parcel=s.unitsperparcel,
                                   units_per_pallet=s.unitsperpallet,
                                   manufacturer=s.manufacturer,
                                   country_of_origin=s.countryoforigin,
                                   traditional_trade=False if s.traditionaltrade == 0 else True,
                                   location=s.location,
                                   net_weight=s.netweight)
                i += 1.0 / customer_count
                if int(i) > last_printed:
                    print i / 100, '%'
                    last_printed = i
        
        def move_log_info():
            print 'Moving log info'
            LogInfo = orm.LogInfo
            customer_count = OLI.objects.using('oracle').count()
            for li in OLI.objects.using('oracle').all():
                try:
                    LogInfo.objects.create(stock_keeping_unit_id=SKU.objects.using('oracle').get(skuid=li.skuid).id if li.skuid else None,
                                           description=li.description,
                                           net_weight=li.netweight,
                                           brutto_weight=li.bruttoweight,
                                           units_per_parcel=li.unitsperparcel,
                                           units_per_pallet=li.unitsperpallet,
                                           shelf_life_period=li.shelflifeperiod,
                                           measurement_unit=li.mu,
                                           location=li.location)
                except:
                    create_sku(li.skuid)
                    LogInfo.objects.create(stock_keeping_unit_id=SKU.objects.using('oracle').get(skuid=li.skuid).id,
                                           description=li.description,
                                           net_weight=li.netweight,
                                           brutto_weight=li.bruttoweight,
                                           units_per_parcel=li.unitsperparcel,
                                           units_per_pallet=li.unitsperpallet,
                                           shelf_life_period=li.shelflifeperiod,
                                           measurement_unit=li.mu,
                                           location=li.location)
        
        def move_operations():
            print 'Moving operations'
            Operation = orm.Operation
            customer_count = OP.objects.using('oracle').count()
            for op in OP.objects.using('oracle').all():
                try:
                    Operation.objects.create(document=op.document,
                                             direction=op.direction,
                                             stock_keeping_unit_id=SKU.objects.using('oracle').filter(skuid=op.skuid)[0].id,
                                             quantity=op.qty,
                                             location=op.location,
                                             operation_date=datetime.date.today() - datetime.timedelta(days=random.randint(0, 366)),
                                             customer_id=OracleCustomer.objects.using('oracle').filter(customerid=op.customerid)[0].id if op.customerid else None,
                                             operation_id=op.operationid)
                except:
                    if SKU.objects.using('oracle').filter(skuid=op.skuid).count() == 0:
                        create_sku(op.skuid)
                    if OracleCustomer.objects.using('oracle').filter(customerid=op.customerid).count() == 0:
                        create_customer(op.customerid)
                    try:
                        Operation.objects.create(document=op.document,
                                             direction=op.direction,
                                             stock_keeping_unit_id=SKU.objects.using('oracle').filter(skuid=op.skuid)[0].id,
                                             quantity=op.qty,
                                             location=op.location,
                                             operation_date=datetime.date.today() - datetime.timedelta(days=random.randint(0, 366)),
                                             customer_id=OracleCustomer.objects.using('oracle').filter(customerid=op.customerid)[0].id if op.customerid else None,
                                             operation_id=op.operationid)
                    except:
                        pass
                
        move_customers()
        move_sku()
        move_stock_balance()
        move_log_info()
        move_operations()

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
            'group': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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
