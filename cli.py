#!/usr/bin/env python3

import argparse, sys
from tasks import Task
from storage import load_tasks, save_tasks

def add_tasks(title, description=""):
    tasks = load_tasks()
    new_task = Task(title, description)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added: {new_task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:    
        print("Title | Description | Completed\n" +
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}.")

def complete_task(taskId):
    tasks = load_tasks()
    for task in tasks:
        if task.id == taskId:
            task.completed = True
            print(f"completed {task}.")
            save_tasks(tasks)
            return
    print(f"Unable to find task with {taskId} id.")
        
def delete_task(taskId):
    tasks = load_tasks()
    updated_tasks = []
    for task in tasks:
        if task.id != taskId:
            updated_tasks.append(task)
    save_tasks(updated_tasks)
    #print(f"Unable to delete task with {taskId} id.")

def main():
    if len(sys.argv) <= 1:
        print("Must provide arguments")
        sys.exit(1)

    command = sys.argv[1]
    #print(f"command: {command}, task: {task}, description: {description}")
    if command == "list":
        list_tasks()
    elif command == "add":
        task, description = sys.argv[2], sys.argv[3]
        add_tasks(task, description)
    elif command == "complete":
        taskId = sys.argv[2]
        complete_task(taskId)
    elif command == "delete":
        taskId = sys.argv[2]
        delete_task(taskId)
    else:
        print("Must use one of these commands: list, add, complete, delete")


if __name__ == "__main__":
    main()
