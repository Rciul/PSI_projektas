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
def Data_import(file):
    import csv
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
