"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from PSI_projektas.stock_info.models import Orderfailure, Operation, \
    StockKeepingUnit, Customer
from decimal import Decimal
import random
from datetime import date, datetime, timedelta
import time

class ServiceLevelCalculationTest(TestCase):
    
    def test_one_hundred_percent_test(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        for i in xrange(100):
            oper = Operation.objects.create(document='test',
                                            direction='test',
                                            stock_keeping_unit=skus[i % 5],
                                            quantity=Decimal('1.000'),
                                            location='test',
                                            operation_date=date.today(),
                                            customer=test_customer,
                                            operation_id=i,
                                            date=datetime.now())
            
            created_items.append(oper)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [100]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()
            
    def test_one_week_period_one_hundred_percent(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        for j in xrange(7):
            for i in xrange(100):
                oper = Operation.objects.create(document='test',
                                                direction='test',
                                                stock_keeping_unit=skus[i % 5],
                                                quantity=Decimal('1.000'),
                                                location='test',
                                                operation_date=date.today(),
                                                customer=test_customer,
                                                operation_id=i,
                                                date=datetime.now()-timedelta(days=j))
                oper.date=datetime.now()-timedelta(days=j)
                oper.save()
                created_items.append(oper)
        
        for a in xrange(5):
            test_times = []
            levels = []
            for i in xrange(7):
                test_times.append(time.mktime((date.today()-timedelta(days=i)).timetuple()) * 1000)
                levels.append(100)
            expected_level = [test_times[::-1], levels]
            res = Orderfailure.calculate_service_level(date.today()-timedelta(days=6), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()

    def test_less_than_one_hundred_percent(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        opers = []
        for i in xrange(100):
            oper = Operation.objects.create(document='test',
                                                direction='test',
                                                stock_keeping_unit=skus[i % 5],
                                                quantity=Decimal('1.000'),
                                                location='test',
                                                operation_date=date.today(),
                                                customer=test_customer,
                                                operation_id=i,
                                                date=datetime.now())
            created_items.append(oper)
            opers.append(oper)
            if i % 2 == 0:
                fail = Orderfailure.objects.create(operation=oper,
                                                   reason='test',
                                                   amount=Decimal('1.000'))
                created_items.append(fail)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [50]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()
            
            
            
            
    def test_one_hundred_percent_test_orders(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        for i in xrange(100):
            oper = Operation.objects.create(document='test',
                                            direction='test',
                                            stock_keeping_unit=skus[i % 5],
                                            quantity=Decimal('1.000'),
                                            location='test',
                                            operation_date=date.today(),
                                            customer=test_customer,
                                            operation_id=i,
                                            date=datetime.now())
            
            created_items.append(oper)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [100]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level_by_orders(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()
            
    def test_one_week_period_one_hundred_percent_orders(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        for j in xrange(7):
            for i in xrange(100):
                oper = Operation.objects.create(document='test',
                                                direction='test',
                                                stock_keeping_unit=skus[i % 5],
                                                quantity=Decimal('1.000'),
                                                location='test',
                                                operation_date=date.today(),
                                                customer=test_customer,
                                                operation_id=i,
                                                date=datetime.now()-timedelta(days=j))
                oper.date=datetime.now()-timedelta(days=j)
                oper.save()
                created_items.append(oper)
        
        for a in xrange(5):
            test_times = []
            levels = []
            for i in xrange(7):
                test_times.append(time.mktime((date.today()-timedelta(days=i)).timetuple()) * 1000)
                levels.append(100)
            expected_level = [test_times[::-1], levels]
            res = Orderfailure.calculate_service_level_by_orders(date.today()-timedelta(days=6), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()

    def test_less_than_one_hundred_percent_orders(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        opers = []
        for i in xrange(100):
            oper = Operation.objects.create(document='test',
                                                direction='test',
                                                stock_keeping_unit=skus[i % 5],
                                                quantity=Decimal('1.000'),
                                                location='test',
                                                operation_date=date.today(),
                                                customer=test_customer,
                                                operation_id=i,
                                                date=datetime.now())
            created_items.append(oper)
            opers.append(oper)
            if i % 2 == 0:
                fail = Orderfailure.objects.create(operation=oper,
                                                   reason='test',
                                                   amount=Decimal('1.000'))
                created_items.append(fail)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [50]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level_by_orders(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()
            
    def test_null_orders(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [None]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level_by_orders(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()
            
    def test_null(self):
        created_items = []
        skus = []
        test_customer = Customer.objects.create(customer_id='test',
                                                name='test',
                                                city='city',
                                                region='region',
                                                type='type',
                                                shipping_limit=100,
                                                address='test')
        created_items.append(test_customer)
        for a in xrange(5):
            sku = StockKeepingUnit.objects.create(stock_keeping_unit_id=str(a),
                                                  group='test%s' % a,
                                                  description='test',
                                                  units_per_parcel=1,
                                                  units_per_pallet=1,
                                                  manufacturer='test',
                                                  country_of_origin='test',
                                                  traditional_trade=False,
                                                  location='test',
                                                  net_weight=Decimal('1.000'),
                                                  measurement_unit='test',
                                                  base_units=Decimal('1.000'))
            created_items.append(sku)
            skus.append(sku)
        test_time = time.mktime(date.today().timetuple()) * 1000
        expected_level = [[test_time], [None]]
        for a in xrange(5):
            res = Orderfailure.calculate_service_level(date.today(), date.today(), 'test%s' % a)
            trace = 'expected:%(exp)s, result:%(res)s'
            trace = trace % {'exp' : expected_level,
                             'res' : res}
            self.assertEqual(res[0], expected_level[0], trace)
            self.assertEqual(res[1], expected_level[1], trace)
        for item in created_items[::-1]:
            item.delete()

class ImportTest(TestCase):
    def test_import(self):
        content = '''
        1;lol;10.000
        2;Blogas uzsakymas;2.300
        1;Negautas uzsakymas;2.200'''
        