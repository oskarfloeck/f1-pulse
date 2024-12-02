#-----------------------------------------------------------------------------#
# test_user_auth.py										  				      #
# Here we test user behavior and various edge cases.                          #
#-----------------------------------------------------------------------------#

from app import db, create_app
from app.models import User
import pytest
import datetime

@pytest.fixture
def app():
    test_app = create_app()
    with test_app.app_context():
        db.create_all()
        yield test_app
        db.drop_all()

#-----------------------------------------------------------------------------#

def test_create_user(app):
    with app.app_context():
        # Create user
        current_time = datetime.datetime.now(datetime.timezone.utc)
        user = User(username='jrek1', email='jrek@mail.com', password='password123', user_type=0, acc_created=current_time, acc_last_modified =current_time)
        db.session.add(user)
        db.session.commit()

        # Assert that the user was created with expected data
        assert user.username == 'jrek1'
        assert user.email == 'jrek@mail.com'
        assert user.acc_created is not None  # Check if timestamp is set
        assert user.acc_last_modified is not None  # Check if timestamp is set

        # Query the user from the database
        u = User.query.filter_by(username='jrek1').first()
        assert u is not None  # User should exist in the DB
        assert u.username == 'jrek1'
        assert u.email == 'jrek@mail.com'

        # (Debug) Print queried user details for confirmation
        print(f"Queried User: {u.username}, Email: {u.email}, Created: {u.acc_created}, Modified: {u.acc_last_modified}")


