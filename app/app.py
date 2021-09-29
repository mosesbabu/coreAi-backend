
from flask import Flask, jsonify,request
import json
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)



try:
    connection = mysql.connector.connect(host='localhost',database='coreai',user='root',password='')
    if connection.is_connected():
        SQL = "select id,amount,amount_one,amount_two,amount_three,amount_four,date from dataset;"
        cursor = connection.cursor()
        cursor.execute(SQL)
        #returns sql result
        data = cursor.fetchall()      
        print("fetch result-->",type(data))  #is s list type, need to be a dict

        fields_list = cursor.description   # sql key name
        print("fields result -->",type(fields_list))
        cursor.close()
        connection.close()



   # main function
    column_list = []
    for i in fields_list:
        column_list.append(i[0])
    print("print final column_list",column_list)

        # prints the column list
    jsonData_list = []
    for row in data:
        data_dict = {}
        for i in range(len(column_list)):
            data_dict[column_list[i]] = row[i]
       
        jsonData_list.append(data_dict)
        


    @app.route('/api/retrieve', methods=['GET'])
    def get_data():
        return jsonify({'dataset': jsonData_list})
    
    @app.route('/api/add', methods = ['POST'])
    def create():
   
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

except Error as e:
    print("Error while connecting to Mysql", e)
    
finally:
    connection.close()
    print (" mysql closed")



    if __name__ == '__main__':
        app.run(debug=True)









