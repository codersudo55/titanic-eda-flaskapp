# Titanic Dataset Exploratory Data Analysis Flask App

Perform Exploratory Data Analysis for Titanic Dataset using Python and run it as a Flask app.

## Description

In this project, I have designed a Flask App which contains a login functionality. Once you have signed in, you have access to a dashboard which contains graphs obtained after performing Exploratory Data Analysis on Titanic dataset.

## Approach Used
### 1. **User Authentication**
   - A **login system** was implemented to restrict access to the app's features.
   - **Werkzeug**, a utility library for Flask, was used for secure password hashing and verification.
   - User credentials (username and hashed passwords) are stored in a **SQLite database**.
   - Users can register by providing a username and password, which are validated and stored in the database.
   - During login, the provided password is verified against the hashed password using Werkzeug's `check_password_hash` function.


### 2. **Data Loading**
   - The Titanic dataset (`titanic_dataset.csv`) was loaded directly into a **SQLite database** (`titanic.db`) without any preprocessing.
   - Created a seeding script (`seed_db.py`) which seeds data from csv file to the db.
   - The dataset was used as-is to maintain its original structure and values for analysis.


### 3. **Exploratory Data Analysis (EDA)**
   - The dataset was analyzed to uncover patterns and trends related to passenger survival.
   - Four key visualizations were created to derive insights:
     1. **Survival Rate by Gender**: Analyzed the survival rates of male and female passengers.
     2. **Age Distribution by Survival**: Examined the distribution of passenger ages for survivors and non-survivors.
     3. **Survival Rate by Passenger Class**: Explored how survival rates varied across different passenger classes (1st, 2nd, and 3rd class).
     4. **Fare Distribution by Survival**: Investigated the relationship between fare prices and survival rates

### 4. **Flask App Integration**
   - A **Flask web application** was developed to showcase the EDA results interactively.
   - The app includes:
     - A homepage with an overview of the project.
     - Interactive visualizations of the four key graphs.
   - The app is designed to be user-friendly, allowing users to explore the dataset and insights without needing to run code.

### 5. **Database Integration**
   - **SQLite** was chosen as the database for its simplicity and lightweight nature.
   - The database is managed using Flask's `SQLAlchemy` ORM for easy querying and data manipulation.

### 6. **Deployment**
   - The Flask app is containerized using **Docker** for easy deployment.
   - It can be deployed locally or on cloud platforms like Heroku, AWS, or Google Cloud.
   - I have used `Render` - a free cloud service to upload my dashboard - ([@Live Website URL](https://codersudo55-titanic-flaskapp.onrender.com))

## Observations
Based on the visualizations, the following insights were derived:

1. **Survival Rate by Gender**:
   - Female passengers had a significantly higher survival rate compared to male passengers.
   - This suggests that gender played a critical role in determining survival, likely due to the "women and children first" protocol during the evacuation.

2. **Age Distribution by Survival**:
   - Younger passengers (children) had a higher survival rate compared to older passengers.
   - The age distribution of survivors was skewed toward younger ages, indicating that children were prioritized during the rescue.

3. **Survival Rate by Passenger Class**:
   - Passengers in **1st class** had the highest survival rate, followed by 2nd class and then 3rd class.
   - This indicates that socio-economic status (as represented by passenger class) influenced survival chances, with higher-class passengers having better access to lifeboats.

4. **Fare Distribution by Survival**:
   - Survivors tended to have paid higher fares compared to non-survivors.
   - This further supports the correlation between socio-economic status and survival, as higher fares were associated with better accommodations and proximity to lifeboats.


## Getting Started

### Dependencies

* Python 3.9+ (I have used Python 3.13)
* virtualenv (venv) for running it locally
* Libraries - Flask, SQLAlchemy, numpy, pandas, plotly

### Installing

* Python Installation - https://www.python.org/downloads/
* Microsoft Visual Studio Code Installation (IDE to run your code locally and for Source Control operations) -  https://code.visualstudio.com/download 

## How to Run Flask App Locally

1. Clone the repository and open the project folder:
```
$ git clone https://github.com/codersudo55/titanic-eda-flaskapp.git
```

2. Install `virtualenv`:
```
$ pip install virtualenv
```
2. Open a terminal in the project root directory and run:
```
$ virtualenv venv
```
3. Then run the command:
```
$ .\venv\Scripts\activate
```
4. Then install the dependencies:
```
$ (venv) pip install -r requirements.txt
```
5. First run the script to seed csv data to database:
```
$ (venv) python seed_db.py
```
6. Finally start the web server:
```
$ (venv) python app.py
```
This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

### Author 
Sudarshan Srinivasan ([@codersudo55](https://www.github.com/codersudo55))

