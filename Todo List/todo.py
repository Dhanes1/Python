todo = [["Do homework",False],["Clean the house",False]]
def show_task():
    num=1
    for i in todo:
        check="\u2714"if i[1]else"_"
        print(str(num)+". "+i[0]+" "+check)
        num+=1
def add_task(task):
    newTask = [task,False]
    if newTask not in todo:
        todo.append(newTask)
        print("Task added succesfully")
        show_task()
def remove_task(index):
    if (0 <= index < len(todo)):
        todo.pop(index)
        print("Task removed sucessfully")
        show_task()
    else:
        print("Task out of range")
def mark_as_done(index,is_done):
    if (0 <= index < len(todo)):
        temp = todo[index]
        if temp[1]==is_done:
            if is_done:
                print('Task already marked as done')
            else:
                print("Task already marked as not done")
        else:
            todo[index][1] = not temp[1]
            print("Marked sucessfully")
            show_task()