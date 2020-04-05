from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quote.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tandnrthekqatb:2c1cc388bea6e6dbf35dd85c2824e618d7201a67d3ba5db1191b7360b4175dcc@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d7clifad508e0s'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route("/")
def index():
    result = Favquotes.query.all()
    return render_template("index.html",result=result)

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/process",methods=['post'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for("index"))