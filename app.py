from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USER = {
    "email": "dan_deadman@live.co.uk",
    "password": "@user827ey2u",
    "name": "John Doe",
    "dob": "1999-05-15",
    "phone": "+1 234 567 8901",
    "address": "1234 Elm Street, Houston, TX, USA"
}

@app.route('/')
def index():
    if session['user']:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == USER['email'] and password == USER['password']:
            session['user'] = USER  # store user data in session
            flash('Login successful!', 'success')
            return redirect(url_for('/'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if session['user']:
        return render_template('profile.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)