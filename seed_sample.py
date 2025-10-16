from app import create_app, db
from app.models import User, AidListing
app = create_app()
with app.app_context():
    # check if provider exists
    if not User.query.filter_by(email='provider@example.com').first():
        u = User(name='Provider One', email='provider@example.com', role='provider')
        u.set_password('providerpass')
        db.session.add(u)
        db.session.commit()
        print('Created provider account: provider@example.com / providerpass')
        l = AidListing(title='Food Drive - Bags of maize', category='Food', description='Free maize distributed to vulnerable families', location='Nairobi', posted_by=u.id)
        db.session.add(l)
        db.session.commit()
        print('Added sample listing.')
    else:
        print('Provider already exists.')
