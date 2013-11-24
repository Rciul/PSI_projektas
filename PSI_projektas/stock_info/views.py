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
from PSI_projektas.stock_info.forms import FileForm, QualityForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
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

def Data_export():
    import csv
    with open("export.csv", 'rb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        #for row in data_reader:
        #import pdb
        #pdb.set_trace()
#         data_writer.writerow()
#         operation_id = row[0].encode('utf-8')
#         reason = row[1].encode('utf-8')
#         opertation_ID = Operation.objects.get(operation_id=operation_id)
#         Orderfailure.objects.create(operation = opertation_ID, reason = reason)
#         print operation_id+' - '+reason

def handleAction(request):
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
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
    
def Render_quality(request):
    if request.method == 'POST':
        #TODO
        pass
    form = QualityForm()
    data_for_templete = {'form' : form, 'is_popup' : False}
    rc = RequestContext(request, {})
    rc.autoescape = False
    return render_to_response('admin/stock_info/quality_service.html', data_for_templete, rc)
