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
    print("ciao")
    sql = "INSERT into task(todo) VALUES (%s)"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_manager")
    cursor = connection.cursor()
    cursor.execute(sql, (newTask,))
    connection.commit()
    cursor.close()
    connection.close()


def removeTask(task):
    sql = "DELETE FROM task WHERE id=%s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_manager")
    cursor = connection.cursor()
    cursor.execute(sql, (task,))
    connection.commit()
    cursor.close()
    connection.close()



# def main():
#     updater = Updater("500897023:AAFgIl4FC5PcsZU-KxZCTpNrx5TULx7xYTU")
#
#     # register a command handler
#     dp = updater.dispatcher
#
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("showTasks", showTasks))
#     dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
#     dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
#     dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks, pass_args=True))
#     dp.add_handler(CommandHandler("stop", stop))    #does not stop the program if /stop from telegram
#
#     # add a non-command handler (messagge handler)
#     dp.add_handler(MessageHandler(Filters.text, error))
#
#     updater.start_polling()
#
#     updater.idle()  # handle the stop of the program

#
# if __name__ == "__main__":
#     main()