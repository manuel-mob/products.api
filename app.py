from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
from pymongo import MongoClient
from bson.json_util import dumps, loads 
from bson import BSON
from bson import json_util
import json
import mysql.connector

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'programacion_user'
app.config['MYSQL_PASSWORD'] = 'puser.5858..'
app.config['MYSQL_DB'] = 'products'

# Create a MySQL connection
mysql_conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

cursor = mysql_conn.cursor(dictionary=True)
# Guardians data
guardians = [
    {"name": "Ragnar", "power": 80},
    {"name": "Freya", "power": 75},
    {"name": "Thorin", "power": 100},
    # ... other guardians
]

# API keys (for demonstration purposes)
API_KEYS = {
    "api_key_1": "user_1",
    "api_key_2": "user_2",
}

# Connect to MongoDB
# client = MongoClient(
#     "mongodb://apiproductouser:apiproduct.5858.@localhost:27017/productsapi"
# )
# db = client["productsapi"]
# guardians_collection = db["guardians"]  # Replace with your collection name

# Replace this with your MongoDB query to fetch guardians data
#guardians_data = list(guardians_collection.find())


# Decorator for API key authentication
def requires_api_key(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        api_key = request.headers.get("Api-Key")

        if api_key not in API_KEYS:
            return jsonify({"message": "Unauthorized"}), 401

        return func(*args, **kwargs)

    return decorated

# Route for getting the list of guardians
@app.route("/guardians", methods=["GET"])
@requires_api_key
def get_guardians():
    guardians_data = {}
    return json.dumps(guardians_data, sort_keys=True, indent=4, default=json_util.default)
    return jsonify(dumps(guardians_collection, indent = 2))


# Route for getting the list of products
@app.route("/products", methods=["GET"])
@requires_api_key
def get_products():
    query = "select id,name,brand from product"
    cursor.execute(query)
    guardians = cursor.fetchall()
    return jsonify(guardians)


# Route for getting the list of category
@app.route("/categories", methods=["GET"])
@requires_api_key
def get_categories():
    query = "select id,name,description from category"
    cursor.execute(query)
    guardians = cursor.fetchall()
    return jsonify(guardians)


    return json.dumps(guardians_data, sort_keys=True, indent=4, default=json_util.default)
    return jsonify(dumps(guardians_collection, indent = 2))

if __name__ == "__main__":
    app.run(debug=True)
