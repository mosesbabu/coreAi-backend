
from flask import Flask, jsonify,request
import json
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)



try:
    #establish connection to mysql server
    connection = mysql.connector.connect(host='localhost',database='coreai',user='root',password='')
    if connection.is_connected():
        SQL = "select id,amount,amount_one,amount_two,amount_three,amount_four from amount;"
        
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
    
    connection = mysql.connector.connect(host='localhost',database='coreai',user='root',password='')
    if connection.is_connected():
        SQL = "select id,date,date_one,date_two,date_three,date_four from dates;"
        
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
    date_list = []
    for i in fields_list:
        date_list.append(i[0])
    print("print final date_list",date_list)
    
    

        # prints the column list
    jsonDate_list = []
    for row in data:
        data_dict = {}
        for i in range(len(date_list)):
            data_dict[date_list[i]] = row[i]
       
        jsonDate_list.append(data_dict)
    #api endpoint route to create retreive all dataset records from the db
    @app.route('/api/retrieve', methods=['GET'])
    def get_data():
        return jsonify({'dataset': jsonData_list, 'label':jsonDate_list})
    
    #api endpoint route to create dataset record and save to db
    
    @app.route('/api/add', methods = ['POST'])
    def create():
        data_id=request.json['id']
        amount = request.json['amount']
        amount_one = request.json['amount_one']
        amount_two = request.json['amount_two']
        amount_three = request.json['amount_three']
        amount_four = request.json['amount_four']
        date = request.json['date']
        connection = mysql.connector.connect(host='localhost',database='coreai',user='root',password='')
        cursor = connection.cursor()
        cursor.execute(''' INSERT INTO dataset VALUES(%s,%s,%s,%s,%s,%s,%s)''',(data_id,amount,amount_one,amount_two,amount_three,amount_four,date))
        connection.commit()
        connection.close()
        return f"success!!"
    #api endpoint route to delete dataset record
    
    @app.route('/api/delete/<id>', methods=['DELETE'])
    def delete_data(id):
        connection = mysql.connector.connect(host='localhost',database='coreai',user='root',password='')
        SQL = "DELETE FROM dataset WHERE id=id ;"
        cursor = connection.cursor()
        cursor.execute(SQL)
        cursor.close()
        connection.close()

        
        
        
        return f"Done!!"
    

except Error as e:
    print("Error while connecting to Mysql", e)
finally:
    connection.close()
    print (" mysql closed")



    if __name__ == '__main__':
        app.run(debug=True)









