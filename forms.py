from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Email, EqualTo



class CadastroUsuarioForm(FlaskForm):
    
    username = StringField (
        'Usuário',
        validators=[DataRequired(), Length(min=2, max=80)])    
    email = StringField (
        'Email',
        validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField (
        'Senha',
        validators=[DataRequired()])
    confirmar_password = StringField (
        'Repita a Senha',
        validators=[DataRequired(),EqualTo('password')])
