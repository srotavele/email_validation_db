from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from ..models.email import User


@app.route('/')
def index():
    addresses = User.get_all()
    return render_template('index.html', all_email = addresses)

@app.route('/process/', methods = ['POST'])
def add_email():
    if not User.validate_address(request.form):
        return redirect('/')
    else:
        if User.validate_address(request.form):
            flash(f"the email address entered ({request.form['email']}) is a VALID address. Thank you!")
    
    emails = User.add_email(request.form)
    return redirect('/entry/results')
    
@app.route('/entry/results')
def show_entries():
    emails = User.get_entry()
    return render_template('success.html', all_email = emails)

@app.route('/entry/delete/<int:user_id>')
def delete_entry(user_id):
    User.delete_entry({'id': user_id})
    return redirect('/entry/results')
