#!/usr/bin/python3
"""app views for Airbnb_clone_v3"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/staus')
def status():
    """returns the status of the app"""
    status = {"status": "ok"}
    return jsonify(status)


@app.views.route('/stats')
def count():
    """returns the number of each objects by type"""
    total = {}
    classes = {"Amenity": "amenities",
            "City": "cities",
            "Place": "place",
            "Reviews": "reviews",
            "State": "states",
            "User": "users"}
    for cls in classes:
        count =storage.count(cls)
        total[classes.get(cls)] = count
    return jsonify(total)
