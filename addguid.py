from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)

app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Y@shu1234'
app.config['MYSQL_DB'] = 'Project'
  
mysql = MySQL(app)
  
@app.route('/')
@app.route('/adminhomepage', methods =['GET', 'POST'])
def home():
   return render_template('adminhomepage.html')


@app.route('/addguid', methods =['GET', 'POST'])
def addguid():
    mesage = ''
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        EmailID = request.form['EmailID']
        Address = request.form['Address']
        Pincode = request.form['Pincode']
        City = request.form['City']
        worklocation = request.form['worklocation']
        Country = request.form['Country']
        password = request.form['password']
        conpassword = request.form['conpwd']
        print(FirstName)
        print(LastName)
        print(EmailID)
        print(Address)
        print(Pincode)
        print(City)
        print(Country)
        print(password)
        print(conpassword)
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Guid WHERE EmailID = % s', (EmailID,))
        account = cursor.fetchone()
        if account:
            mesage = 'Guid  already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', EmailID):
            mesage = 'Invalid email address !'
        elif not FirstName:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Guid VALUES (%s, %s, %s,%s, %s, %s,%s, %s,%s, %s)', (FirstName, LastName, EmailID, Address, Pincode, City, Country, worklocation,password, conpassword))
            mysql.connection.commit()
            mesage = 'You have successfully added !'
    elif request.method == 'POST':
        mesage = 'Please fil out the form !'
    return render_template('addguid.html', mesage = mesage)
    
if __name__ == "__main__":
    app.run()