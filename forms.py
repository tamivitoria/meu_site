from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Email, EqualTo



class CadastroUsuarioForm(FlaskForm):
    

    nome_completo = StringField (
        'Nome Completo',
        validators=[DataRequired(), Length(min=2, max=80)])
    data_nascimento = StringField (
        'Data de Nascimento',
        validators=[DataRequired(), Length(min=2, max=80)])
    uf = StringField (
        'Estado',
        validators=[DataRequired(), Length(min=2, max=80)])
    cidade = StringField (
        'Cidade',
        validators=[DataRequired(), Length(min=2, max=80)])
    username = StringField (
        'Usuário',
        validators=[DataRequired(), Length(min=4, max=30)])    
    email = StringField (
        'Email',
        validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField (
        'Senha',
        validators=[DataRequired()])
    confirmar_password = StringField (
        'Repita a Senha',
        validators=[DataRequired(),EqualTo('password')])
    


class CadastroEmpresaForm(FlaskForm):
    

    nome_completo = StringField (
        'Nome da Empresa',
        validators=[DataRequired(), Length(min=2, max=80)])
    CNPJ = StringField (
        'CNPJ',
        validators=[DataRequired(), Length(min=2, max=80)])
    uf = StringField (
        'Estado',
        validators=[DataRequired(), Length(min=2, max=80)])
    cidade = StringField (
        'Cidade',
        validators=[DataRequired(), Length(min=2, max=80)])
    username = StringField (
        'Usuário',
        validators=[DataRequired(), Length(min=4, max=30)])    
    email = StringField (
        'Email',
        validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField (
        'Senha',
        validators=[DataRequired()])
    confirmar_password = StringField (
        'Repita a Senha',
        validators=[DataRequired(),EqualTo('password')])
    


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me', validators=[DataRequired()])