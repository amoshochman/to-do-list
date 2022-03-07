import os

from flask import Flask, jsonify, request

from my_db import db

app = Flask(__name__)


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_title = db.Column(db.String(100), unique=False, nullable=False)
    task_notes = db.Column(db.String(200), unique=False, nullable=True)
    task_is_done = db.Column(db.Integer, unique=False, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if getattr(self, c.name)}

    def __init__(self, task_title, notes=None):
        self.task_title = task_title
        self.task_is_done = 0
        if notes:
            self.task_notes = notes


@app.route('/tasks', methods=['GET', 'DELETE'])
def existing_tasks():
    if request.method == 'GET':
        return jsonify([task.as_dict() for task in Task.query.all()])
    else:
        return "hello"
        # tasks = Task.query.all()
        # db.session.delete(tasks)


@app.route('/tasks/<task_id>', methods=['GET', 'DELETE'])
def existing_task(task_id):
    if request.method == 'DELETE':
        task = Task.query.filter_by(task_id=task_id).first_or_404()
        db.session.delete(task)
        db.session.commit()
        return "ok"
    else:
        task = Task.query.filter_by(task_id=task_id).first_or_404()
        return jsonify(task.as_dict())


@app.route('/tasks', methods=['POST'])
def new_task():
    task_title = request.form.get('task_title')
    notes = request.form.get('notes')
    task = Task(task_title)
    db.session.add(task)
    db.session.commit()
    return {"task_id": task.task_id}


def create_app(is_test=False):
    db_filename = 'todo' + ('_test' if is_test else '') + '.db'
    path = os.path.join(os.getcwd(), db_filename)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)