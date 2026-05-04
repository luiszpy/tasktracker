#Add, Update, and Delete tasks
#Mark a task as in progress or done
#List all tasks
#List all tasks that are done
#List all tasks that are not done
#List all tasks that are in progress



choices = "[1]add task""\n""[2]update task""\n""[3]list task""\n""[4]delete taks""\n"
choice1 = int(input(choices))

if choice1 == 1:#add task
    frequency = int(input('''is:
[1]daily
[2]weekly
[3]monthly
[4]annual
[5]special
'''))
    tfreq = ""
    if frequency == 1:
        tfreq = "every day"
    elif frequency == 2:
        tfreq = "weekly"
    elif frequency == 3:
        tfreq = "monthly"
    elif frequency == 4:
        tfreq = "annual"
    elif frequency == 5:
        tfreq = "special"
    

    if frequency == 2:
        wday = str(input("what week day?(1 monday to 7 sunday, ex: 1/2/7)""\n"))
        


    task = str(input("what the task?""\n"))
    time = str(input("time?"))
    where = str(input("where?"))
    with open(".tasks.txt", "a") as t:
        t.write(f"{task} - {tfreq} - {time} - {where}")
            
  