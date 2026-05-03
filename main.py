#Add, Update, and Delete tasks
#Mark a task as in progress or done
#List all tasks
#List all tasks that are done
#List all tasks that are not done
#List all tasks that are in progress



choices = "[1]add task""\n""[2]update task""\n""[3]list task""\n""[4]delete taks"
choice1 = int(input(choices))

if choice1 == 1:#add task
    task = str(input("what the task?"))
    frequency = int(input('''is:
[1]daily
[2]weekly
[3]monthly
[4]annual
[5]special
'''))
    time = str(input("time?"))
    where = str(input)
    with open(".tasks.txt", "a") as t:
        t.write(f"{task} - {frequency} - {time} - {where}")