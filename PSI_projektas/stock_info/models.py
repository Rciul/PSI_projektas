from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.aggregates import Sum
import datetime
from datetime import timedelta
import time
from decimal import Decimal


# Create your models here.

class Customer (models.Model):
    customer_id = models.CharField(_('Customer ID'), max_length=32, null=True)
    name = models.CharField(_('Name'), max_length=96, null=True)
    city = models.CharField(_('City'), max_length=64, null=True)
    region = models.CharField(_('Region'), max_length=64, null=True) 
    type = models.CharField(_('Type'), max_length=64, null=True)
    shipping_limit = models.IntegerField(_('Shipping limit'), null=True)
    address = models.CharField(_('Address'), max_length=128, null=True)
    
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
    stock_keeping_unit_id = models.CharField(_('Stock keeping unit ID'), max_length=20)
    group = models.CharField(_('Group'), max_length=32, blank=True, null=True)
    description = models.CharField(_('Description'), max_length=255, null=True)
    units_per_parcel = models.IntegerField(_('Units per parcel'), null=True)
    units_per_pallet = models.IntegerField(_('Units per pallette'))
    manufacturer = models.CharField(_('Manufacturer'), max_length=64, null=True)
    country_of_origin = models.CharField(_('Country of origin'), max_length=64, null=True)
    traditional_trade = models.BooleanField(_('Traditional trade'), default=False)
    location = models.CharField(_('Location'), max_length=20, null=True)
    net_weight = models.DecimalField(_('Net weight'), max_digits=9, decimal_places=3, null=True)
    measurement_unit = models.CharField(_('Measurement unit'), max_length=8, blank=True)
    base_units = models.DecimalField(_('Base units'), decimal_places=0, null=True, max_digits=4, blank=True)
    
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
    description = models.CharField(_('Description'), max_length=255, null=True)
    net_weight = models.DecimalField(_('Net weight'), max_digits=9, decimal_places=3, null=True)
    brutto_weight = models.DecimalField(_('Brutto weight'), max_digits=9, decimal_places=3, null=True)
    units_per_parcel = models.IntegerField(_('Units per parcel'), null=True)
    units_per_pallet = models.IntegerField(_('Units per pallette'), null=True)
    shelf_life_period = models.IntegerField(_('Shelf life period'), null=True)
    measurement_unit = models.CharField(_('Measurement unit'), max_length=8, null=True)
    location = models.CharField(_('Location'), max_length=20, null=True)
    
    list_display = ('stock_keeping_unit', 'description', 'location')
    
    class Meta:
        verbose_name = _('Log info')
        verbose_name_plural = _('Log info')
        
    def __unicode__(self):
        return u'%(unit)s (%(description)s)' % {'unit' : self.stock_keeping_unit,
                                                'description' : self.description}
    
class Operation (models.Model):
    document = models.CharField(_('Document'), max_length=20)
    direction = models.CharField(_('Direction'), max_length=20)
    stock_keeping_unit = models.ForeignKey("StockKeepingUnit", verbose_name=_('Stock keeping unit'))
    quantity = models.DecimalField(_('Quantity'), max_digits=10, decimal_places=3, default = 0)
    location = models.CharField(_('Location'), max_length=20)
    customer = models.ForeignKey("Customer", null=True, verbose_name=_('Customer'))
    operation_id = models.IntegerField(_('Operation ID'), null=True)
    date = models.DateTimeField(_('Date'), auto_now_add=True)
    list_display = ('get_operation_id', 'date', 'document', 'direction')
    
    class Meta:
        verbose_name = _('Operation')
        verbose_name_plural = _('Operations')
        
    def __unicode__(self):
        return u'%(operation)s' % {'operation' : self.operation_id}
    
    def get_operation_id(self):
        return self.operation_id or u'--'
    get_operation_id.short_description = _('Operation ID')
    get_operation_id.admin_order_field = 'operation_id'
    
class Orderfailure (models.Model):
    date = models.DateTimeField(_('Date'), auto_now_add=True)
    operation = models.ForeignKey("Operation", verbose_name=_('Operation'))
    reason = models.CharField(_('Reason'), max_length=255)
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=3)
    
    list_display = ('operation', 'reason')

    class Meta:
        verbose_name = _('Order failure')
        verbose_name_plural = _('Order failures')
        
    def __unicode__(self):

        return u'%(operation)s' % {'operation':self.operation}

    @classmethod
    def calculate_service_level(cls, date_from, date_to, group):
        time1 = time.time()
        date_to = date_to + timedelta(days=1)
        operations = list(Operation.objects.filter(stock_keeping_unit__group=group,
                                              date__gte=date_from,
                                              date__lte=date_to))
        time2 = time.time()
        print 'loaded', time2-time1
        dates = []
        levels = []
        start_date = date_from
        while start_date < date_to:
            start = datetime.datetime(year=start_date.year,
                                      month=start_date.month,
                                      day=start_date.day,
                                      hour=0,
                                      minute=0,
                                      second=0)
            end = datetime.datetime(year=start_date.year,
                                    month=start_date.month,
                                    day=start_date.day,
                                    hour=23,
                                    minute=59,
                                    second=59)
#             date_opers = operations.filter(date__gte=start,
#                                            date__lte=end)
            date_opers = [operation for operation in operations if operation.date >= start and operation.date <= end]
            
            fails = cls.objects.filter(operation__in=date_opers)
            
            
            failed_amount = fails.aggregate(Sum('amount'))['amount__sum'] or 0
            time3 = time.time()
#             operation_amount = date_opers.aggregate(Sum('quantity'))['quantity__sum'] or 0
            operation_amount = sum([o.quantity for o in date_opers])
            time4 = time.time()
            dates.append(time.mktime(start_date.timetuple())*1000)
            if operation_amount > 0:
                levels.append(100 - 100 * (failed_amount / operation_amount if failed_amount > 0 else 0))
            else:
                levels.append(None)
            start_date = start_date + datetime.timedelta(days=1)
            
            print 'calc', time4-time3
        print dates, levels
        return dates, levels

    @classmethod
    def calculate_service_level_by_orders(cls, date_from, date_to, group):
        time1 = time.time()
        date_to = date_to + timedelta(days=1)
        operations = list(Operation.objects.filter(stock_keeping_unit__group=group,
                                              date__gte=date_from,
                                              date__lte=date_to).only('date',))
        time2 = time.time()
        print 'loaded', time2-time1
        dates = []
        levels = []
        start_date = date_from
        while start_date < date_to:
            start = datetime.datetime(year=start_date.year,
                                      month=start_date.month,
                                      day=start_date.day,
                                      hour=0,
                                      minute=0,
                                      second=0)
            end = datetime.datetime(year=start_date.year,
                                    month=start_date.month,
                                    day=start_date.day,
                                    hour=23,
                                    minute=59,
                                    second=59)
            date_opers = [operation for operation in operations if operation.date >= start and operation.date <= end]
            
            fails = cls.objects.filter(operation__in=date_opers)
            
            
            failed_amount = fails.count()
            time3 = time.time()
            operation_amount = len(date_opers)
            time4 = time.time()
            dates.append(time.mktime(start_date.timetuple())*1000)
            if operation_amount > 0:
                levels.append(100 - 100 * (Decimal(float(failed_amount) / float(operation_amount)) if failed_amount > 0 else 0))
            else:
                levels.append(None)
            start_date = start_date + datetime.timedelta(days=1)
            
            print 'calc', time4-time3
        return dates, levels
