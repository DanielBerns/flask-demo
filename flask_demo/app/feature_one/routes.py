from flask import render_template, flash
from flask_login import login_required # Maybe this feature requires login
from . import bp # Import the blueprint instance

@bp.route('/')
@login_required # Example: This feature requires login
def feature_home():
    flash("Welcome to Feature One!", "success")
    return render_template('feature_one/feature_page.html', title='Feature One')

