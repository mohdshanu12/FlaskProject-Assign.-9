from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Programmings',
        'description': 'C,Java, Javascript,Nodejs', 
        'done': True
    },
    {
        'id': 2,
        'title': 'Python Programming',
        'description': 'Best Learning book of Python and boost the skills', 
        'done': False
    }
]

@app.route("/home")
def hello_world():
    return "Hello, Welcome to Home Page"

@app.route("/add-info", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-info")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
