import mysql.connector

try:
    dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
    )

    # cursor object

    cursorObject = dataBase.cursor()

    # Create database
    cursorObject.execute('CREATE DATABASE django_crm')
    print('ALL Done')
except Exception as e:
    print(f'Error: {e}')