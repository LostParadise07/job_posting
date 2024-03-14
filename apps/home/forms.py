from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import  DataRequired

class ADDJOBFORM(FlaskForm):
    company_name = StringField('Company Name',
                            id='company_name',
                            validators=[DataRequired()])
    job_title = StringField('Job Title',
                            id='job_title',
                            validators=[DataRequired()])
    job_description = StringField('Job Description',
                            id='job_description',
                            validators=[DataRequired()])
    job_location = StringField('Job Location',
                            id='job_location',
                            validators=[DataRequired()])
    job_salary = StringField('Job Salary',
                            id='job_salary',
                            validators=[DataRequired()])
    job_type = StringField('Job Type',
                            id='job_type',
                            validators=[DataRequired()])
    job_category = StringField('Job Category',
                            id='job_category',
                            validators=[DataRequired()])
    job_experience = StringField('Job Experience',
                            id='job_experience',
                            validators=[DataRequired()])
    job_qualification = StringField('Job Qualification',
                            id='job_qualification',
                            validators=[DataRequired()])
    job_skills = StringField('Job Skills',
                            id='job_skills',
                            validators=[DataRequired()])
    job_posted = StringField('Job Posted',
                            id='job_posted',
                            validators=[DataRequired()])
    job_deadline = StringField('Job Deadline',
                            id='job_deadline',
                            validators=[DataRequired()])
    job_status = StringField('Job Status',
                            id='job_status',
                            validators=[DataRequired()])
    featured_job = SelectField('Featured Job',
                            choices=[('Yes', 'yes'), ('No', 'No')])
    url = StringField('URL',
                            id='url',
                            validators=[DataRequired()])