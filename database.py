
try:
    from mysql.connector import IntegrityError
    import mysql.connector
    import logging
except Exception as e:
    print("Some Modules are missing {}".format(e))


def database_connect():
    connection = mysql.connector.connect(host='',
                                         port="",
                                         database='',
                                         user='',
                                         password='')

    if connection.is_connected():
        # db_info = connection.get_server_info()
        # print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        # cursor.execute("select database();")
        # record = cursor.fetchone()
        # print("You're connected to database: ", record)

        return connection, cursor


def create(connection, cursor, query, records):
    # sql_insert_query = (query, records)
    # try:
    cursor.executemany(query, records)
    connection.commit()
    print("\n[+]inserted")
    # id = connection.insert_id()
    post_id = cursor.lastrowid
    return post_id
    # except IntegrityError:
    #     logging.warning("\nfailed to insert values {}".format(records))
    # finally:
    #     cursor.close()


def read(connection, cursor, query):
    sql_select_query = query
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    return records


def update(connection, cursor, query):
    sql_update_query = query
    cursor.execute(sql_update_query)
    update = connection.commit()

    return update


def delete(connection, cursor, query):
    sql_update_query = query
    cursor.execute(sql_update_query)
    delete = connection.commit()

    return delete

