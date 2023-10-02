from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = os.getenv("mysql_user")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("mysql_password")
app.config['MYSQL_DATABASE_DB'] = os.getenv("db")
app.config['MYSQL_DATABASE_HOST'] = os.getenv("host")

@app.route("/")
def helloworld():
    name = "demo"
    conn = mysql.connect()
    cursor = conn.cursor()
    command = "insert into demo (name) values (%s)"
    cursor.execute(command,name) 
    conn.commit()
    return str(name + " eklendi")

    return "Second version"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
