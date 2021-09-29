from flask import Flask, request, jsonify,abort, make_response
from flask_mysqldb import MySQL
 
 

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coreai'

mysql = MySQL(app)
    
@app.route('/api/retreive', methods = ['GET'])
def index ():
    
    cursor = mysql.connection.cursor()
    cursor.execute(" SELECT * FROM dataset") or []
    data=cursor.fetchall()
    if data:
        return jsonify({
                "data": data
            })
    else:    
        return {},404
  
    
     
@app.route('/api/add', methods = ['POST'])
def create():
    if request.method == 'POST':
        amount = request.json['amount']
        amount_one = request.json['amount_one']
        amount_two = request.json['amount_two']
        amount_three = request.json['amount_three']
        amount_four = request.json['amount_four']
        date = request.json['date']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO dataset VALUES(%s,%s,%s,%s,%s,%s)''',(amount,amount_one,amount_two,amount_three,amount_four,date))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    

if __name__ == '__main__':
   app.run(host='localhost', port=5000)   
 







