from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.Integer, default=0)
    acc_created = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    acc_last_modified = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc), onupdate=datetime.datetime.now(datetime.timezone.utc))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_username(cls, username):
        """
        Retrieve a user by their username.
        
        :param username: Username to search for
        :return: User object if found, None otherwise
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        """
        Retrieve a user by their email.
        
        :param email: Email to search for
        :return: User object if found, None otherwise
        """
        return cls.query.filter_by(email=email).first()

    @classmethod
    def create_user(cls, username, email, password, user_type=0):
        """
        Create a new user in the database.
        
        :param username: Username for the new user
        :param email: Email for the new user
        :param password: Password for the new user
        :param user_type: User type (default is 0)
        :return: Newly created User object
        :raises ValueError: If username or email already exists
        """
        if cls.get_by_username(username):
            raise ValueError("Username already exists")
        
        if cls.get_by_email(email):
            raise ValueError("Email already exists")
        
        new_user = cls(username=username, email=email, user_type=user_type)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user

    @classmethod
    def authenticate(cls, username_or_email, password):
        """
        Authenticate a user by username/email and password.
        
        :param username_or_email: Username or email of the user
        :param password: Password to check
        :return: User object if authenticated, None otherwise
        """
        # Try to find user by username first
        user = cls.query.filter_by(username=username_or_email).first()
        
        # If not found, try by email
        if not user:
            user = cls.query.filter_by(email=username_or_email).first()
        
        # Check password
        if user and user.check_password(password):
            return user
        
        return None

    def update_profile(self, **kwargs):
        """
        Update user profile information.
        
        :param kwargs: Keyword arguments of fields to update
        :return: Updated User object
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        # Update last modified timestamp
        self.acc_last_modified = datetime.datetime.now(datetime.timezone.utc)
        
        db.session.commit()
        return self

    def delete(self):
        """
        Delete the current user from the database.
        """
        db.session.delete(self)
        db.session.commit()
