from PSI_projektas.contrib.options import CustomModelAdmin
from django.contrib import admin
from PSI_projektas.stock_info.models import Customer, StockBalance,\
    StockKeepingUnit, LogInfo, Operation, Orderfailure

def exportCSV(request, queryset):
    pass
    
class CustomerAdmin(CustomModelAdmin):
    class Media:
        js=('customer.js')

class StockBalanceAdmin(CustomModelAdmin):
    actions = [exportCSV,]

class StockKeepingUnitAdmin(CustomModelAdmin):
    pass

class LogInfoAdmin(CustomModelAdmin):
    pass

class OperationAdmin(CustomModelAdmin):
    pass

class OrderFailureAdmin(CustomModelAdmin):
    pass



admin.site.register(Customer, CustomerAdmin)
admin.site.register(StockBalance, StockBalanceAdmin)
admin.site.register(StockKeepingUnit, StockKeepingUnitAdmin)
admin.site.register(LogInfo, LogInfoAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Orderfailure, OrderFailureAdmin)