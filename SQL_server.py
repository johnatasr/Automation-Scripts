import sys
print sys.path
import pyodbc
import pandas as pd
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=<nomve_servidor>;DATABASE=<banco>;UID=<usuario>;PWD=<senha>;autocommit=True')
print ('Tentando criar conexão com o banco')
cursor = connection.cursor()
sql = """SELECT
LEFT(ltrim(ISNULL(IN_OUT_BUILDING_NUM,' '))+REPLICATE(' ', 10) , 10)+
LEFT( ltrim(ISNULL(IN_OUT_ADR_ORIG_SHORT,' '))+REPLICATE(' ', 50) , 50)+
LEFT(ltrim(ISNULL(IN_OUT_ADR_ORIG_CITY,' '))+REPLICATE(' ', 28) , 28)+
LEFT(ltrim(ISNULL(IN_OUT_ADR_ORIG_STATE,' '))+REPLICATE(' ', 2) , 2)+
LEFT(ltrim(ISNULL(IN_OUT_ADR_ORIG_ZIP,' '))+REPLICATE(' ', 9) , 9)
 FROM ADDR_VAL_STAN_PB;"""
DataOut = open("Address_Validation_Input_File.txt", "a+")

# Pegando dados para arquivo CSV
df_csv=pd.DataFrame()
while True:
# Lendo data
    df = pd.DataFrame(cursor.fetchall())
    if len(df) == 0:
        break

    else:
        df_csv.append(df)

#Camninho do arquivo
df_csv.to_csv('D:/path/test.txt', header=None, index=None, sep=' ', mode='a')

DataOut.close()
cursor.close()
connection.close()