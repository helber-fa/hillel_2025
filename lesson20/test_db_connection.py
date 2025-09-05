import psycopg2
import pytest


@pytest.fixture(scope="session")
def open_close_connection():
    dbname = 'hillel_2025'
    user = 'admin'
    password = 'admin'
    host = 'localhost'
    port = '5432'

    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cursor = connection.cursor()
    print("connected successfully")
    yield connection, cursor
    cursor.close()
    connection.close()
    print("disconnected successfully")


def test_connection(open_close_connection):
    connection, cursor = open_close_connection
    table_name = "public.users"
    name_value = "Orest"
    cursor.execute(f"""insert into {table_name} ("name") values ('{name_value}')""")
    cursor.execute(f"""select * from {table_name} where name = \'{name_value}\'""")

    record = cursor.fetchone()
    assert len(record) > 0
    print("You are connected to - ", record)

    cursor.execute(f"""delete from {table_name} where name = \'{name_value}\'""")
    connection.commit()

def test_version(open_close_connection):
    connection, cursor = open_close_connection
    cursor.execute("SELECT version();")



