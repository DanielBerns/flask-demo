from flask import Blueprint

bp = Blueprint('feature_one', __name__)

from . import routes # Import routes

