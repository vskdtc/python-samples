from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import datetime
import pendulum
import pytz
import uuid
import re
import socket
import smtplib
import socket
import cpuinfo
import getpass
import pymysql


info = cpuinfo.get_cpu_info()
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
userID = getpass.getuser()
get_uuid = uuid.getnode()
modified_by = 'user ID: ' + userID + ', host ID: ' + str(get_uuid) + ', computer name: '+ hostname + ', ip address: ' + host_ip

db = pymysql.connect("localhost","root","","DB3" )
cursor = db.cursor()


email_address = input("Enter your E-Mail address: ")
user_name = str(email_address)

addressToVerify = email_address
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
if match == None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')

def validate_email(addressToVerify):
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    host = socket.gethostname()
    server = smtplib.SMTP()
    server.set_debuglevel(0)
    server.connect(mxRecord)
    server.helo(host)
    server.mail('vskdtc@gmail.com')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()
    time.sleep(1)
    print(domain)
    return code


def utcnow():
    return datetime.datetime.now(tz=pytz.utc)
created_date = utcnow().isoformat()
lastupdated_date = created_date

currentDT = pendulum.now().isoformat()

lz_now = pendulum.now('America/Los_Angeles')
offset_utc = lz_now.offset/3600

def query_id_urn(user_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True)
        sql = "SELECT id_urn FROM user WHERE email = %(user_name)s"
        cursor.execute(sql, {'user_name': user_name})
        id_urn = cursor.fetchone()
        id_urn = str(id_urn).replace("('","")
        id_urn = str(id_urn).replace("',)","")
        return(id_urn)

    except Error as e:
        print(e)
    finally:
        #cursor.close()
        conn.close()
        
def query_created_date(user_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True)
        sql = "SELECT created_date FROM user WHERE email = %(user_name)s"
        cursor.execute(sql, {'user_name': user_name})
        created_date = cursor.fetchone()
        created_date = str(created_date).replace("('","")
        created_date = str(created_date).replace("',)","")
        return(created_date)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

id_urn = query_id_urn(user_name)

if id_urn == 'None':
    id = uuid.uuid1()
    id_urn = id.urn.replace("urn:uuid:","")
else:
    id_urn = id_urn
    created_date = query_created_date(user_name)
    

def insert_user(username, email, id_urn, created_date, lastupdated_date, time_zone, modified_by):
    query = "INSERT INTO user(username,email,id_urn,created_date,lastupdated_date,time_zone,modified_by)" \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    args = (user_name,email,id_urn,created_date,lastupdated_date,time_zone,modified_by)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
            print(lz_now)
            print(offset_utc)
            print(currentDT)
            print(hostname)
            print(get_uuid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
    insert_user(user_name,addressToVerify, id_urn, created_date, lastupdated_date, currentDT, modified_by)

if __name__ == '__main__':
    main()