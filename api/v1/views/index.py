#!/usr/bin/python3
"""index"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


@app_views.route('/status', methods=['GET'])
def get_status():
    """Return the status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Return the number of each objects by type."""
    stats = {
        "User": storage.count(User),
        "State": storage.count(State),
        "City": storage.count(City),
        "Amenity": storage.count(Amenity),
        "Place": storage.count(Place),
        "Review": storage.count(Review)
    }
    return jsonify(stats)
