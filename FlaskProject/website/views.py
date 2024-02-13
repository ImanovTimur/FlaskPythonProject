from flask import Blueprint, render_template, request, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/feedback')
def feedback():
    return render_template('feedback.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/organizations')
def organizations():
    return render_template('organizations.html')



