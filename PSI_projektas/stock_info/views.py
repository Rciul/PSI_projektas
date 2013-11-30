from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.

from PSI_projektas.stock_info.models import Operation, Orderfailure
from PSI_projektas.stock_info.forms import FileForm, QualityForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import StringIO
import csv
from django.utils.translation import ugettext_lazy
from django.contrib import messages

def Data_import(csvfile):
    data_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    operation_list = []
    not_found_operation_count = 0
    failed_rows = 0
    success = 0
    for row in data_reader:
        try:
            operation_id = row[0].encode('utf-8')
            reason = row[1].encode('utf-8')
            amount = row[2].encode('utf-8')
            try:
                operation_ID = Operation.objects.get(operation_id=operation_id)
            except:
                not_found_operation_count += 1
                continue
            tmp = Orderfailure(operation = operation_ID, reason = reason, amount = amount)
            operation_list.append(tmp)
            success += 1
        except:
            failed_rows += 1
    Orderfailure.objects.bulk_create(operation_list)
    return {'not_found' : not_found_operation_count,
            'failed' : failed_rows,
            'success' : success}

def Data_export(queryset):
    import csv
    export_list = queryset.values_list('operation__operation_id', 'reason', 'amount')
    
    output = StringIO.StringIO()
    for row in export_list:
        print_str = ';'.join(['%s' % r for r in row])+"\n"
        output.write(print_str)
    output.seek(0)
    
#     with open(name_file, 'wb') as csvfile:
#         data_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         for row in export_list:
#             print ';'.join(['%s' % r for r in row])
#             data_writer.writerow(row)
    return output
    

def handleAction(request):
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def File_form(request):
    if request.method == 'GET':
        form = FileForm()
        data_for_templete = {'form' : form}
        rc = RequestContext(request, {})
        rc.autoescape = False
        return render_to_response('stock_info/fileimport.html', data_for_templete, rc)
    else:
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.cleaned_data['file_name']
            results = Data_import(data)
            err_msg = []
            if results['not_found']:
                err_msg.append(unicode(ugettext_lazy('Not found operations: %d' % results['not_found'])))
            if results['failed']:
                err_msg.append(unicode(ugettext_lazy('Failed rows: %d' % results['failed'])))
            if len(err_msg) > 0:
                messages.error(request, '; '.join(err_msg))
            else:
                messages.info(request, unicode(ugettext_lazy('Success: %s rows' % results['success'])))
    return HttpResponseRedirect('/admin/stock_info/orderfailure')
    
def Render_quality(request):
    if request.method == 'POST':
        #TODO
        pass
    form = QualityForm()
    data_for_templete = {'form' : form, 'is_popup' : False}
    rc = RequestContext(request, {})
    rc.autoescape = False
    return render_to_response('stock_info/quality_service.html', data_for_templete, rc)
