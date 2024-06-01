from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.wrappers import Response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do_tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)


@app.route('/')
def index() -> Response:
    """
    Rendering index page with the list of tasks.

    Returns:
        Response: A rendering HTML templete with the list of tasks.
    """
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task() -> Response:
    """
    Add a new task to the database and after that
    return redirect to the index page.

    Returns:
        Response: A redirect to the index page.
    """
    task_content = request.form['content']
    new_task = Task(content=task_content)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
