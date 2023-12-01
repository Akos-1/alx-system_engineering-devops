#!/usr/bin/python3
"""A bash script accept an integer as a
parameter, which is the employee ID"""
import requests
import sys
import csv


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

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos = response.json()

        # Extract employee name
        employee_name = todos[0].get('username', '')

        # Count the number of completed tasks
        done_tasks = [task for task in todos if task.get('completed', False)]

        # Create CSV file for the employee
        csv_filename = f'{employee_id}.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write CSV header
            writer.writeheader()

            # Write tasks to CSV
            for task in todos:
                task_data = {
                    'USER_ID': employee_id,
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': str(task.get('completed', False)),
                    'TASK_TITLE': task.get('title', ''),
                }
                writer.writerow(task_data)

        # Display the employee TODO list progress
        num_done_tasks = len(done_tasks)
        total_tasks = len(todos)
        status = "OK" if num_done_tasks > 0 else "Incorrect"
        progress_message = (
            f'Employee Name: {status} '
            f'({num_done_tasks}/{total_tasks}):'
        )
        print(progress_message)

        # Display the titles of completed tasks
        if done_tasks:
            for task in done_tasks:
                print(f'\t{task.get("title", "")}')
        else:
            print('\tNo completed tasks')

        print(f'Data exported to {csv_filename}')
    else:
        print(f'Error: Unable to fetch TODO list for employee {employee_id}')


if __name__ == "__main__":
    # Check if an employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
