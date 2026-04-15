from flask import Flask, jsonify, request, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Create Database tables within the application context
with app.app_context():
    db.create_all()

# --- SWAGGER/OPENAPI CONFIG ---
template = {
    "openapi": "3.0.0",
    "info": {
        "title": "Task Manager API",
        "version": "1.1.0",
        "description": "Enterprise-ready CRUD API using Flask-SQLAlchemy and SQLite."
    }
}
swagger = Swagger(app, template=template)

# --- GLOBAL ERROR HANDLERS ---
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error.description)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "The requested task does not exist"}), 404

# --- CRUD ROUTES ---

@app.route('/')
def index():
    return redirect('/apidocs/')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks from the database"""
    all_tasks = Task.query.all()
    output = [{"id": t.id, "title": t.title, "done": t.done} for t in all_tasks]
    return jsonify({"tasks": output}), 200

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task by ID"""
    task = Task.query.get_or_404(task_id)
    return jsonify({"id": task.id, "title": task.title, "done": task.done}), 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    if not request.json or 'title' not in request.json:
        abort(400, description="Payload must contain a 'title' field.")
    
    new_task = Task(title=request.json['title'], done=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title, "done": new_task.done}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task"""
    task = Task.query.get_or_404(task_id)
    
    if not request.json:
        abort(400, description="No data provided for update.")

    task.title = request.json.get('title', task.title)
    task.done = request.json.get('done', task.done)
    
    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "done": task.done}), 200

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Remove a task from the database"""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    # use_reloader=False prevents double-initialization issues with DB and Swagger
    app.run(debug=True, port=5000, use_reloader=False)