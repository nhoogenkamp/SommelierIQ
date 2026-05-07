from flask import Flask
from routes.wines import get_tables, get_wines 
from routes.menu import get_food
from routes.senddish import send_dish

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

#get all food from db
@app.route('/getFood', methods=['GET'])
def food_items():
    return get_food()

# getting dish from frontend
@app.route('/senddish', methods=['POST'])
def receive_dish():
    return send_dish()

if __name__ == "__main__":
    print("connecting to DB....")
    app.run(host='0.0.0.0', port=8080)