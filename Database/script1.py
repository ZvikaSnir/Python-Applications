import psycopg2
import config as cfg

def create_table():
    conn = psycopg2.connect("dbname={} user={} password={} host={}  port={}".format(cfg.psql['db'],cfg.psql['user'],cfg.psql['pass'],cfg.psql['host'],cfg.psql['port']))
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gamer123' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gamer123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gamer123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gamer123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
# insert("Orange",10,15)
# delete("Orange")
update(20,4.2,"Apple")
print(view())
