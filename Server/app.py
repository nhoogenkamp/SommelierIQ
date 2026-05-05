from flask import Flask,jsonify
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# https://www.newline.co/@goatandsheep/python-dotenv-managing-your-environment-variables-with-ease--ce4fb62d
# Using .env file to store secret password etc.
con=mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)
@app.route('/getTable', methods=['GET'])
def get_tables():
    cursor=con.cursor()
    cursor.execute("SHOW TABLES;")
    tables=cursor.fetchall()
    cursor.close()
    con.close()
    table_names=[table[0] for table in tables]
    return jsonify({"tables":table_names}),200


if __name__=="__main__":
    print("connecting to DB....")
    app.run(host='0.0.0.0', port=8080)
