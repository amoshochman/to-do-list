import os

from flask import Flask, jsonify, request

from database import db

app = Flask(__name__)


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_title = db.Column(db.String(100), unique=False, nullable=False)
    task_is_done = db.Column(db.Integer, unique=False, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if getattr(self, c.name) is not None}

    def __init__(self, task_title):
        self.task_title = task_title
        self.task_is_done = 0


@app.route('/tasks', methods=['GET', 'DELETE', 'POST'])
def tasks_id_not_provided():
    if request.method == 'GET':
        return jsonify([task.as_dict() for task in Task.query.all()])
    elif request.method == 'DELETE':
        tasks = Task.query.all()
        for task in tasks:
            db.session.delete(task)
        db.session.commit()
        return "all items were removed"
    else:
        task_title = request.form.get('task_title')
        task = Task(task_title)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.as_dict())


@app.route('/tasks/<task_id>', methods=['GET', 'DELETE'])
def tasks_id_yes_provided(task_id):
    task = Task.query.filter_by(task_id=task_id).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify(task.as_dict())
    else:
        return jsonify(task.as_dict())


@app.route('/tasks/done/<task_id>', methods=['PUT'])
def mark_task_as_done(task_id):
    task = Task.query.filter_by(task_id=task_id).first_or_404()
    task.task_is_done = 1
    db.session.commit()
    return jsonify(task.as_dict())


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
