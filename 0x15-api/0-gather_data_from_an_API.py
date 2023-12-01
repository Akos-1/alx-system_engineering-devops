#!/usr/bin/python3
"""A bash script that accepts data from an api"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get employee TODO list progress.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    # Replace this URL with the actual endpoint of your REST API
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Make a GET request to the API
    user_response = requests.get(user_url)

    # Check if the request was successful (status code 200)
    if user_response.status_code != 200:
        print("Error: Could not fetch employee details.")
        return

    # Extract employee name
    user_data = user_response.json()
    employee_name = user_data.get('name', f'Employee {employee_id}')

    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        total_tasks = len(todos)
        done_tasks = sum(1 for task in todos if task['done'])

        if total_tasks > 0:
            progress_message = f"({done_tasks}/{total_tasks})"
        else:
            progress_message = "(No tasks)"

        print(f"Employee {employee_name} is done with tasks{progress_message}: ")

        for task in todos:
            if task['done']:
                print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
