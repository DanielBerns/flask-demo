from flask import render_template, flash
from flask_login import login_required, current_user
from . import bp # Import the blueprint instance

@bp.route('/')
@bp.route('/index')
def index():
    # Example: Pass some data to the template
    posts = [{'author': {'email': 'test@example.com'}, 'body': 'Beautiful day!'}]
    return render_template('main/index.html', title='Home', posts=posts)

@bp.route('/profile')
@login_required # Protect this route
def profile():
    # You can access the logged-in user via current_user
    flash(f"This is the profile page for {current_user.email}.", 'info')
    return render_template('main/profile.html', title='Profile') # Create profile.html if needed

