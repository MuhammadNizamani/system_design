import jwt, datetime, os
from flask import Flask, Request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)
server.config["MY_SQL"] = os.environ.get("MY_SQL") 
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER") 
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD") 
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB") 
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT") 


@server.route("/login", methods =['POST'])
def login ():
    auth = Request.authorization
    if not auth:
        return "missing credentails", 401