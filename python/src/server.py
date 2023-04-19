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
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT email, password FROM user WHERE email = %s", (auth.username,))
    if res>0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]
        if auth.username != email or auth.password != password:
            return "Invalid credentails", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "Invalid credentails", 401
    

def createJWT(username, secret, authz):
    return jwt.encode({"username": username,
                       "exp": datetime.datetime.now(tz=datetime.timezone.utc)+ datetime.timedelta(days=1),
                       "iat":datetime.datetime.utcnow(),
                       "admin": authz},
                       secret,
                       algorithm= "HS256",
        )

if __name__ == "__main__":
    
    server.run(host="0.0.0.0", port="5000")