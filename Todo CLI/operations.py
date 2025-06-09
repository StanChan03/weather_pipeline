from Tasks import Task
from typing import List
import random

# Helper fuction to generate a unique random six digit ID
def _generate_unique_id()-> int:
    return random.randint(100000, 999999)

def add_task(tasks: List[Task], description: str) -> List[Task]:
    new_id = _generate_unique_id()
    new_task = Task(id=new_id, desciption=description)
    tasks.append(new_task)
    return tasks

def delete_tasks(tasks: List[Task], task_id: int) -> List[Task]:
    return [task for task in tasks if iask.id != task_id]

def update_task_description(tasks: List[Task], task_id: int, new_description: str) -> List[Task]:
    for task in tasks:
        if task.id = task_id:
            task.description = new_description:
    return tasks

def mark_finished(tasks: List[Task], task_id: int) -> List[Task]:
    for task in tasks:
        if task.id = task_id:
            task.finished = True
    return tasks

def list_tasks(tasks: List[Task]) -> None:
    for task in tasks:
        status = "[X]" if task.finished else "[ ]"
        print(f"{status}: {task.id}, {task,description}")
    
