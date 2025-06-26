import flask
from flask import request, jsonify
import student_generator_v2 as sg

app = flask.Flask(__name__)

app.config["DEBUG"] = True

"""
Function to query the studnet dictionaries based on a search key
Input: searchkey
Output: list of results
"""
def search_student_data(search_value,search_key):
    print(f"Search key: {search_key}")
    print(f"Search value: {search_value}")
    student_dictionaries = sg.get_student_dictionaries()
    results_list = []
    for student in student_dictionaries:
        if search_value.lower() == student[search_key].lower():
            results_list.append(student)

    return results_list
@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is JayyBucks </h1>"

@app.route('/api/students/all', methods=['GET'])
def api_all():
   
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

@app.route('/api/majors/<string:major>', methods=['GET'])
def api_student_by_major(major:str):
    major_students = search_student_data(major, "major")
    return jsonify(major_students)

@app.route("/api/students/<string:id>", methods=['GET'])
def api_student_by_id(id:str):
    student_dictionaries = sg.get_student_dictionaries()
    target_student = None
    for student in student_dictionaries:
        if student['id'] == id:
            target_student = student
            break
    return jsonify(target_student)

@app.route('/api/students/class/<string:class_rank>', methods=['GET'])
def api_student_by_class(class_rank:str):
    print(class_rank)
    api_student_by_class = search_student_data(class_rank, 'class')
    return jsonify(api_student_by_class)

app.run()