import pymysql


#import the list of tasks from the database
def readTasks():
    sql = "SELECT * from task"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_manager")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    tasks = []
    for task in result:
        print(task[1])
        tasks.append(task[1])
    print(result)
    cursor.close()
    connection.close()
    return result


def saveTask(newTask):
    sql = "INSERT into task(todo) VALUES (%s)"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_manager")
    cursor = connection.cursor()
    cursor.execute(sql, (newTask,))
    connection.commit()
    cursor.close()
    connection.close()


def removeTask(id_task):
    sql = "DELETE FROM task WHERE id=%s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_manager")
    cursor = connection.cursor()
    cursor.execute(sql, (id_task,))
    connection.commit()
    cursor.close()
    connection.close()