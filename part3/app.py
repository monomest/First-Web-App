# -----------------------------------------------------------------
# File: app.py 
# Author: Renee Lu & Arthur Sze
# Last Revised: 11 November 2020
# -----------------------------------------------------------------
# This code runs a website on the local machine (http://localhost:5000))
# and contains the Title page, full list of students and marks, and individual student marks
# 
# ------------------------------------------------------------------

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/studentlist' ,methods=['GET', 'POST'])
def studentlist():
    with open('../part1/student-data.json') as f:
        data = json.load(f)
    name = ""

    # Search by student name
    if request.method == 'POST':
        filtered_names = {}
        fields = ['studentname', 'studentmark']
        name = request.form['searchbox']
        for x in data.items():
            if name.lower() in data[x[0]]['studentname'].lower():
                # Student class object derived from part 1 udp_client.py
                # Make a new list and add the filtered students to it
                current_student = {}
                current_student[fields[0]] = data[x[0]]['studentname']
                current_student[fields[1]] = data[x[0]]['studentmark']
                filtered_names[data[x[0]]['studentname']] = current_student
        return render_template('studentlist.html', data = filtered_names, name = name)

    # Show full student list
    return render_template('studentlist.html', data = data, name = name)



# webpage to show specified student's marks
@app.route('/api/studentmark/<name>', methods = ['GET', 'POST'])
def studentmark(name):
    with open('../part1/student-data.json') as f:
        data = json.load(f)

    for x in data.items():
        if name == data[x[0]]['studentname']:
            mark = data[x[0]]['studentmark']
            break

    return render_template('studentmark.html', name = name, mark = mark)


if __name__ == "__main__":
    app.run(debug = True, port = 5000)