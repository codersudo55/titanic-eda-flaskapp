# Titanic Dataset Exploratory Data Analysis Flask App

Perform Exploratory Data Analysis for Titanic Dataset using Python and run it as a Flask app.

## Description

In this project, I have designed a Flask App which contains a login functionality. Once you have signed in, you have access to a dashboard which contains graphs obtained after performing Exploratory Data Analysis on Titanic dataset.

## Getting Started

### Dependencies

* Python 3.9+ (I have used Python 3.13)
* virtualenv (venv) for running it locally
* Libraries - Flask, SQLAlchemy, numpy, pandas, plotly

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### How to Run Flask App Locally
1. Install `virtualenv`:
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
5. Finally start the web server:
```
$ (venv) python app.py
```
This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)


## Author
Sudarshan Srinivasan

