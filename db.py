from multiprocessing import connection
import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="personinfodb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def createNewPersonCard(name, age, salary):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = (
                "INSERT INTO `personinfodb`.`personinfo` (`id`, `name`, `age`, `salary`) VALUES (0, %s, %s, %s);"
                ""
            )
            data = (name, age, salary)
            cursor.execute(sql, data)
        connection.commit()
