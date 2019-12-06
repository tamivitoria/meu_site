from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroUsuarioForm, CadastroEmpresaForm, LoginForm
from flask_login import LoginManager, login_user


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_site.db'
app.config['SECRET_KEY'] = "fghjklçlkjhgtrrghjklpiuytr"
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    uf = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return "[User: %r]" % self.username

class Empresa(db.Model):
    CNPJ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    uf = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return "[User: %r]" % self.username 




@app.route ("/index")
@app.route ("/home")
@app.route ("/")
def index():
    return render_template("index.html")



@app.route ("/login", methods=["GET", "POST"])
def login():
   
    return render_template("login.html", form=form)


@app.route ("/cadastro/usuario", methods=["GET", "POST"])
def cadastroUsuario():
    form = CadastroUsuarioForm()

    if form.validate_on_submit():
        novo_usuario= Usuario(name=form.name.data, idade=form.idade.data, uf=form.uf.data, cidade=form.cidade.data, username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(novo_usuario)
        db.session.commit()
        
    return render_template("cadastroUsuario.html", form=form)


@app.route ("/cadastro/empresa", methods=["GET", "POST"])
def cadastroEmpresa():
    form = CadastroEmpresaForm()

    if form.validate_on_submit():
        nova_empresa= Empresa(name=form.name.data, CNPJ=form.CNPJ.data, uf=form.uf.data, cidade=form.cidade.data, username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(nova_empresa)
        db.session.commit()
        
    return render_template("cadastroEmpresa.html", form=form)




if __name__ == ('__main__'):
   app.run(debug=True)
