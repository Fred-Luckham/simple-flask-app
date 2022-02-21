# Imports
from flask import (
    Flask,
    request,
    render_template,
    redirect,
)
from flask_sqlalchemy import SQLAlchemy

##########################
## Define the app and db ##
###########################

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, email):
        self.pname = pname
        self.email = email

###################
## Define routes ##
###################

# The landing page. This will inherit from the base.html template
@app.route('/')
def home():
    return render_template("index.html")

# A basic about page
@app.route('/about')
def about():
    return render_template('about.html')

# The input page
@app.route("/addperson")
def addperson():
    return render_template("addperson.html")

# Database input logic
@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    email = request.form["email"]
    entry = People(pname, email)
    db.session.add(entry)
    db.session.commit()

    return render_template("addperson.html")

# Display the "people" table as a html table
@app.route("/display")
def display():
    #select all people from people
    people=db.session.execute("SELECT * FROM people order by id")
    # render template to display the all people
    return render_template("display.html", people=people)  
