from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker"},
    {"id": 2, "title": "Build Multi-Tier App"}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

