"""Routes module for the Flask REST API application."""

from flask import jsonify, request

from app import app

# In-memory storage for items
items = []


@app.route("/api/health", methods=["GET"])
def health_check():
    """Return the health status of the API.

    Returns:
        JSON response indicating the API is healthy.
    """
    return jsonify({"status": "healthy"})


@app.route("/api/items", methods=["GET", "POST"])
def handle_items():
    """Handle GET and POST requests for items.

    GET: Retrieve all items from the storage.
    POST: Create a new item with the provided data.

    Returns:
        JSON response with items list for GET or
        creation confirmation for POST.
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
    """Handle operations on a specific item.

    GET: Retrieve details of a specific item.
    PUT: Update an existing item.
    DELETE: Remove an item from storage.

    Args:
        item_id: The unique identifier of the item.

    Returns:
        JSON response with operation result.
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
