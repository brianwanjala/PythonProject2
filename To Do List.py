import time
from operator import index

tasks = []
def add_task():
    task = input('Add task: ')
    tasks.append(task)
    return
def view_task():
    if not tasks:
        print('No tasks added!')
    else:
        print(f'{tasks}')
def remove_task():
    remove = int(input("Enter task number to remove: "))
    try:
        if not tasks:
            print("Please add task.")
        else:
            tasks.remove(tasks[remove-1])
            print(f'task number {remove} has been removed.')
            print(f'remaining tasks {tasks}')
    except:
        print(f"task not found!")

def completed_task():
    complete = int(input("enter task number to mark as completed: "))
    try:
        if not tasks:
            print("Please add task.")
        elif complete > len(tasks):
            print("Task not found!")
        elif complete in range(len(tasks)):
            print(f"task number {complete} is completed")
        else:
            print('task not yet completed')
    except:
        print(f"task not found!")

print('Welcome to our to do list.')
print('what do you want to do?')
print('Please choose from the options below')

print('\noptions')
print('1. Add task')
print('2. view task')
print('3. remove task')
print('4. completed task')
print('5. quit')

while True:
    try:
        choice = input('Enter your choice: ')
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            completed_task()
        elif choice == "5":
            break
        else:
            print('Enter a valid option!')

    except:
        print('Invalid option!')
print("Thank you for your time. Bye.")


