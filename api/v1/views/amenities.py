#!/usr/bin/python3
"""amenities"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities/', methods=['GET'])
def get_all_amenities():
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    return jsonify({})


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data:
        abort(400)
    if 'name' not in data:
        abort(400)
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())
