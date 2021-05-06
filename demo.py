import psycopg2

def create():
    #  connect to a database. go to psql and get the info you need
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
    # create cursor
    cur = conn.cursor()
    # once cursor is created, to create a table
    cur.execute('''CREATE TABLE demo(ID serial, Name text, Color text, Age int);''')
    print("Table Created")
    # to save it
    conn.commit()
    # close the connection
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
    cur = conn.cursor()
    # to insert data
    cur.execute('''INSERT INTO demo (Name, Color, Age) VALUES ('Kuro','Black',2);''')
    print("Data Added to Database")
    conn.commit()
    conn.close()

insert_data()