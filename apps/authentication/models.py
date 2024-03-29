# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)
    number = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(64))
    role = db.Column(db.String(64), default='user')


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)
    
class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    company_name = db.Column(db.String(64))
    job_title = db.Column(db.String(64))
    job_description = db.Column(db.String(64))
    job_location = db.Column(db.String(64))
    job_salary = db.Column(db.String(64))
    job_type = db.Column(db.String(64))
    job_category = db.Column(db.String(64))
    job_experience = db.Column(db.String(64))
    job_qualification = db.Column(db.String(64))
    job_skills = db.Column(db.String(64))
    job_posted = db.Column(db.String(64))
    job_deadline = db.Column(db.String(64))
    job_status = db.Column(db.String(64))
    featured_job = db.Column(db.Boolean, default=False)
    url=db.Column(db.String(64))



@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None
