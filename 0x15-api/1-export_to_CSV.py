#!/usr/bin/python3
"""
Python script that, using this REST API, or a given employee ID,
returns information about his/her TODO list progress.
and exports it as a CSV
"""

from sys import argv
import csv
import requests

# Modules to fetch the URL response


def get_employee_todo_prog(employee_id):
    """returning employee todo info"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_id = requests.get(url + f"users/{employee_id}")
        user_data = user_id.json()
        employ_nam = user_data["name"]

        # fetch todo list for the employee, convert to json
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        # calculate the tasks done and todos left
        total_task = len(json_todos_list)

        # check the task completed by the employee
        task_done = [task for task in json_todos_list if task["completed"]]
        no_task_done = len(task_done)

        # Displaying the result
        print(
            f"Employee {employ_nam} is done with tasks("
            f"{no_task_done}/{total_task}):"
        )

        # displaying the Title of completed tasks
        for task in task_done:
            print(f"\t {task['title']}")

        # Exporting the employee data to csv format
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in json_todos_list:
                writer.writerow(
                    [employee_id, employ_nam, task["completed"], task["title"]]
                )

    except Exception as e:
        print(f"AN ERROR OCCURRED: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todo_prog(argv[1])
