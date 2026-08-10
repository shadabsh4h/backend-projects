# Importing requests to send the CRUD operations

import requests

# Connecting to this server 
BASE_URL = "http://127.0.0.1:5000"

# To read the data from the server
def get_users():
    response = requests.get(f"{BASE_URL}/users")
    print(response.status_code)
    print(response.json())

# To add a new user in our memory based database
def create_user(name):
    response=requests.post(f"{BASE_URL}/users", json={"name": name})
    print(response.status_code)
    print(response.json())

# To update the existing data
def update_user(user_id, name):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json={"name": name})
    print(response.status_code)
    print(response.json())

# To remove the user from the memory based database
def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    # call the function as per the requires request
    get_users()
    create_user("Priya")
    update_user(name="Stark",user_id=1)
    delete_user(3)