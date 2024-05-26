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

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def get_status():
    """Return the status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Return the number of each objects by type."""
    dicta = {}
    for dicta_cls in classes:
        dicta[dicta_cls] = storage.count(classes[dicta_cls])
    return jsonify(dicta)
