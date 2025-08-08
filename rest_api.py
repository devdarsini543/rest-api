from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store users
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# GET: Fetch all users
@app.route("/", methods=["GET"])
def get_users():
    return jsonify(users), 200

# POST: Add a new user
@app.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid data"}), 400
    users.append(data)
    return jsonify({"message": "User added successfully!"}), 201

# PUT: Update user by name
@app.route("/<name>", methods=["PUT"])
def update_user(name):
    data = request.get_json()
    for user in users:
        if user["name"].lower() == name.lower():
            user["age"] = data.get("age", user["age"])
            user["name"] = data.get("name", user["name"])
            return jsonify({"message": f"{name} updated successfully!"}), 200
    return jsonify({"error": "User not found"}), 404

# DELETE: Delete user by name
@app.route("/<name>", methods=["DELETE"])
def delete_user(name):
    for i, user in enumerate(users):
        if user["name"].lower() == name.lower():
            users.pop(i)
            return jsonify({"message": f"{name} deleted successfully!"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
