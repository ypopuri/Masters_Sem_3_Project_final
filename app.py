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

@app.route('/home', methods =['GET', 'POST'])
def home():
   return render_template('index.html')


@app.route('/login', methods =['GET', 'POST'])  
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        EmailID = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE EmailID = % s AND pasword = % s', (EmailID, password, ))
        Users = cursor.fetchone()
        if Users:
            session['loggedin'] = True
            session['name'] = Users['FirstName']
            session['email'] = Users['EmailID']
            mesage = 'Logged in successfully !'
            return render_template('location.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

@app.route('/location', methods =['GET', 'POST'])
def location():
    mesage = ''
    return render_template('location.html', mesage = mesage)

  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    return render_template('login.html')
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        EmailID = request.form['EmailID']
        Address = request.form['Address']
        Pincode = request.form['Pincode']
        City = request.form['City']
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
        cursor.execute('SELECT * FROM Users WHERE EmailID = % s', (EmailID,))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', EmailID):
            mesage = 'Invalid email address !'
        elif not FirstName:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Users VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)', (FirstName, LastName, EmailID, Address, Pincode, City, Country, password, conpassword))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fil out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/location1', methods =['GET', 'POST'])
def location1():
    mesage = ''
    if request.method == 'POST':
        print("heyy")
        FirstName = request.form['Firstname']
        LastName = request.form['Lastname']
        EmailID = request.form['Email']
        Nopeople = request.form['noperson']
        Travelstartdate = request.form['StartDate']
        Travelenddate = request.form['EndDate']
        Location ='ISTANBUL'
        Paidamount = '2500'
        print(FirstName)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Transactions VALUES (%s, %s, %s, %s, %s, %s,%s, %s)', (FirstName, LastName, EmailID, Travelstartdate, Travelenddate, Location, Nopeople, Paidamount))
        mysql.connection.commit()
        mesage = 'You have successfully added !'
        return render_template('payment.html', mesage = mesage)
    return render_template('location1.html', mesage = mesage)

@app.route('/location2', methods =['GET', 'POST'])
def location2():
    mesage = ''
    if request.method == 'POST':
        print("heyy")
        FirstName = request.form['Firstname']
        LastName = request.form['Lastname']
        EmailID = request.form['Email']
        Nopeople = request.form['noperson']
        Travelstartdate = request.form['StartDate']
        Travelenddate = request.form['EndDate']
        Location ='ISTANBUL'
        Paidamount = '2500'
        print(FirstName)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Transactions VALUES (%s, %s, %s, %s, %s, %s,%s, %s)', (FirstName, LastName, EmailID, Travelstartdate, Travelenddate, Location, Nopeople, Paidamount))
        mysql.connection.commit()
        mesage = ''
        return render_template('payment.html', mesage = mesage)
    return render_template('location2.html', mesage = mesage)

@app.route('/location3', methods =['GET', 'POST'])
def location3():
    mesage = ''
    if request.method == 'POST':
        print("heyy")
        FirstName = request.form['Firstname']
        LastName = request.form['Lastname']
        EmailID = request.form['Email']
        Nopeople = request.form['noperson']
        Travelstartdate = request.form['StartDate']
        Travelenddate = request.form['EndDate']
        Location ='ISTANBUL'
        Paidamount = '2500'
        print(FirstName)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Transactions VALUES (%s, %s, %s, %s, %s, %s,%s, %s)', (FirstName, LastName, EmailID, Travelstartdate, Travelenddate, Location, Nopeople, Paidamount))
        mysql.connection.commit()
        mesage = ''
        return render_template('payment.html', mesage = mesage)
    return render_template('location3.html', mesage = mesage)

@app.route('/location4', methods =['GET', 'POST'])
def location4():
    mesage = ''
    if request.method == 'POST':
        print("heyy")
        FirstName = request.form['Firstname']
        LastName = request.form['Lastname']
        EmailID = request.form['Email']
        Nopeople = request.form['noperson']
        Travelstartdate = request.form['StartDate']
        Travelenddate = request.form['EndDate']
        Location ='ISTANBUL'
        Paidamount = '2500'
        print(FirstName)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Transactions VALUES (%s, %s, %s, %s, %s, %s,%s, %s)', (FirstName, LastName, EmailID, Travelstartdate, Travelenddate, Location, Nopeople, Paidamount))
        mysql.connection.commit()
        mesage = ''
        return render_template('payment.html', mesage = mesage)
    return render_template('location4.html', mesage = mesage)

@app.route('/location5', methods =['GET', 'POST'])
def location5():
    mesage = ''
    if request.method == 'POST':
        print("heyy")
        FirstName = request.form['Firstname']
        LastName = request.form['Lastname']
        EmailID = request.form['Email']
        Nopeople = request.form['noperson']
        Travelstartdate = request.form['StartDate']
        Travelenddate = request.form['EndDate']
        Location ='ISTANBUL'
        Paidamount = '2500'
        print(FirstName)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Transactions VALUES (%s, %s, %s, %s, %s, %s,%s, %s)', (FirstName, LastName, EmailID, Travelstartdate, Travelenddate, Location, Nopeople, Paidamount))
        mysql.connection.commit()
        mesage = ''
        return render_template('payment.html', mesage = mesage)
    return render_template('location5.html', mesage = mesage)

 
@app.route('/transaction', methods =['GET', 'POST'])
def transaction():
    mesage = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print( session['email'])
    cursor.execute('SELECT * FROM Transactions WHERE EmailID = % s', ( session['email'],))
    account = cursor.fetchall()
    print(account)
    return render_template('transaction.html', accountDetials = account)
  
# ADMIN Code

@app.route('/adminhomepage', methods =['GET', 'POST'])
def adminhomepage():
     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        EmailID = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM ADMIN WHERE EmailID = % s AND password = % s', (EmailID, password, ))
        Users = cursor.fetchone()
        if Users:
            session['loggedin'] = True
            session['name'] = Users['FirstName']
            session['email'] = Users['EmailID']
            mesage = 'Logged in successfully !'
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            print( session['email'])
            cursor.execute('SELECT * FROM GUID')
            guideDetails = cursor.fetchall()
            return render_template('adminhomepage.html', mesage = mesage,guideDetails = guideDetails)
        else:
            mesage = 'Please enter correct email / password !'
            return render_template('adminlogin.html', mesage = mesage)
     return render_template('adminhomepage.html')




@app.route('/addguid', methods =['GET', 'POST'])
def addguid():
    mesage = ''
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        EmailID = request.form['EmailID']
        phoneNo = request.form['phoneno']
        Address = request.form['Address']
        Pincode = request.form['Pincode']
        City = request.form['City']
        worklocation = request.form['worklocation']
        Country = request.form['Country']
        print("jhjhj")
        
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
            cursor.execute('INSERT INTO Guid VALUES (%s, %s, %s,%s, %s, %s,%s, %s,%s)', (FirstName, LastName, EmailID,phoneNo, Address, Pincode, City, Country, worklocation))
            mysql.connection.commit()
            mesage = 'You have successfully added !'
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('SELECT * FROM GUID')
            guideDetails = cursor.fetchall()
            return render_template('adminhomepage.html', mesage = mesage,guideDetails=guideDetails)

    elif request.method == 'POST':
        mesage = 'Please fil out the form !'
    return render_template('addguid.html', mesage = mesage)
  
    
    
@app.route('/showguid', methods =['GET', 'POST'])
def showguid():
    mesage = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print( session['email'])
    cursor.execute('SELECT * FROM GUID')
    guideDetails = cursor.fetchall()
    return render_template('adminhomepage.html', guideDetails = guideDetails)
  
    


@app.route('/deleteguid', methods=['GET', 'POST'])
def deleteguid():
    message = ''
    if request.method == 'POST':
        # Fetch the EmailID from the form data
        EmailID = request.form['email']
        print(EmailID)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Perform the DELETE operation
        cursor.execute('DELETE FROM GUID WHERE EmailID = %s', (EmailID,))
        # Commit the changes to the database
        mysql.connection.commit()

    # Fetch the remaining guide details
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM GUID')
    guideDetails = cursor.fetchall()
    
    return render_template('adminhomepage.html', guideDetails=guideDetails)



@app.route('/loginadmin', methods =['GET', 'POST'])
def loginadmin():
   return render_template('adminlogin.html')



# Admin User


    
@app.route('/showUsers', methods =['GET', 'POST'])
def showUsers():
    mesage = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print( session['email'])
    cursor.execute('SELECT * FROM USERS')
    userDetails = cursor.fetchall()
    return render_template('addUserHome.html', userDetails = userDetails)
  



@app.route('/addUser', methods =['GET', 'POST'])
def addUser():
    mesage = ''
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        EmailID = request.form['EmailID']
        Address = request.form['Address']
        Pincode = request.form['Pincode']
        City = request.form['City']
        Country = request.form['Country']
        password = request.form['password']
        conpassword = request.form['conpwd']
        
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE EmailID = % s', (EmailID,))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', EmailID):
            mesage = 'Invalid email address !'
        elif not FirstName:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Users VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)', (FirstName, LastName, EmailID, Address, Pincode, City, Country, password, conpassword))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
            cursor.execute('SELECT * FROM Users')
            
            userDetails = cursor.fetchall()
            print(userDetails)
            return render_template('addUserHome.html', userDetails = userDetails)

    elif request.method == 'POST':
        mesage = 'Please fil out the form !'
    return render_template('adduserDetails.html', mesage = mesage)
   
   
   
@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteuser():
    message = ''
    if request.method == 'POST':
        # Fetch the EmailID from the form data
        EmailID = request.form['email']
        print(EmailID)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Perform the DELETE operation
        cursor.execute('DELETE FROM USERS WHERE EmailID = %s', (EmailID,))
        # Commit the changes to the database
        mysql.connection.commit()

    # Fetch the remaining guide details
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM USERS')
    userDetails = cursor.fetchall()
    
    return render_template('adduserHome.html', userDetails=userDetails)



# feedback Code
  
@app.route('/feedback', methods =['GET', 'POST'])
def feedback():
    mesage = ''
    return render_template('feedback.html', mesage = mesage)



  
@app.route('/submitfeedback', methods =['GET', 'POST'])
def submitfeedback():
    mesage = ''
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        Rating = int(request.form['rating'])
        EmailID = request.form['EmailID']
        Comments = request.form['comments']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # account = cursor.fetchone()
        cursor.execute('INSERT INTO FEEDBACK VALUES (%s, %s, %s,%s)', (FirstName, EmailID, Rating, Comments))
        mysql.connection.commit()
        mesage = 'Feedback submitted succesfully!! !'
    elif request.method == 'POST':
        mesage = 'Please fil out the form !'
    return render_template('user.html', mesage = mesage)




if __name__ == "__main__":
    app.run()