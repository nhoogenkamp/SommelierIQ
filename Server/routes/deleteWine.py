from flask import request, jsonify
from db import get_db_connection

def add_wine():
    