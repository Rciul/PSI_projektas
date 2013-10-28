from django.db import models

# Create your models here.

class Customer (models.Model):
    customer_id = models.CharField('Užsakovo Nr.', max_lenght=32, null=True)
    name = models.CharField('Vardas', max_lenght=96, null=True)
    city = models.CharField('Miestas', max_lenght=64, null=True)
    region = models.CharField('Regionas', max_lenght=64, null=True) 
    type = models.CharField('Tipas', max_lenght=64, null=True)
    shipping_limit = models.IntegerField('Pristatymo terminas', null=True)
    address = models.CharField('Adresas', max_lenght=128, null=True) 

class StockBalance (models.Model):
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", null=True)
    description = models.CharField('Aprašymas', max_lenght=255, null=True)
    quantity = models.DecimalField('Kiekis', max_digits=10, decimal_places=3, null=True)
    
class StockKeepingUnit (models.Model):
    stock_keeping_unit_id = models.CharField('Atsargų ID', max_lenght=20)
    group = models.CharField('Grupė', max_lenght=32)
    description = models.CharField('Aprašymas', max_lenght=255, null=True)
    units_per_parcel = models.IntegerField('Vienetų per siuntą', null=True)
    units_per_pallet = models.IntegerField('Vienetų per paletę')
    manufacturer = models.CharField('Gamintojas', max_lenght=64, null=True)
    country_of_origin = models.CharField('Kilmės šalis', max_lenght=64, null=True)
    traditional_trade = models.BooleanField('Tradicinė prekyba', null=True)
    location = models.CharField('Vieta', max_lenght=20, null=True)
    net_weight = models.DecimalField('Neto svoris', max_digits=9, decimal_places=3, null=True)
    
class LogInfo (models.Model):
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", null=True)
    description = models.CharField('Aprašymas', max_lenght=255, null=True)
    net_weight = models.DecimalField('Neto svoris', max_digits=9, decimal_places=3, null=True)
    brutto_weight = models.DecimalField('Bruto svoris', max_digits=9, decimal_places=3, null=True)
    units_per_parcel = models.IntegerField('Vienetų per siuntą', null=True)
    units_per_pallet = models.IntegerField('Vienetų per paletę', null=True)
    shelf_life_period = models.IntegerField('Galiojimo laikas', null=True)
    measurement_unit = models.CharField('Matavimo vienetas', max_lenght=8, null=True)
    location = models.CharField('Vieta', max_lenght=20, null=True)
    
class Operation (models.Model):
    document = models.CharField('Dokumentas', max_lenght=20)
    direction = models.CharField('Kryptis', max_lenght=20)
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit")
    quantity = models.DecimalField('Kiekis', max_digits=10, decimal_places=3)
    location = models.CharField('Vieta', max_lenght=20)
    operation_date = models.DateField('Data', auto_now_add=False)
    customer = models.ForeignKey("Customer", null=True)
    operation_id = models.IntegerField('Operacijos ID', null=True)
    
class Orderfailute (models.Model):
    operation = models.ForeignKey("Operation")
    reason = models.CharField('Priežastis', max_lenght=255)
    
    
    
    
