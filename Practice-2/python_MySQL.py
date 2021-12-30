import mysql.connector
from mysql.connector import Error 

Connection = mysql.connector.connect(host="localhost",
                                     database="pytest",
                                     user="hemanth",
                                     password="12345")

print(Connection.get_server_info())