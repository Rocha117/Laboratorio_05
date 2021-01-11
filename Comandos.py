import psycopg2
import hashlib
import random


def hashF():
    num = str(random.randint(1, 10000))
    hnum = hashlib.sha224(num.encode()).hexdigest()

    return hnum


def Crear_tabla(tabla):
    conn = None
    sql = f"""CREATE TABLE {tabla} (
      id SERIAL PRIMARY KEY,
      CodigoHash VARCHAR,
      Nombre VARCHAR NOT NULL,
      Apellido VARCHAR NOT NULL)"""

    try:
        conn = psycopg2.connect(host="localhost",

                                database="BaseHuella",

                                user="postgres",

                                password="a",

                                port="5432")

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()


def añadir(tabla, codigo, nombre, apellido):
    conn = None
    sql = f"""INSERT INTO {tabla} (CodigoHash, Nombre,Apellido) VALUES(%s, %s,%s);"""

    try:
        conn = psycopg2.connect(host="localhost",

                                database="BaseHuella",

                                user="postgres",

                                password="a",

                                port="5432")

        cur = conn.cursor()
        cur.execute(sql, (codigo, nombre, apellido))
        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()


def Buscar(codigo):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",

                                database="BaseHuella",

                                user="postgres",

                                password="a",

                                port="5432")

        cur = conn.cursor()
        tabla="Huella"
        cur.execute(f"SELECT * FROM {tabla} WHERE CodigoHash = %s", (codigo,))
        usuario = cur.fetchone()
        conn.commit()
        cur.close()
        return usuario
    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()


def MostrarTodo(tabla):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",

                                database="BaseHuella",

                                user="postgres",

                                password="a",

                                port="5432")

        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {tabla};")
        u = cur.fetchall()
        print(u)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()
