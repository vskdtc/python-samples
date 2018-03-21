from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import datetime
import pendulum
import pytz
import uuid
import re
import socket
import smtplib


user_name = input("Enter your User Name: ")
user_name = str(user_name)

def select_user(user_name):
    query = "SELECT * FROM user WHERE username = %(user_name)s"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor(buffered=True)
        cursor.execute(query, { 'user_name': user_name })

    except Error as e:
        print(e)

    finally:
        print(query)
        cursor.close()
        conn.close()

def main():
    select_user(user_name)

if __name__ == '__main__':
    main()