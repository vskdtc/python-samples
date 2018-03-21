#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","DB3" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

user_name = input("Enter your User Name: ")
user_name = str(user_name)
sql = "SELECT user_id, id_urn, username, email, created_date, lastUpdated_date, time_zone, modified_by FROM user WHERE username = %(user_name)s"
print('executed SQL query:')
print(sql)
print('results:')
cursor.execute(sql, {'user_name': user_name })
for row in cursor:
  print(row)

db.close()