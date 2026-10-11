def add_task(tasks, title):
    new_id = max((task["id"] for task in tasks), default=0) + 1

    new_task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    return new_task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise ValueError("Task not found")