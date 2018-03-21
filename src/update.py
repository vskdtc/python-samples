from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import datetime
import pytz

def utcnow():
    return datetime.datetime.now(tz=pytz.utc)
created_date = utcnow().isoformat()
lastupdated_date = str(created_date)

def update_user(user_id, email, lastupdated_date):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE user SET email = %s, lastupdated_date = %s WHERE user_id = %s """

    data = (email, lastupdated_date, user_id)

    try:
        conn = MySQLConnection(**db_config)

        # update
        cursor = conn.cursor()
        cursor.execute(query, data)

        print("executed")

        # accept
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    update_user(135, 'abc25_1@gmail.com', lastupdated_date)