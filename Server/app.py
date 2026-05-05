from flask import Flask,jsonify
import mysql.connector


app = Flask(__name__)

con=mysql.connector.connect(
    host='trolley.proxy.rlwy.net',
    port=39957,
    database='railway',
    user='root',
    password='fnKEhqNMePaAhEdEzsEJkhEZNiDgANTw'
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
    app.run(debug=True)
    app.run(host='0.0.0.0', port='8080')
