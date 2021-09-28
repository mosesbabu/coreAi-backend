from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
 
 

app = Flask(__name__)
mysql = MySQL(app)
    
@app.route('/api', methods = ['POST', 'GET'])
def index ():
    if request.method == 'GET':
        return "Login via the login Form"
     
@app.route('/api/add', methods = ['POST'])
def create():
    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO dataset VALUES(%s,%s)''',(amount,date))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)   
 







