import csv
import sqlite3
from sqlite3 import Error

from flask import Flask, render_template,request
app = Flask(__name__)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "QuizShehzad.db"

    sql_create_vehicle_table = """ CREATE TABLE IF NOT EXISTS Vehicles (
                                        Name text,
                                        Vehicle text,
                                        Grade integer,
                                        Room integer,
                                        Telnum integer,
                                        Picture text,
                                        Keywords text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create Vehicle table
        create_table(conn, sql_create_vehicle_table)
        readcsvinsertdata(conn)
    else:
        print("Error! cannot create the database connection.")


def readcsvinsertdata(conn):
    with open('People.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            conn.execute("INSERT INTO Vehicles (Name,Vehicle,Grade,Room,Telnum,Picture,Keywords) VALUES (?,?,?,?,?,?,?)", (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        conn.commit()

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/vehicles')
def vehiclename():
    con = sqlite3.connect("QuizShehzad.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Vehicles')
    rows = cur.fetchall()
    print(len(rows))
    print(rows)
    return render_template("original.html", rows=rows)

@app.route('/original')
def original():
   return render_template('original.html')

if __name__ == '__main__':
   main()
   app.run(debug=True)


# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#    if request.method == 'POST':
#       try:
#          nm = request.form['nm']
#          addr = request.form['add']
#          city = request.form['city']
#          pin = request.form['pin']
         
#          with sql.connect("database.db") as con:
#             cur = con.cursor()
            
#             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
#             con.commit()
#             msg = "Record successfully added"
#       except:
#          con.rollback()
#          msg = "error in insert operation"
      
#       finally:
#          return render_template("result.html",msg = msg)
#          con.close()

# @app.route('/list')
# def list():
#    con = sql.connect("database.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from students")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)

