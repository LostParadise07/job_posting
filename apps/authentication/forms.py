# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField , SelectField
from wtforms.validators import Email, DataRequired, InputRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password',
                                    id='confirm_password_create',
                                    validators=[DataRequired()])
    number = IntegerField('Number',
                            id='number_create',
                            validators=[DataRequired()])
    address = StringField('Address',
                            id='address_create',
                            validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin', 'admin'), ('user', 'user')])
