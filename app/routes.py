from flask import jsonify, request

from app import app

# In-memory storage for items
items = []


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint to verify API status"""
    return jsonify({"status": "healthy"})


@app.route("/api/items", methods=["GET", "POST"])
def handle_items():
    """
    Handle items endpoint:
    - GET: Retrieve all items
    - POST: Create a new item
    """
    if request.method == "GET":
        return jsonify({"items": items})

    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    new_item = {"id": len(items) + 1, "name": data["name"]}
    items.append(new_item)
    return jsonify({"message": "Item created", "item": new_item}), 201


@app.route("/api/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
def handle_item(item_id):
    """
    Handle specific item operations:
    - GET: Retrieve item details
    - PUT: Update item
    - DELETE: Remove item
    """
    item = next((item for item in items if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    if request.method == "GET":
        return jsonify({"item": item})

    elif request.method == "PUT":
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "Invalid request data"}), 400

        item["name"] = data["name"]
        return jsonify({"message": "Item updated", "item": item})

    elif request.method == "DELETE":
        items.remove(item)
        return jsonify({"message": "Item deleted"})
