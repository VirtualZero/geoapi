from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



# Instantiations
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configurations
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
app.config['GEO_DB_LOCATION'] = 'geoapi/geo_db/GeoLite2-City.mmdb'
app.config['DOWNLOAD_GEO_DB_URL'] = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config['JWT_REFRESH_KEY'] = os.environ['JWT_REFRESH_KEY']

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQL_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Routes
from geoapi.api.routes import api_routes
from geoapi.errors import errors