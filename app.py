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
    print("creo")
    bot.saveTask(task)
    return render_template("create_task.html")


if __name__ == '__main__':
    app.run()
