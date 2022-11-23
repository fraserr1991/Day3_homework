tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks
def uncompleted_tasks():
    uncompleted_tasks = 0

    for task in tasks:
        if task["completed"] == False:
            task_des = task["description"]
            print(f"Uncompleted: {task_des}")

uncompleted_tasks()

# 2. Print a list of completed tasks
def completed_tasks():
    completed_tasks = 0

    for task in tasks:
        if task["completed"] == True:
            task_des = task["description"]
            print(f"Completed: {task_des}")
            

completed_tasks()

# 3. Print a list of all task descriptions
def all_tasks():
    all_tasks = 0

    for task in tasks:
            task_des = task["description"]
            print(task["description"])
            

all_tasks()

# 4. Print a list of tasks where time_taken is at least a given time
def timed_tasks():

    for task in tasks:
        if task["time_taken"] > 15:
            task_des = task["description"]
            print(f"This task took more than 15 seconds: {task_des}")
            

timed_tasks()

# 5. Print any task with a given description
def find_task():

    for task in tasks:
        if task["description"] == "Wash Dishes":
            print(task)
            

find_task()

