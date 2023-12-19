# app/routes.py
#from app import create_app
from flask import Blueprint, render_template

print('yes right')
#app = create_app()
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def hello():
    print('Nahi re')
    return render_template('index.html')
@main_bp.route('/home')
def test():
    print('yupp')
    return 'welcome to routing'
@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/signup')
def signup():
    return render_template('signup.html')
