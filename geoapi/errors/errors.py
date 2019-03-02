from geoapi import app
from flask import jsonify

@app.errorhandler(404)
def error_404(error):
    return jsonify({
        "message": "ERROR: Not Found (404)"
    }), 404


@app.errorhandler(403)
def error_403(error):
    return jsonify({
        "message": "ERROR: Forbidden (403)"
    }), 403


@app.errorhandler(500)
def error_500(error):
    return jsonify({
        "message": "ERROR: Something went wrong. (500)"
    }), 500


@app.errorhandler(405)
def error_405(error):
    return jsonify({
        "message": "ERROR: Invalid request method. (405)"
    }), 405


@app.errorhandler(400)
def error_400(error):
    return jsonify({
        "message": "ERROR: Something was not right about the request. (400)"
    }), 400
