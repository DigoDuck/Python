import os
import json

def list_(tasks):
    print()
    if not tasks:
        print("No tasks to list")
        return
    
    print("Tasks: ")
    for task in tasks:
        print(f"\t{task}")
        
def undo(tasks, redo_tasks):
    print()
    if not tasks:
        print("No tasks to undo")
        print()
        return
    
    task = tasks.pop()
    redo_tasks.append(task)
    
def redo(tasks, redo_tasks):
    print()
    if not redo_tasks:
        print("No tasks to redo")
        print()
        return
    
    task = redo_tasks.pop()
    tasks.append(task)
    
def add(task,tasks):
    print()
    task = task.strip()
    if not task:
        print("You didn't send any task")
        print()
        return
    tasks.append(task)
    
def read(tasks, path):
    data = []
    try:
        with open(path, "r", encoding="utf8") as a_file:
            data = json.load(a_file)
    except FileNotFoundError:
        print("File does not exist")
        save(tasks, path)
    return data
    
def save(tasks, path):
    with open(path, "w", encoding="utf8") as a_file:
            data = json.dump(tasks, a_file, indent=2,
             ensure_ascii=False)
    return data
    
FILE_PATH = "task_list.json"
tasks = read([], FILE_PATH)
redo_tasks = []

while True:
    print("commands: list, undo, redo, exit, clear")
    user_input = input("type one task or command: ")
    save(tasks, FILE_PATH)
    
    if user_input == "list":
        list_(tasks)
        continue
    elif user_input == "undo":
        undo(tasks, redo_tasks)
        list(tasks)
        continue
    elif user_input == "redo":
        redo(tasks, redo_tasks)
        list(tasks)
        continue
    elif user_input == "clear":
        os.system("cls")
    elif user_input == "exit":
        break
    else:
        add(user_input, tasks)
        list(tasks)
        continue