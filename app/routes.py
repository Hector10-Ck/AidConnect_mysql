from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User, AidListing, Request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    listings = AidListing.query.order_by(AidListing.created_at.desc()).all()
    return render_template('index.html', listings=listings)

@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'beneficiary')
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please login.', 'warning')
            return redirect(url_for('main.login'))
        user = User(name=name, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', 'info')
    return redirect(url_for('main.index'))

@bp.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    # Provider can post listings
    if current_user.role == 'provider' and request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        location = request.form['location']
        desc = request.form['description']
        listing = AidListing(title=title, category=category, location=location, description=desc, posted_by=current_user.id)
        db.session.add(listing)
        db.session.commit()
        flash('Listing posted', 'success')
        return redirect(url_for('main.dashboard'))

    # show listings (provider sees their listings; beneficiary sees all)
    if current_user.role == 'provider':
        my_listings = AidListing.query.filter_by(posted_by=current_user.id).order_by(AidListing.created_at.desc()).all()
    else:
        my_listings = AidListing.query.order_by(AidListing.created_at.desc()).all()
    return render_template('dashboard.html', listings=my_listings)

@bp.route('/listing/<int:id>', methods=['GET','POST'])
@login_required
def listing_detail(id):
    listing = AidListing.query.get_or_404(id)
    if request.method == 'POST':
        # beneficiary requests aid
        msg = request.form.get('message','')
        req = Request(user_id=current_user.id, listing_id=listing.id, message=msg)
        db.session.add(req)
        db.session.commit()
        flash('Request submitted', 'success')
        return redirect(url_for('main.listing_detail', id=listing.id))
    # fetch requests for providers
    listing_requests = []
    if current_user.role == 'provider' and listing.posted_by == current_user.id:
        listing_requests = Request.query.filter_by(listing_id=listing.id).all()
    return render_template('listing_detail.html', listing=listing, requests=listing_requests)
