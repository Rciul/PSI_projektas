from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
# import csv
# import MySQLdb
# 
# mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='root',
#     db='psi')
# cursor = mydb.cursor()
# 
# csv_data = csv.reader(file('data.csv'))
# for row in csv_data:
#     
#     
# #close the connection to the database.
# mydb.commit()
# cursor.close()
# print "Done"
from PSI_projektas.stock_info.models import Operation, Orderfailure
from PSI_projektas.stock_info.forms import FileForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import StringIO
def Data_import(f):
    import csv
    
    with open(f, 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        operation_list = []
        for row in data_reader:
            #import pdb
            #pdb.set_trace()
            operation_id = row[0].encode('utf-8')
            reason = row[1].encode('utf-8')
            amount = row[2].encode('utf-8')
            operation_ID = Operation.objects.get(operation_id=operation_id)
#             import pdb
#             pdb.set_trace()
            tmp = Orderfailure(operation = operation_ID, reason = reason, amount = amount)
            operation_list.append(tmp)
        Orderfailure.objects.bulk_create(operation_list)
        print "Baige "

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
    

def File_form(request):
    if request.method == 'GET':
        form = FileForm()
        data_for_templete = {'form' : form,
                             'is_popup' : True}
        rc = RequestContext(request, {})
        rc.autoescape = False
        return render_to_response('stoc_info/fileimport.html', data_for_templete, rc)
    else:
        form = FileForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            Data_import(file_name)
            close = """<script type="text/javascript">
            window.close();
            </script>"""
            return HttpResponse(close)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
