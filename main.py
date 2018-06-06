from flask import Flask, render_template, request
app = Flask(__name__)

import csv
with open('People.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    names =[]
    vehicles =[]
    grades =[]
    rooms =[]
    telephones =[]
    pictures =[]
    keywords =[]
    for row in readCSV:
        name = row[0]
        vehicle =row[1]
        grade =row[2]
        room =row[3]
        telephone =row[4]
        picture =row[5]
        keyword =row[6]

        names.append(name)
        vehicles.append(vehicle)
        grades.append(grade)
        rooms.append(room)
        telephones.append(telephone)
        pictures.append(picture)
        keywords.append(keyword)

    print(names)
    print(vehicles)
    print(grades)
    print(rooms)
    print(telephones)
    print(pictures)
    print(keywords)

    # now, remember our lists?

    # whatColor = input('What color do you wish to know the date of?:')
    # coldex = colors.index(whatColor)
    # theDate = dates[coldex]
    # print('The date of',whatColor,'is:',theDate)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/original')
def original():
   return render_template('original.html')

if __name__ == '__main__':
   app.run(debug = True)

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

