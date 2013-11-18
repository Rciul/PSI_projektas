from PSI_projektas.contrib.options import CustomModelAdmin
from django.contrib import admin
from PSI_projektas.stock_info.models import Customer, StockBalance,\
    StockKeepingUnit, LogInfo, Operation, Orderfailure

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

admin.site.register(Customer, CustomerAdmin)
admin.site.register(StockBalance, StockBalanceAdmin)
admin.site.register(StockKeepingUnit, StockKeepingUnitAdmin)
admin.site.register(LogInfo, LogInfoAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Orderfailure, OrderFailureAdmin)