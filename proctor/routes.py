from proctor import app
from flask import render_template 
from proctor.forms import RegisterForm  

@app.route('/')
def hello_world():
    return 'hello flask framework'

@app.route('/home')
def home_page():
    return 'homepage'


@app.route('/<username>')
def user(username):
    return f'welcome {username}'



@app.route('/base')
def base_page():
    form = RegisterForm()
    return render_template('base.html', form = form)    

# with app.test_request_context():
#     print url_for('user')

# url_for('static', filename= 'style.css')     To generate URLs to that part of the URL,

