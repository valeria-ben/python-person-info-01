import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection
