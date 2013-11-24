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
def Data_import(f):
    import csv
    
    with open(f, 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in data_reader:
            #import pdb
            #pdb.set_trace()
            operation_id = row[0].encode('utf-8')
            reason = row[1].encode('utf-8')
            opertation_ID = Operation.objects.get(operation_id=operation_id)
            Orderfailure.objects.create(operation = opertation_ID, reason = reason)
            print operation_id+' - '+reason
