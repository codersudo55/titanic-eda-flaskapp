# Titanic Dataset EDA Flask App
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Passenger
import plotly.express as px
import pandas as pd

app = Flask(__name__)
app.secret_key = '\x0e\xab\xc1\xfd\x94&NaG\xe1\x83\xc03_\xfe\xack\xa1B\x16\xb7\xd5OR'  # Required for session management (os.urandom(24))

# DB Component declaration for users and passengers
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///titanic.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Home Page
@app.route('/')
def home():
    # If the user is already logged in, redirect to the dashboard
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


# Sign Up Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username already exists
        if User.query.filter_by(username=username).first():
            return render_template('signup.html', error='Username already exists')

        # Create a new user
        new_user = User(username=username)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('signup.html')


# Login Page
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['logged_in'] = True
        session['username'] = username  # Store username in session
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Invalid username or password')



# Dashboard Page
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in before allowing access to the dashboard
    if 'logged_in' in session and session['logged_in']:
        # Query data from the database
        passengers = Passenger.query.all()
        
        # Convert the data to a Pandas DataFrame for easier analysis
        data = [{
            'PassengerId': p.PassengerId,
            'Survived': p.Survived,
            'Pclass': p.Pclass,
            'Name': p.Name,
            'Sex': p.Sex,
            'Age': p.Age,
            'SibSp': p.SibSp,
            'Parch': p.Parch,
            'Ticket': p.Ticket,
            'Fare': p.Fare,
            'Cabin': p.Cabin,
            'Embarked': p.Embarked
        } for p in passengers]
        df = pd.DataFrame(data)
        
        # Create Plotly graphs
        # 1. Survival Rate by Gender
        survival_by_gender = px.pie(
            df, names='Sex', color='Survived',
            title='Survival Rate by Gender',
            labels={'Sex': 'Gender', 'Survived': 'Survived'}
        )

        # 2. Age Distribution by Survival
        age_distribution = px.histogram(
            df, x='Age', color='Survived',
            title='Age Distribution by Survival',
            labels={'Age': 'Age', 'Survived': 'Survived'},
            nbins=20
        )

        # 3. Survival Rate by Passenger Class
        survival_by_class = px.box(
            df, x='Pclass', color='Survived',
            title='Survival Rate by Passenger Class',
            labels={'Pclass': 'Passenger Class', 'Survived': 'Survived'}
        )

        # 4. Fare Distribution by Survival
        fare_distribution = px.box(
            df, x='Survived', y='Fare',
            title='Fare Distribution by Survival',
            labels={'Survived': 'Survived', 'Fare': 'Fare'}
        )
        
        # Convert graphs to HTML
        graph1 = survival_by_gender.to_html(full_html=False)
        graph2 = age_distribution.to_html(full_html=False)
        graph3 = survival_by_class.to_html(full_html=False)
        graph4 = fare_distribution.to_html(full_html=False)


        return render_template(
            'dashboard.html',
            passengers=passengers,
            graph1=graph1,
            graph2=graph2,
            graph3=graph3,
            graph4=graph4
        )
    
    else:
        return redirect(url_for('home'))

# Logout Page (inside dashboard page)
@app.route('/logout')
def logout():
    # Clear the session and log the user out
    # session.pop('logged_in', None)
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Create the database tables (if they don't exist)
    with app.app_context():
        db.create_all() # Create all tables (User and Passenger)
    app.run(debug=True)