# Flask CRUD API

A simple REST API built with Flask, demonstrating full CRUD (Create, Read, Update, Delete) operations on an in-memory user database.

## What this project does

This API manages a small in-memory list of users. It supports:

- **GET** `/users` — retrieve all users
- **POST** `/users` — create a new user
- **PUT** `/users/<id>` — update an existing user's name
- **DELETE** `/users/<id>` — remove a user

A separate `client.py` script demonstrates calling all four operations against the running server using Python's `requests` library.

> Note: data is stored in memory (a Python list), so it resets every time the server restarts. This project is meant to demonstrate REST API and Flask fundamentals, not persistent storage.

## Tech stack

- Python
- Flask
- Requests (for the client)

## Setup

1. Clone this repository and navigate into the project folder:
   ```
   cd flask-crud-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1      # Windows PowerShell
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the server

```
$env:FLASK_APP = "server.py"
flask run --debug
```

The server will start at `http://127.0.0.1:5000`.

## Testing the API

With the server running, open a **second terminal** (keep the server running in the first) and run:

```
python client.py
```

This will call all four operations in sequence and print each response.

## Example requests

**Get all users**
```python
requests.get("http://127.0.0.1:5000/users")
```

**Create a user**
```python
requests.post("http://127.0.0.1:5000/users", json={"name": "Priya"})
```

**Update a user**
```python
requests.put("http://127.0.0.1:5000/users/1", json={"name": "New Name"})
```

**Delete a user**
```python
requests.delete("http://127.0.0.1:5000/users/1")
```

## Status codes used

| Code | Meaning |
|------|---------|
| 200  | Success (GET) |
| 201  | Created (POST) |
| 404  | User not found |

## Possible future additions

- Persist data with a real database (SQL) instead of an in-memory list
- Add input validation
- Convert to FastAPI
