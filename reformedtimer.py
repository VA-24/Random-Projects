from flask import Flask, render_template, request, flash
import datetime
import time

app = Flask(__name__)
app.secret_key = 'xyz'
timers = []

@app.route('/')
def home():
    now = datetime.datetime.now()
    return render_template('index.html', timers=timers, now=now)

@app.route('/add_timer', methods=['POST'])
def add_timer():
    start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%dT%H:%M')
    timers.append({'start_date': start_date, 'name': request.form['name']})
    return home()

app.run()