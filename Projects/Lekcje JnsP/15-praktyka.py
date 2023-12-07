user_choice = -1

tasks = []
# tasks.append("Throw the garbage out")
# tasks.append("Clean the desk up")


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


def add_task():
    task = input("Enter the content of the task: ")
    tasks.append(task)
    print("Task has been addeed")


def delete_task():
    task_index = int(input("Enter the task index to delete: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("Task with this index doesn't exist")
        return
    tasks.pop(task_index)
    print("The task has been deleted")


def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()


def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return


load_tasks_from_file()


while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()

    print()
    print("1. Show the task")
    print("2. Add the task")
    print("3. Delete the task")
    print("4. Save changes to file")
    print("5. Exit")

    user_choice = int(input("Choose a numer: "))
    print()
