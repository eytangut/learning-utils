import os
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
from functools import wraps


import sqlite3
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()
def login_required(f):
    """
    Decorate routes to require login.
    Copied from CS50 week 9, finance project, from helpers.py
    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form.get('username'))
        print(request.form.get('password'))
        names = cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', (request.form.get('username'), request.form.get('password'))).fetchall()
        thing = cur.execute('SELECT * FROM users WHERE username = ?', (request.form.get('username'),)).fetchall()
        print(names)
        print(thing)
        if len(names) == 1:
            session['user_id'] = names[0][2]
            return redirect('/')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (request.form.get('username'), request.form.get('password')))
        con.commit()
        return redirect('/')
    else:
        return render_template('signup.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
@app.route('/classes', methods=['GET', 'POST'])
@login_required
def classes():
    if request.method == 'POST':
        print(request.form)
        match request.form.get('request_type'):
            case 'create':
                cur.execute('INSERT INTO classes (class_name, user_id) VALUES (?, ?)', (request.form.get('class_name_create'), session['user_id']))
                con.commit()     
                print(request.form.get('class_name_create'))
            case 'delete':
                cur.execute('DELETE FROM classes WHERE class_name = ? AND user_id = ?', (request.form.get('class_name_delete'), session['user_id']))
                con.commit()
            case 'edit_desc':
                cur.execute('UPDATE classes SET class_description = ? WHERE id = ?', (request.form.get('class_desc_edit'), request.form.get('class_id')))
                con.commit()
                print(request.form)
                print(request.form.get('class_desc_edit'))
                print(request.form.get('class_id'))
            case 'delete_link':
                cur.execute('DELETE FROM links WHERE id = ?', (request.form.get('link_id'),))
                con.commit()
                print(request.form.get('link_id'))
            case 'add_link':
                cur.execute('INSERT INTO links (url, class_id) VALUES (?, ?)', (request.form.get('link'), request.form.get('class_id')))
        return redirect('/classes')
    else:
        classes = None
        try:
            classes = cur.execute('SELECT * FROM classes WHERE user_id = ?', (session['user_id'],)).fetchall()
            links = cur.execute('SELECT * FROM links WHERE class_id IN (SELECT id FROM classes WHERE user_id = ?)', (session['user_id'],)).fetchall()
            if links:
                pass
            else:
                links = []        
        except:
            classes = None
        return render_template('classes.html', classes=classes, links=links)

def apology(error, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", error_code=code, error_description=error)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
