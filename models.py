from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the database object
db = SQLAlchemy()

# Define the User model (for authentication)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Define the Passenger model (for dashboard)
class Passenger(db.Model):
    __tablename__ = 'passengers'  # Optional: Explicitly set the table name

    PassengerId = db.Column(db.Integer, primary_key=True)
    Survived = db.Column(db.Boolean, nullable=False)
    Pclass = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Sex = db.Column(db.String(10), nullable=False)
    Age = db.Column(db.Float, nullable=True)
    SibSp = db.Column(db.Integer, nullable=False)  # Number of siblings/spouses aboard
    Parch = db.Column(db.Integer, nullable=False)  # Number of parents/children aboard
    Ticket = db.Column(db.String(20), nullable=False)
    Fare = db.Column(db.Float, nullable=False)
    Cabin = db.Column(db.String(10), nullable=True)  # Cabin number
    Embarked = db.Column(db.String(1), nullable=True)  # Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

    def __repr__(self):
        return f"<Passenger {self.Name}>"