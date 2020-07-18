from header import *
import mysql.connector
from mysql.connector import Error


class clsDbConnection:
    try:
        con = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='flask_tutorial', port='3309')
        if con.is_connected():
            print('Database connected')
    except Error as ex:
        print("Can not connect database :", ex)

    # this function use for update and save data to database
    def save(self, sql):
        try:
            cmd = clsDbConnection.con.cursor()
            cmd.execute(sql)
            clsDbConnection.con.commit()
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            print("Error {}".format(error))
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close

    def update(self, sql):
        try:
            cmd = clsDbConnection.con.cursor()
            cmd.execute(sql)
            clsDbConnection.con.commit()
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            print("Error {}".format(error))
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close

    # this function use for delete data from database
    def delete(table_name, field_id, field_value):
        try:
            cmd = clsDbConnection.con.cursor()
            cmd.execute("delete from " + table_name + " where " + field_id + "='" + field_value + "'")
            clsDbConnection.con.commit()
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            print("Error {}".format(error))
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close


