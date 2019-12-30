# ---- THIRD PARTY IMPORTS ----
import os, shutil

# pylint: disable=F0401
from flask import Blueprint, request, make_response, current_app as app
import mysql.connector

# Register flask blueprint
dbhelper_blueprint = Blueprint('dbhelper', __name__)

config = {
    'user': 'spec-sim',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'spec-sim'
}
connection = mysql.connector.connect(**config)

@dbhelper_blueprint.route('/initDB', methods=['GET'])
def initializeDatabase(): 
  cursor = connection.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS test (uuid INT);')
  # results = [{name: color} for (name, color) in cursor]
  cursor.close()
  connection.close()

  return 'initDB'

@dbhelper_blueprint.route('/dropDB', methods=['GET'])
def dropDatabase():
  return 'dropDB'