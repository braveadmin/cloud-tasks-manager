from flask import Flask, request, render_template
import create_queue
import create_task
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sign-up.html')
    #return "Hello World"

@app.route('/createqueue', methods=['POST'])
def createqueue():
    queue_name = request.form['queue_name']
    location = request.form['location']
    project_id = request.form['project_id']
    return create_queue.create_queue(project_id, queue_name, location)

@app.route('/createtask', methods=['POST'])
def createtask():
    task_name = request.form['task_name']
    location = request.form['location']
    project_id = request.form['project_id']
    queue = request.form['queue']
    return create_task.create_http_task(project_id, queue, location)


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)