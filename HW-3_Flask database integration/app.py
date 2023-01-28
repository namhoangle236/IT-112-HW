from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 
app.config['SECRET_KEY'] = "namleislearningflask"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False # make it so that it doesn't track, so doesn't show tracking error

db = SQLAlchemy(app) #Flask app connects to a db using SQLAlchemy

class Milks(db.Model):
    id = db.Column('milk_id', db.Integer, primary_key = True)    # Auto-incrementing ID
    name = db.Column(db.String(50))
    flavor = db.Column(db.String(50))
    color = db.Column(db.String(50))
    pasteurize = db.Column(db.String(50))

    def __init__(self, name, flavor, color):
        self.name = name
        self.flavor = flavor
        self.color = color
        self.pasteurize = pasteurize

# create / use the database
with app.app_context():
  db.create_all()

# route to index page
@app.route('/')
def index():
    # create a 'milks' variable to store all the Milks class's query, then pass it to index.html as 'milks'
    return render_template('index.html', milks = Milks.query.all())

# make add function to add new milks
@app.route('/add', methods=['POST'])
def add():
    # Put data received from html form in the 'Milks' class (to it's attributes), then assign to a 'milk' variable to be added to database
    milk = Milks(name=request.form.get('name'), flavor=request.form.get('flavor'), color=request.form.get('color'), pasteurize=request.form.get('pasteurize'))
    # Add and commit the data to the database
    db.session.add(milk)
    db.session.commit()
    # Flash a message to notify successful addition
    flash('New milk has been added!')
    # Redirect back to the index, but now with new database items added
    return redirect(url_for('index'))

# make route to detail page to display more info about milk
@app.route('/detail')   # methods should be GET, since it's a hyperlink to the detail page
def detail():
    name = request.args.get('name')
    flavor = request.args.get('flavor')
    color = request.args.get('color')
    pasteurize = request.args.get('pasteurize')

    return f'Milk name: {name}, flavor: {flavor}, color: {color}, is pasteurized: {pasteurize}'
    
# Note: better way to get a single record: Milks.query.filter_by(id=2).first(), check info:
# https://www.youtube.com/watch?v=JKoxrqis0Co&list=PLA5mOwB4xQtSldcetzUYWYEKSEQ5cDIo6&index=12

    
if __name__ == "__main__":
    app.run(debug=True)