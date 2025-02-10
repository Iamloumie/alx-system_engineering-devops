#!/usr/bin/python3
"""
Python script that, using this REST API, or a given employee ID,
returns information about his/her TODO list progress.
"""

from sys import argv
import json
import requests

# request module to fetch the url response


def get_employee_tasks():
    """returning all employee task progress info"""
    try:
        # fetching the user info
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users")
        user_data = user_response.json()

        # putting the employee data in a dictionary
        all_employee_task = {}

        for user in user_data:
            employee_id = user["id"]
            employee_name = user["username"]

            # getting the employee todo list for the current employee
            todo_response = requests.get(url + f"todos?userId={employee_id}")
            todo_list = todo_response.json()

            # preparing json data
            tasks = [
                {
                    "username": employee_name,
                    "task": task["title"],
                    "completed": task["completed"],
                }
                for task in todo_list
            ]
            all_employee_task[str(employee_id)] = tasks

        # export to json
        json_filename = "todo_all_employees.json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(all_employee_task, json_file, indent=4)

    except Exception as e:
        print(f"AN ERROR OCCURED: {e}")


if __name__ == "__main__":
    get_employee_tasks()
