from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

tasks = [
    {"id": 1, "title": "Learn Docker"},
    {"id": 2, "title": "Build Multi-Tier App"}
]

@main.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)
