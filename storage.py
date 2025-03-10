import csv, os
from tasks import Task
STORAGE_FILE="daily_tasks.csv"
fieldnames = ['id', 'title', 'description', 'completed']
def load_tasks():
    tasks = []
    try:
        with open(STORAGE_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task = Task(title = row["title"], description = row["description"])
                task.id = row["id"]
                task.completed = row["completed"].lower() == "true"
                tasks.append(task)
    except FileNotFoundError:
        return []
    return tasks
            
                



def save_tasks(tasks):
    with open(STORAGE_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({"id": task.id, "title": task.title, "description": task.description, "completed": str(task.completed)})
