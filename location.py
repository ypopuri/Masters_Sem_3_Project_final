# import the flask class
from flask import Flask, session, render_template, request,make_response,redirect,flash
from flask import Flask, redirect, url_for, render_template, request, abort
from flaskext.mysql import MySQL
# instatiating flask class 
app=Flask(__name__)

mysql = MySQL()
 
# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'    
app.config['MYSQL_DATABASE_PASSWORD'] = 'Y@shu1234'
app.config['MYSQL_DATABASE_DB'] = 'Project'  
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#initialise mySQL
mysql.init_app(app)
#create connection to access data
conn = mysql.connect()
