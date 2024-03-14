# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps import db, login_manager
from flask import render_template, request , url_for
from flask_login import login_required ,current_user
from jinja2 import TemplateNotFound
from apps.home.forms import ADDJOBFORM
from apps.authentication.models import Jobs


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/jobs')
@login_required
def jobs():
    jobs = Jobs.query.all()
    return render_template('home/Jobs.html', jobs=jobs)


@blueprint.route('/add_jobs', methods=['POST', 'GET'])
@login_required
def add_jobs():
    form = ADDJOBFORM()
    if form.validate_on_submit():
        featured_job_data=form.featured_job.data
        if(featured_job_data=="Yes"):
            featured_job=True
        else:
            featured_job=False
        url_data=form.url.data
        # if url contains https:// remove that
        if(url_data.startswith('https://')):
            url_data=url_data[8:]
        
        add_job = Jobs(
            user_id = current_user.id,
            company_name=form.company_name.data,
            job_title=form.job_title.data,
            job_description=form.job_description.data,
            job_location=form.job_location.data,
            job_salary=form.job_salary.data,
            job_type=form.job_type.data,
            job_category=form.job_category.data,
            job_experience=form.job_experience.data,
            job_qualification=form.job_qualification.data,
            job_skills=form.job_skills.data,
            job_posted=form.job_posted.data,
            job_deadline=form.job_deadline.data,
            job_status=form.job_status.data,
            featured_job=featured_job,
            url=url_data
        )
        # Add the job to the database session
        db.session.add(add_job)
        db.session.commit()
        # Redirect to a success page or render a success message
        return render_template('home/add_jobs.html', segment='add_jobs', form=form, msg="Job Added Successfully")
    return render_template('home/add_jobs.html', segment='add_jobs', form=form)


@blueprint.route('/edit_jobs')
@login_required
def edit_jobs():
    return render_template('home/edit_jobs.html', segment='edit_jobs')

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
