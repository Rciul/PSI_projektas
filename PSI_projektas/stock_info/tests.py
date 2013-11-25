"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from PSI_projektas.stock_info.models import Orderfailure


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ImportTest(TestCase):
    def setUp(self):
        import csv
        with open('TestingImportFile.csv', 'wb') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in export_list:
                print ';'.join(['%s' % r for r in row])
                data_writer.writerow(row)
        
#         Orderfailure.objects.create(operation = "1", reasons = 'Testuojant Neivykdyta', amount = 50.5)
                
    def GoodImport(self):
        Test1 = Orderfailure.objects.get(operation = '1')
        self.assertEqual(, '')
        