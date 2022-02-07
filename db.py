from multiprocessing import connection
import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection
