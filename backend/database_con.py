import pyodbc

# DATABASE DATA
conn = pyodbc.connect('Driver={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.2.so.0.1};'
                      'Server=tcp:codersi06mssqlckwl3pv5lf5q4.database.windows.net,1433;'
                      'Database=HackathonPOS;'
                      'UID=codersi06;'
                      'PWD=9D45PxuArXjF;')

cursor = conn.cursor()

headers_tpd = 'TPD.TxnData, TPD.TxnCzas, TPD.anon_kwota, TPD.DCC, TPD.TypePayment, '
headers_merchant = 'MERCHANT.MCC, MERCHANT.LocZipCode '

main_query = 'SELECT TOP 10 ' + headers_tpd + headers_merchant + \
    ' from TPD INNER JOIN MERCHANT ON TPD.anon_MID = anon_Eid' + \
    ' where TxnData > 20180731'

# where TxnData > 20180731 group by TxnData 

test_query = 'select TOP 25 MCC, LocCity, LocZipCode, COUNT(ROWID), SUM(TPD.anon_Kwota), TxnData FROM TPD join MERCHANT on Merchant.anon_EID = TPD.anon_MID group by TxnData, anon_Eid, MCC, LocCity, LocZipCode ORDER BY COUNT(ROWID) DESC'

cursor.execute(test_query)


columns = [column[0] for column in cursor.description]
print(columns)
for row in cursor:
    print(row)