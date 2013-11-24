from PSI_projektas.contrib.options import CustomModelAdmin
from django.contrib import admin
from PSI_projektas.stock_info.models import Customer, StockBalance,\
    StockKeepingUnit, LogInfo, Operation, Orderfailure
from PSI_projektas.stock_info.views import Data_export
from django.http import HttpResponse
from django.utils.encoding import smart_str
import datetime


    
class CustomerAdmin(CustomModelAdmin):
    list_display = Customer.list_display
    class Media:
        js=('customer.js')

class StockBalanceAdmin(CustomModelAdmin):
    list_display = StockBalance.list_display


class StockKeepingUnitAdmin(CustomModelAdmin):
    list_display = StockKeepingUnit.list_display

class LogInfoAdmin(CustomModelAdmin):
    list_display = LogInfo.list_display

class OperationAdmin(CustomModelAdmin):
    list_display = Operation.list_display

class OrderFailureAdmin(CustomModelAdmin):
    list_display = Orderfailure.list_display
    actions = ['exportCSV']
    def exportCSV(self, request, queryset):
        name_file = "export%s.csv" % datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        mimetype = 'text/csv'
        export_file = Data_export(queryset)
        response = HttpResponse(content=export_file.getvalue(),
                                        mimetype=mimetype)
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(name_file)
        #response['X-Sendfile'] = smart_str(export_file)
        
        return response



admin.site.register(Customer, CustomerAdmin)
admin.site.register(StockBalance, StockBalanceAdmin)
admin.site.register(StockKeepingUnit, StockKeepingUnitAdmin)
admin.site.register(LogInfo, LogInfoAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Orderfailure, OrderFailureAdmin)