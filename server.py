'''
Importing from flask:
Flask- To create server/app object.
request- Let server read incoming data.
jsonify- To convert pyhton dcitionary inti json format.
'''
from flask import Flask,request,jsonify

# Creating app object or server using Flask.
app=Flask(__name__)

# Creating a python dictionary as a database that 
# lives in memory when server .
# It only works when the server is running .
users=[
    {"id":1,"name":"Rahul"},
    {"id":2,"name":"Xavier"},
    {"id":3,"name":"Ali"}
]

# The first endpoint- homepage .
@app.route("/")
def root():
    return "Hello, Welcome to my Rest API project"

'''
Second endpoint- Client can make get and post request.
get- returns the databse.
post- adds new data to our memory based database  
sent by the client in json format.
'''
@app.route("/users",methods=["GET","POST"])
def user_info():
    if request.method=="GET":
        return jsonify(users),200
    elif request.method=="POST":
        new_user=request.get_json()
        new_user["id"]=len(users)+1
        users.append(new_user)
        return jsonify(new_user),201

'''
Third endpoint- Client can update the existing data using unique_id ,
here it is "id" in our database.
'''
@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data=request.get_json()

    for user in users:
        if user["id"]==user_id:
            user["name"]=data["name"]
            return jsonify(user)
    
    return jsonify({"message":f"User {user_id} not found"}),404

'''
Fouth endpoint- Cliend can delete the existing data from the
memory based database
'''
@app.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"]==user_id:
            users.remove(user)
            return jsonify({"message":f"User {user_id} deleted"})
    return jsonify({"message":f"User {user_id} not found"}),404