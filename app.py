from flask import Flask, request, Response
import json
import mariadb
import random


app = Flask(__name__)
zoo = ["dog", "cat", "lion", "tiger", "elephant", "deer", "monkey", "donkey", "horse", "cow", "mouse"]

@app.route('/animals', methods = ['GET', 'POST', 'UPDATE', 'DELETE'])
def animals():
    if request.method == 'GET':
        return Response(
            json.dumps(zoo, default=str),
            mimetype="application/json",
            status=200
        )
    elif request.method == 'POST':
        return Response(
            "mr.snake is added now..",
             mimetype="text/html",
             status=201
        )   
    elif request.method == 'PATCH':
        return Response(
            "now mr.snake is turned into owl!",
             mimetype="text/html",
             status=201
        )
    elif request.method == 'DELETE':
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