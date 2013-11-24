# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Customers(models.Model):
    customerid = models.CharField(max_length=32L, db_column='CUSTOMERID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=96L, db_column='NAME', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=64L, db_column='CITY', blank=True) # Field name made lowercase.
    region = models.CharField(max_length=64L, db_column='REGION', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=64L, db_column='TYPE', blank=True) # Field name made lowercase.
    shippinglimit = models.DecimalField(decimal_places=30, null=True, max_digits=67, db_column='SHIPPINGLIMIT', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=128L, db_column='ADDRESS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'customers'

class Loginfo(models.Model):
    skuid = models.CharField(max_length=20L, db_column='SKUID', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255L, db_column='DESCRIPTION', blank=True) # Field name made lowercase.
    netweight = models.DecimalField(decimal_places=3, null=True, max_digits=11, db_column='NETWEIGHT', blank=True) # Field name made lowercase.
    bruttoweight = models.DecimalField(decimal_places=3, null=True, max_digits=11, db_column='BRUTTOWEIGHT', blank=True) # Field name made lowercase.
    unitsperparcel = models.DecimalField(decimal_places=0, null=True, max_digits=7, db_column='UNITSPERPARCEL', blank=True) # Field name made lowercase.
    unitsperpallet = models.DecimalField(decimal_places=0, null=True, max_digits=7, db_column='UNITSPERPALLET', blank=True) # Field name made lowercase.
    shelflifeperiod = models.DecimalField(decimal_places=0, null=True, max_digits=7, db_column='SHELFLIFEPERIOD', blank=True) # Field name made lowercase.
    mu = models.CharField(max_length=8L, db_column='MU', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=20L, db_column='LOCATION', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'loginfo'

class Operations(models.Model):
    document = models.CharField(max_length=20L, db_column='DOCUMENT') # Field name made lowercase.
    direction = models.CharField(max_length=20L, db_column='DIRECTION') # Field name made lowercase.
    skuid = models.CharField(max_length=20L, db_column='SKUID') # Field name made lowercase.
    qty = models.DecimalField(decimal_places=3, max_digits=12, db_column='QTY') # Field name made lowercase.
    location = models.CharField(max_length=20L, db_column='LOCATION') # Field name made lowercase.
    customerid = models.CharField(max_length=32L, db_column='CUSTOMERID', blank=True) # Field name made lowercase.
    operationid = models.DecimalField(decimal_places=30, null=True, max_digits=67, db_column='OID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'operations'

class Sku(models.Model):
    skuid = models.CharField(max_length=20L, db_column='SKUID',null=True) # Field name made lowercase.
    skugroup = models.CharField(max_length=32L, db_column='SKUGROUP', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255L, db_column='DESCRIPTION', blank=True) # Field name made lowercase.
    mu = models.CharField(max_length=8L, db_column='MU', blank=True) # Field name made lowercase.
    baseunits = models.DecimalField(decimal_places=0, null=True, max_digits=4, db_column='BASEUNITS', blank=True) # Field name made lowercase.
    unitsperparcel = models.DecimalField(decimal_places=0, null=True, max_digits=7, db_column='UNITSPERPARCEL', blank=True) # Field name made lowercase.
    unitsperpallet = models.DecimalField(decimal_places=0, null=True, max_digits=7, db_column='UNITSPERPALLET', blank=True) # Field name made lowercase.
    manufacturer = models.CharField(max_length=64L, db_column='MANUFACTURER', blank=True) # Field name made lowercase.
    countryoforigin = models.CharField(max_length=64L, db_column='COUNTRYOFORIGIN', blank=True) # Field name made lowercase.
    traditionaltrade = models.DecimalField(decimal_places=0, null=True, max_digits=2, db_column='TRADITIONALTRADE', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=20L, db_column='LOCATION', blank=True) # Field name made lowercase.
    netweight = models.DecimalField(decimal_places=3, null=True, max_digits=11, db_column='NETWEIGHT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'sku'

class StockBalance(models.Model):
    skuid = models.CharField(max_length=20L, db_column='SKUID', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255L, db_column='DESCRIPTION', blank=True) # Field name made lowercase.
    qty = models.DecimalField(decimal_places=3, null=True, max_digits=12, db_column='QTY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'stock_balance'

