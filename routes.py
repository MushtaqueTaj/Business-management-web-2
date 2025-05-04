from flask import Blueprint, request, render_template, redirect

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to Business Manager!"

@main.route('/customers')
def customers():
    return "Customers list"

@main.route('/sales')
def sales():
    return "Sales list"