from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []  # liste simple en mémoire pour commencer

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
