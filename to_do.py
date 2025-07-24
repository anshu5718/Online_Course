"""4. To-Do List
Q: Create a menu-based to-do list:
1. Add task
2. View all tasks
3. Remove task
4. Exit
Hint: Use a list to store tasks."""
Menu="""
1. Add task
2. View all tasks
3. Remove task
4. Exit
"""
def to_do():
    task={}
    id=0
    while True:
        print("**********************************")
        print(Menu)
        print("**********************************")
        choice=int(input("Enter a choice: "))
        if choice==1:
            id+=1
            string=input("Enter a task: ")
            task[id]=string
            print("**********************************")
        elif choice==2:
            print("All the task")
            for key, val in task.items():
                print(f"{key}. {val}")
            print("**********************************")
        elif choice==3:
            remove=input("Enter a task to remove: ")
            for key,value in list(task.items()):
                if remove.lower()== value.lower():
                    del task[key]
                    task = {i+1: v for i, v in enumerate(task.values())}
                    break
            print("Deletion complete")
            print("**********************************")
        elif choice==4:
            print("Thank you")
            break
        else:
            print("Wrong entry")
            print("**********************************")
to_do()