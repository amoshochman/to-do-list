from flask import Flask, jsonify
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
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, title, notes=None):
        self.title = title
        if notes:
            self.notes = notes

@app.route('/tasks')
def post_task():
    return jsonify([task.as_dict() for task in Task.query.all()])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)