from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect MySQL
db = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="databasename"
)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
