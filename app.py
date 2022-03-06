from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    notes = db.Column(db.String(200), unique=False, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if getattr(self, c.name)}

    def __init__(self, title, notes=None):
        self.title = title
        if notes:
            self.notes = notes


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
        task = Task.query.filter_by(id=task_id).first_or_404()
        db.session.delete(task)
        db.session.commit()
        return "ok"
    else:
        return "in get by id..."


@app.route('/tasks', methods=['POST'])
def new_task():
    title = request.form.get('title')
    notes = request.form.get('notes')
    task = Task(title, notes)
    db.session.add(task)
    db.session.commit()
    return "task succesfully added, id: " + str(task.id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)