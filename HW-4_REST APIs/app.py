from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 
app.config['SECRET_KEY'] = "namleislearningflask"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False # make it so that it doesn't track, so doesn't show tracking error

db = SQLAlchemy(app) #Flask app connects to a db using SQLAlchemy

# Make a 'Milks' Class to store milk data
class Milks(db.Model):
    id = db.Column(db.Integer, primary_key = True)    # Auto-incrementing ID
    name = db.Column(db.String(50))
    flavor = db.Column(db.String(50))

    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor

    # Decorator to add aditional function to Class without modifying it
    # Return object data in easily serializable format to be used later!

    # without a serialize function, it's difficult to return db items as JSON list.
    # research: https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json 
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'flavor': self.flavor
        }

# create / use the database
with app.app_context():
  db.create_all()

#____________________________________ API stuff bellow here_________________________________________#


# Create route to RECIEVE json data with POST method, add to db, commit, then return the jsonify'd version of the db
@app.post('/add_milk')
def add_milk():
    name = request.json['name']
    flavor = request.json['flavor']

    new_milk = Milks(name, flavor)

    db.session.add(new_milk)
    db.session.commit()

# Create var 'latest_milk' to store the query of the latest item added, then return jsonify'd of the serialized query
    latest_milk = Milks.query.order_by(Milks.id.desc()).first()
    return jsonify(latest_milk.serialize)


# Create a route that RETURNS milks API (from db) with GET method, with content-type: "application/json"
@app.get('/api/milks')
def api_milks():
  # return db query results as a JSON list
  return jsonify([milk.serialize for milk in Milks.query.all()])

if __name__ == "__main__":
    app.run(debug=True)