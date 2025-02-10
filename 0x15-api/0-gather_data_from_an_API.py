#!/usr/bin/python3
"""
Python script that, using this REST API, or a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

# request module to fetch the url response


def get_employee_todo_prog(employee_id):
    """returning employee todo progress info"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_id = requests.get(url + f"users/{employee_id}")
        user_data = user_id.json()
        employee_name = user_data["name"]

        # fetch todo list for the employee
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        # calculating the task done and task left
        total_task = len(json_todos_list)

        # check the completed task
        task_done = [task for task in json_todos_list if task["completed"]]
        no_task_done = len(task_done)

        # Displaying the result
        print(
            f"Employee {employee_name} is done with tasks("
            f"{no_task_done}/{total_task}):"
        )

        # printing the Title of completed tasks
        for task in task_done:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"AN ERROR OCCURRED: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todo_prog(argv[1])
