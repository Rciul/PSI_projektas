from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Customer (models.Model):
    customer_id = models.CharField('Customer ID', max_length=32, null=True)
    name = models.CharField('Name', max_length=96, null=True)
    city = models.CharField('City', max_length=64, null=True)
    region = models.CharField('Region', max_length=64, null=True) 
    type = models.CharField('Type', max_length=64, null=True)
    shipping_limit = models.IntegerField('Shipping limit', null=True)
    address = models.CharField('Address', max_length=128, null=True) 
    
    list_display = ('customer_id', 'name', 'city', 'region', 'type',
                    'shipping_limit', 'address')
    
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        
    def __unicode__(self):
        return u'%(name)s' % {'name' : self.name}

class StockBalance (models.Model):
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", null=True,
                                           verbose_name=_('Stock keeping unit'))
    description = models.CharField('Description', max_length=255, null=True)
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=3, null=True)
    
    list_display = ('stock_keeping_unit', 'description', 'quantity')
    
    class Meta:
        verbose_name = _('Stock balance')
        verbose_name_plural = _('Stock balance')
        
    def __unicode__(self):
        return u'%(description)s' % {'description' : self.description}
    
class StockKeepingUnit (models.Model):
    stock_keeping_unit_id = models.CharField('Stock keeping unit ID', max_length=20)
    group = models.CharField('Group', max_length=32)
    description = models.CharField('Description', max_length=255, null=True)
    units_per_parcel = models.IntegerField('Units per parcel', null=True)
    units_per_pallet = models.IntegerField('Units per pallette')
    manufacturer = models.CharField('Manufacturer', max_length=64, null=True)
    country_of_origin = models.CharField('Country of origin', max_length=64, null=True)
    traditional_trade = models.BooleanField('Traditional trade', default=False)
    location = models.CharField('Location', max_length=20, null=True)
    net_weight = models.DecimalField('Net weight', max_digits=9, decimal_places=3, null=True)
    
    list_display = ('stock_keeping_unit_id', 'group', 'description', 'manufacturer', 'location')
    
    class Meta:
        verbose_name = _('Stock keeping unit')
        verbose_name_plural = _('Stock keeping units')
        
    def __unicode__(self):
        return u'%(group)s: %(description)s' % {'group' : self.group,
                                      'description' : self.description}
    
class LogInfo (models.Model):
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", null=True,
                                           verbose_name=_('Stock keeping unit'))
    description = models.CharField('Description', max_length=255, null=True)
    net_weight = models.DecimalField('Net weight', max_digits=9, decimal_places=3, null=True)
    brutto_weight = models.DecimalField('Brutto weight', max_digits=9, decimal_places=3, null=True)
    units_per_parcel = models.IntegerField('Units per parcel', null=True)
    units_per_pallet = models.IntegerField('Units per pallette', null=True)
    shelf_life_period = models.IntegerField('Shelf life period', null=True)
    measurement_unit = models.CharField('Mesaurement unit', max_length=8, null=True)
    location = models.CharField('Location', max_length=20, null=True)
    
    list_display = ('stock_keeping_unit', 'description', 'location')
    
    class Meta:
        verbose_name = _('Log info')
        verbose_name_plural = _('Log info')
        
    def __unicode__(self):
        return u'%(unit)s (%(description)s)' % {'unit' : self.stock_keeping_unit,
                                                'description' : self.description}
    
class Operation (models.Model):
    document = models.CharField('Document', max_length=20)
    direction = models.CharField('Direction', max_length=20)
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", verbose_name=_('Stock keeping unit'))
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=3)
    location = models.CharField('Location', max_length=20)
    operation_date = models.DateField('Operation date', auto_now_add=False)
    customer = models.ForeignKey("Customer", null=True, verbose_name=_('Customer'))
    operation_id = models.IntegerField('Operation ID', null=True)
    
    list_display = ('document', 'direction')
    
    class Meta:
        verbose_name = _('Operation')
        verbose_name_plural = _('Operations')
        
    def __unicode__(self):
        return u'%(operation)s' % {'operation' : self.operation_id}
    
class Orderfailure (models.Model):
    operation = models.ForeignKey("Operation", verbose_name=_('Operation'))
    reason = models.CharField('Reason', max_length=255)
    
    list_display = ('operation', 'reason')

    class Meta:
        verbose_name = _('Order failure')
        verbose_name_plural = _('Order failures')
        
    def __unicode__(self):
        return u'%(operation)s' % self.operation
