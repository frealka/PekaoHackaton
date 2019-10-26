import pyodbc

# DATABASE DATA
conn = pyodbc.connect('Driver={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.2.so.0.1};'
                      'Server=tcp:codersi06mssqlckwl3pv5lf5q4.database.windows.net,1433;'
                      'Database=HackathonPOS;'
                      'UID=codersi06;'
                      'PWD=9D45PxuArXjF;')

cursor = conn.cursor()

headers_tpd = 'TPD.TxnData, TPD.TxnCzas, TPD.anon_kwota, TPD.DCC, TPD.TypePayment,'
headers_merchant = 'MERCHANT.MCC, MERCHANT.LocCity, MERCHANT.LocZipCode '
cursor.execute('SELECT TOP 10' + headers_tpd + headers_merchant + 'from TPD INNER JOIN MERCHANT ON TPD.anon_MID = anon_Eid')


columns = [column[0] for column in cursor.description]
print(columns)
for row in cursor:
    print(row)