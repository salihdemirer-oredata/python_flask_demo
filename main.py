# from flask import Flask,render_template, request
# from flask_mysqldb import MySQL
# import os
 
# app = Flask(__name__)
 
# app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
# app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
# app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
# app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
 
# mysql = MySQL(app)
 
# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
 
# app.run(host='localhost', port=8080)


# ---
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define MySQL connection parameters
db_config = {
 "host": "10.248.64.3",
 "user": "test",
 "password": "test",
 "database": "test",
}

@app.route("/")
def index():
 try:
     # Establish a connection to the MySQL database
     conn = mysql.connector.connect(**db_config)
     cursor = conn.cursor()

     # Execute a query to fetch data from a table (replace 'your_table_name' with the actual table name)
     query = "SELECT * FROM info_table"
     cursor.execute(query)

     # Fetch all the results
     results = cursor.fetchall()

     # Render an HTML template with the data
     return render_template("index.html", data=results)

 except mysql.connector.Error as err:
     return f"Error: {err}"

 finally:
     cursor.close()
     conn.close()

if __name__ == "__main__":
 app.run(debug=True)