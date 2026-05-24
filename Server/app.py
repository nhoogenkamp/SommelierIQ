from flask import Flask
from routes.wines import get_tables, get_wines , get_all_wines
from routes.menu import get_food
from routes.senddish import send_dish
from routes.admin import add_admin, login_admin
from routes.addwine import add_wine
from routes.deleteWine import delete_wine
from routes.updateWine import update_wine
from routes.availableWine import available_wine


from flask_cors import CORS
# Ran into CORS error:
#https://www.google.com/search?q=from+flask_cors+import+cors&oq=from+flask_cors+import+CORS&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyCAgBEAAYFhgeMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yDQgHEAAYhgMYgAQYigUyBwgIEAAY7wUyBwgJEAAY7wXSAQcyNzBqMGo5qAIGsAIB8QX1TVs-UXY3Vg&sourceid=chrome&ie=UTF-8

app = Flask(__name__)
CORS(app)

# https://www.newline.co/@goatandsheep/python-dotenv-managing-your-environment-variables-with-ease--ce4fb62d
# Using .env file to store secret password etc.

@app.route('/getTable', methods=['GET'])
def tables():
    return get_tables()

#get wines from db
@app.route('/getWines', methods=['GET'])
def wines():
    return get_wines()

@app.route('/getallWines', methods=['GET'])
def all_wines():
    return get_all_wines()

#get all food from db
@app.route('/getFood', methods=['GET'])
def food_items():
    return get_food()

# getting dish from frontend
@app.route('/senddish', methods=['POST'])
def receive_dish():
    return send_dish()

@app.route('/addAdmin', methods=['POST'])
def create_admin():
    return add_admin()

@app.route('/adminLogin', methods=['POST'])
def admin_login():
    return login_admin()

@app.route('/addWine', methods=['POST'])
def new_wine():
    return add_wine()

@app.route('/deleteWine', methods=['DELETE'])
def deleting_wine():
    return delete_wine()

@app.route('/updateWine', methods=['PUT'])
def updating_wine():
    return update_wine()

@app.route('/availableWine', methods=['PUT'])
def updating_available_wine():
    return available_wine()

if __name__ == "__main__":
    print("connecting to DB....")
    app.run(host='0.0.0.0', port=8080)