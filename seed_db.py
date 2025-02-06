# Script to seed Titanic csv data into the SQLite database
import pandas as pd
from app import app  
from models import db, Passenger

def seed_database():
    # Load the Titanic dataset
    df = pd.read_csv("titanic_dataset.csv")

    # Create tables and insert data (to avoid duplicate entries)
    with app.app_context():
        # db.drop_all()  #  Drop all tables
        # db.create_all() # Recreate them
        # Clear only the Passenger table
        Passenger.query.delete()
        db.session.commit()

        # Insert data into the database
        for _, row in df.iterrows():
            passenger = Passenger(
                PassengerId=row['PassengerId'],
                Survived=bool(row['Survived']),
                Pclass=row['Pclass'],
                Name=row['Name'],
                Sex=row['Sex'],
                Age=row['Age'],
                SibSp=row['SibSp'],
                Parch=row['Parch'],
                Ticket=row['Ticket'],
                Fare=row['Fare'],
                Cabin=row['Cabin'],
                Embarked=row['Embarked']
            )
            db.session.add(passenger)
        db.session.commit()

if __name__ == "__main__":
    seed_database()