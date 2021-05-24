import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
cur = conn.cursor() 
cur.execute(''' ''')
print("")   
conn.commit()    
conn.close()




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

# def insert_data():
#     conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
#     cur = conn.cursor()
#     # to insert data
#     cur.execute('''INSERT INTO demo (Name, Color, Age) VALUES ('Kuro','Black',2);''')
#     print("Data Added to Database")
#     conn.commit()
#     conn.close()

# To take input from user
def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
    cur = conn.cursor()
    # to insert data from input
    name = input("What is the name of your sheep?")
    color = input("What color is your sheep?")
    age = input("How old is your sheep?")

    query = '''INSERT INTO demo (Name, Color, Age) VALUES (%s,%s,%s);'''
    cur.execute(query,(name,color,age))
    print("You're sheep's data has been saved.")
    conn.commit()
    conn.close()

insert_data()