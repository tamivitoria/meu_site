from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    IntegerField
)
from wtforms.validators import DataRequired, Length, Email, EqualTo



class CadastroUsuarioForm(FlaskForm):
    
    name = StringField ('Nome completo', validators=[DataRequired(), Length(min=2, max=80)])
    idade = IntegerField ('Idade', validators=[DataRequired()])
    uf = StringField ('Estado', validators=[DataRequired(), Length(min=2, max=2)])
    cidade = StringField ('Cidade', validators=[DataRequired(), Length(min=2, max=80)])
    username = StringField ('Usuário', validators=[DataRequired(), Length(min=4, max=30)])    
    email = StringField ('Email', validators=[DataRequired(), Email(message="Email invalido"), Length(min=2, max=80)])
    password = PasswordField ('Senha', validators=[DataRequired()])
    confirmar_password = PasswordField ('Repita a Senha', validators=[DataRequired(),EqualTo('password')])
    botao = SubmitField("Cadastrar")   


class CadastroEmpresaForm(FlaskForm):
    
    name = StringField ('Nome da Empresa', validators=[DataRequired(), Length(min=2, max=80)])
    CNPJ = StringField ('CNPJ', validators=[DataRequired(), Length(min=2, max=80)])
    uf = StringField ('Estado', validators=[DataRequired(), Length(min=2, max=80)])
    cidade = StringField ('Cidade', validators=[DataRequired(), Length(min=2, max=80)])
    username = StringField ('Usuário', validators=[DataRequired(), Length(min=4, max=30)])    
    email = StringField ('Email', validators=[DataRequired(), Email(message="Email invalido"), Length(min=2, max=80)])
    password = PasswordField ('Senha', validators=[DataRequired()])
    confirmar_password = PasswordField ('Repita a Senha', validators=[DataRequired(),EqualTo('password')])
    botao = SubmitField("Cadastrar")


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembre-me', validators=[DataRequired()])
    botao = SubmitField("Entrar")
