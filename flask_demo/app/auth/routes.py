# app/auth/routes.py
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from . import bp # Import the blueprint instance
from .forms import LoginForm, SignupForm
from ..models import User
from ..extensions import db # Import db from extensions

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) # Redirect logged-in users

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome back, {user.email}!', 'success')

        # Redirect to the page the user was trying to access, or the main index
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
@login_required # Ensure user is logged in to log out
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index')) # Redirect to home page after logout

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login')) # Redirect to login after successful signup

    return render_template('auth/signup.html', title='Sign Up', form=form)

