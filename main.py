import os
import csv
from datetime import datetime

def read_tasks(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tasks.append({"description": row[0], "due_date": row[1]})
    return tasks

def write_tasks(file_path, tasks):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for task in tasks:
            writer.writerow([task["description"], task["due_date"]])

def add_task(tasks):
    description = input("Enter task description:")
    due_date_str = input("Enter due date (YYYY-MM-DD):")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        tasks.append({"description": description, "due_date": due_date_str})
        print("Task added successfully!")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_tasks(tasks):
    if not tasks:
        print("Your To-Do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):  # enumarate -> enumerate
            print(f"{index}. {task['description']} - Due on {task['due_date']}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove:")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            print("Task removed successfully")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    file_path = input("Enter the file path to use:")
    if not file_path:
        file_path = "todo_list.csv"

    tasks = read_tasks(file_path)

    while True:
        print("\nTo-Do List Manager\n")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            write_tasks(file_path, tasks)
            print("\nTo-Do List saved successfully. See you next time!")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()