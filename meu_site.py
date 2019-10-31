from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroForm()

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_site.db'
app.config['SECRET_KEY']
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username
        









@app.route ("/")
def index():
    return render_template("index.html")

@app.route ("/login")
def login():
    return render_template("login.html")

@app.route ("/cadastro")
def cadastro():
    form = CadastroForm()
    return render_template("cadastro.html")

if (__name__) == ("__main__"):
    app.run(debug=True)