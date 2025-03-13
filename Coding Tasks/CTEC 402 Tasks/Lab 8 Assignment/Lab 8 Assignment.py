import logging
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from datetime import datetime
from functools import wraps
import re

app = Flask(__name__)
app.secret_key = 'Th1sis$Strong'

# Set up logging
logging.basicConfig(filename='app.log', level=logging.WARNING,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Load common passwords
with open('CommonPassword.txt', 'r') as file:
    COMMON_PASSWORD = {line.strip() for line in file}

# Dummy user database
users = {'testuser': 'Test@1234'}


# Decorator for protecting routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("You need to log in first!")
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        username = session['username']

        # Validate current password
        if users.get(username) != current_password:
            flash('Current password is incorrect.', 'error')
            return redirect(url_for('update_password'))

        # Validate new password
        if (len(new_password) < 12 or
                not re.search(r'[A-Z]', new_password) or
                not re.search(r'[a-z]', new_password) or
                not re.search(r'\d', new_password) or
                not re.search(r'[!@#$%^&*]', new_password) or
                new_password in COMMON_PASSWORDS):
            flash('New password does not meet security criteria.', 'error')
            return redirect(url_for('update_password'))

        # Update password
        users[username] = new_password
        flash('Password updated successfully!', 'success')
        return redirect(url_for('protected'))

    return render_template('update_password.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('protected'))
        else:
            # Log failed login attempt
            logging.warning(f"Failed login attempt for user: {username}, IP: {request.remote_addr}")
            flash('Invalid username or password. Try again.', 'error')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
