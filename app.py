from flask import Flask, render_template, session, redirect, url_for,request
import bot

app = Flask(__name__)

#app.secret_key = "veryveryverysecrettt"

@app.route('/')
def hello_world():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template("index.html", tasks=bot.readTasks())


@app.route('/create_task', methods=['POST'])
def create_task():
    task = request.form['task']
    bot.saveTask(task)
    return render_template("create_task.html")


@app.route('/delete_task/<id_task>')
def delete_task(id_task):
    tasks = bot.readTasks()
    task_deleted = [task for task in tasks if task[0] == id_task]
    # print(task_deleted)
    # deleted = task_deleted[1]
    bot.removeTask(id_task)
    # return render_template("delete_task.html", task=deleted)
    return render_template("index.html", tasks=bot.readTasks())


if __name__ == '__main__':
    app.run()
