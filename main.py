from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghjkl1234567890'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from auth import auth_bp
app.register_blueprint(auth_bp)

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    current_user = None
    if user_id:
        current_user = User.query.get(user_id)
    return dict(current_user=current_user)

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    todos = Todo.query.filter_by(user_id=session['user_id']).all()
    return render_template('index.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        new_task = Todo(
            title=request.form['title'],
            description=request.form.get('description'),
            due_date=request.form.get('due_date'),
            completed=('completed' in request.form),
            user_id=session['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('todo_form.html', action='Create', todo=None)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form.get('description')
        task.due_date = request.form.get('due_date')
        task.completed = ('completed' in request.form)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('todo_form.html', action='Edit', todo=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    task = Todo.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
