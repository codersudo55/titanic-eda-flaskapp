import os
import sys
from flask_testing import TestCase
from werkzeug.security import check_password_hash

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, User, Passenger

class FlaskAppTestCase(TestCase):

    def create_app(self):
        """Create and configure the app for testing."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_titanic.db'  # Use a separate test database
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        return app

    def setUp(self):
        """Set up the test client and initialize the database."""
        db.create_all()

        # Add a test user
        user = User(username='testuser')
        user.set_password('testpassword')
        db.session.add(user)

        # Add test passengers
        passenger1 = Passenger(
            PassengerId=1, Survived=1, Pclass=1, Name='John Doe', Sex='male', Age=30,
            SibSp=0, Parch=0, Ticket='12345', Fare=50.0, Cabin='C123', Embarked='S'
        )
        passenger2 = Passenger(
            PassengerId=2, Survived=0, Pclass=3, Name='Jane Doe', Sex='female', Age=25,
            SibSp=1, Parch=0, Ticket='67890', Fare=20.0, Cabin='E456', Embarked='C'
        )
        db.session.add(passenger1)
        db.session.add(passenger2)

        db.session.commit()

    def tearDown(self):
        """Clean up the database after each test."""
        db.session.remove()
        db.drop_all()

    def test_home_route(self):
        """Test the home route."""
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('login.html')  # Check if the login page is rendered


    def test_login_route(self):
        """Test the login route with valid credentials."""
        # First, create a user
        self.client.post('/signup', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Attempt to log in
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assert200(response)
        self.assertTemplateUsed('dashboard.html')  # Check if redirected to the dashboard

        # Verify the session is set correctly
        with self.client.session_transaction() as session:
            self.assertTrue(session['logged_in'])
            self.assertEqual(session['username'], 'testuser')

    def test_dashboard_route(self):
        """Test the dashboard route when the user is authenticated."""
        # First, create a user and log in
        self.client.post('/signup', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Access the dashboard
        response = self.client.get('/dashboard')
        self.assert200(response)
        self.assertTemplateUsed('dashboard.html')  # Check if the dashboard is rendered

        # Verify the response contains passenger data
        self.assertIn(b'John Doe', response.data)  # Check for passenger name in the response
        self.assertIn(b'Jane Doe', response.data)  # Check for passenger name in the response

        # Log out
        response = self.client.get('/logout', follow_redirects=True)
        self.assert200(response)
        self.assertTemplateUsed('login.html')  # Check if redirected to the login page

        # Verify the session is cleared
        with self.client.session_transaction() as session:
            self.assertNotIn('logged_in', session)

if __name__ == '__main__':
    import unittest
    unittest.main()