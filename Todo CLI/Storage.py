import json
from typing import List
from Tasks import Task

def load_tasks(filename='tasks_list.json') -> List[Task]:
    try:
        with open(filename, 'r') as file:
            file_content = json.loads(file)
            return [Task(**t) for task in file_content]
    except FileNotFoundError:
        return []

def save_tasks(tasks: List[Task], filename='tasks_list.json') -> None:
    with open(filename, 'w') as file:
        json.dumps([task.__dict__ for task in tasks], f, indent=2)

        
        
