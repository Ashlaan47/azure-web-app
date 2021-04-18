from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'You have been successfully logged in!!'


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == '2020mt93516@wilp' and request.form['username'] == '2020mt93516':
        session['logged_in'] = True
    else:
        flash('Invalid credentials!!Please try again!!')
    return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    flash("You have been successfully logged out!!")
    return home()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
