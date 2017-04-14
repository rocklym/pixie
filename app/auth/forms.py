from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me in your mind please ^_^')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                                                          'Username must have only letters,numbers or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 64, message='More than 6 bits.'), ])
    password2 = PasswordField('Password', validators=[DataRequired(), Length(6, 64), EqualTo('password',
                              message='Passwords must match.')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use.')

    def validate_usernamel(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
