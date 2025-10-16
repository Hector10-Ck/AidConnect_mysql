from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# ----------------------------
# USER MODEL
# ----------------------------
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='beneficiary')

    # Relationships
    listings = db.relationship('AidListing', backref='poster', lazy=True)
    requests = db.relationship('Request', backref='requester', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# ----------------------------
# AID LISTING MODEL
# ----------------------------
class AidListing(db.Model):
    __tablename__ = 'aid_listings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    posted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship
    requests = db.relationship('Request', backref='listing', lazy=True)


# ----------------------------
# REQUEST MODEL
# ----------------------------
class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey('aid_listings.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)


# ----------------------------
# LOGIN MANAGER
# ----------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

