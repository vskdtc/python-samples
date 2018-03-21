from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT id_urn FROM user WHERE email='abc49@gmail.com' ")
        rows = cursor.fetchone()
        rows = str(rows).replace("('","")
        rows = str(rows).replace("',)","")
        print(rows)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone()
