"""Flask application package initialization."""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import routes after app initialization to avoid circular imports
from app import routes  # noqa: F401, E402
