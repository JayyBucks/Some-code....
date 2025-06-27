from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

app.config["SECRET_KEY"] = "your secret key"

def get_student_data(url:str):
    response = requests.get(url)

    response_json = response.json()
    return response_json
@app.route('/', methods=['GET'])
def index():
    url = 'http://127.0.0.1:5000/api/students/all'

    student_data = get_student_data(url)
    return render_template('index.html', student_data=student_data)
@app.route('/majors', methods=['GET'])
def majors_get():
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)
    major_list = []
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])

        major_list.sort()
    return render_template('majors.html', major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)
    major_list = []
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])

    major_list.sort()
    major = request.form.get('major')
    print(major)
    url =f"http://127.0.0.1:5000/api/majors/{major}"
    result_list = get_student_data(url)
    return render_template('majors.html', major_list=major_list, result_list=result_list)

app.run(port=5001)