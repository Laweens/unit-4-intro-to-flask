import pymysql 
import pymysql.cursors
from pprint import pprint as print 

connect = pymysql.connect(
    database = 'world',
    user = 'lfrancois',
    password = '231566837',
    host = '10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connect.cursor()
cursor.execute("SELECT `Name`, `Continent` FROM `country`")
results = cursor.fetchall()

print(results[0]['Continent'])

for x in results:
    print(x['Continent'])