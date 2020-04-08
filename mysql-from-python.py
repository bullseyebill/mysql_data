import os
import pymysql


# (modify this variable if running on another environment)
username = os.getenv('GITPOD_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()        
finally:
    connection.close()