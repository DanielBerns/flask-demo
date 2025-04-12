from flask import Blueprint

bp = Blueprint('auth', __name__)

# Import routes and forms at the end to avoid circular dependencies
from . import routes, forms

