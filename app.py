from flask import Flask, request, Response
import json
import mariadb
import random
import dbcreds

app = Flask(__name__)

# zoo = ["dog", "cat", "lion", "tiger", "elephant", "deer", "monkey", "donkey", "horse", "cow", "mouse"]

def connect():
      return mariadb.connect(
         user = dbcreds.user,
         password = dbcreds.password,
         host = dbcreds.host,
         port = dbcreds.port,
         database = dbcreds.database
    )

     
@app.route('/animals', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def animals():
    if request.method == 'GET':
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM animals")
            result = cursor.fetchall()
            animals=[]
            for item in result:
                animal={
                    "id" : item[0], 
                    "name": item[1]
                    }
                animals.append(animal) 
        except mariadb.OperationalError as ex:
            print("connection problem", ex) 
        except:
            print("error") 
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close() 
                return Response(
                    json.dumps(animals, default=str),
                    mimetype="application/json",
                    status=200
                )                    
       
    elif request.method == 'POST':
        animal = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animals(name) VALUES (?)",[name])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        except:
            print("error")
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()  
                return Response(
                    "mr.snake is added now..",
                     mimetype="text/html",
                     status=201
                )



           
    elif request.method == 'PATCH':
        animal = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE animals SET name=? WHERE id=?", ["name", "id"])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close()
                return Response(
                    "now mr.snake is turned into owl!",
                     mimetype="text/html",
                     status=201
                )             
        
    elif request.method == 'DELETE':
        animal_id = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM animals WHERE id=?", [animal_id])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        except:
            print("error")
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close() 
                return Response(
                     "aww sorry! mouse you are not in zoo now",
                     mimetype="text/html",
                     status=201
                )                
         
    else:
        return Response(
            "something wrong in zoo!!....",
            mimetype="text/html",
            status=401
        )          










# from flask import Flask
# # import json
# import mariadb


# app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return "hello world! dhwani"


# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#        login_dictionary = {"loginToken": "abc123"}
#        return Response(
#          json.dumps(login_dictionary, default=str),
#          mimetype="application/json",
#          status=200
#     )  

#     elif request.method == 'GET':
#         return Response(
#             "welcome to my login form",
#             mimetype="text/html",
#             status=200
#         )