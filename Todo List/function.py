import todo
def main():
    print("Welcome to todo app")
    print("""1. Add task
2. Remove Task
3. Mark as done
4. Mark as not done
5. Exit""")
    print("")
    todo.show_task()
    while True:
        user_input=int(input("Pick action: "))
        if user_input == 5:
            print("Thank you")
            break
        if user_input == 1:
            user_input_task=input("Insert the task: ")
            todo.add_task(user_input_task)
        elif user_input == 2:
            user_input_index=int(input("What number do you want to remove? "))-1
            todo.remove_task(user_input_index)
        elif user_input == 3:
            user_input_index=int(input("Which number?"))-1
            todo.mark_as_done(user_input_index, True)
        elif user_input == 4:
            user_input_index=int(input("Which number?"))-1
            todo.mark_as_done(user_input_index, False)
main()