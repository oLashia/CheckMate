from todo_list import TodoList


class TodoListManager:
    todo_lists = []

    @classmethod
    def new_todo_list(cls, name):
        cls.todo_lists.append(TodoList(name))
        print(f"Todo list {name} created")

    @classmethod
    def remove_todo_list(cls, id):
        cls.todo_lists.pop(id)

    @classmethod
    def view_all_todo_lists(cls):
        for i in range(len(cls.todo_lists)):
            print(i + 1, cls.todo_lists[i].name, sep=": ")

    @classmethod
    def view_todo_list(cls, id):
        for i in range(len(cls.todo_lists[id].tasks)):
            print(i + 1, cls.todo_lists[id].tasks[i]["task"], sep=": ")

    @classmethod
    def add_new_task(cls, id, task):
        cls.todo_lists[id].add_task(task)
        print(f"Task {task} created")

    @classmethod
    def complete_task(cls, id, task_id):
        cls.todo_lists[id].complete_task(task_id)

    @classmethod
    def remove_task(cls, id, task_id):
        cls.todo_lists[id].remove_task(task_id)


def main():
    print("CHECK MATE by Lashwanth Kumar", end="")
    while True:
        choice = main_menu()

        if choice == 1:
            name = new_todo_list_menu()
            TodoListManager.new_todo_list(name)
            choice = 2

        while choice == 2:
            second_choice = view_all_todo_lists_menu()

            if second_choice == len(TodoListManager.todo_lists) + 1:
                id = remove_todo_list_menu() - 1
                TodoListManager.remove_todo_list(id)
            elif second_choice <= len(TodoListManager.todo_lists):
                while True:
                    third_choice, id = selected_todo_list_menu(second_choice - 1)

                    if third_choice == len(TodoListManager.todo_lists[id].tasks) + 3:
                        print("gay")
                        break
                    elif third_choice == len(TodoListManager.todo_lists[id].tasks) + 2:
                        task_id = remove_task_menu(id) - 1
                        TodoListManager.remove_task(id, task_id)
                    elif third_choice == len(TodoListManager.todo_lists[id].tasks) + 1:
                        task = new_task_menu()
                        TodoListManager.add_new_task(id, task)
                    elif third_choice < len(TodoListManager.todo_lists[id].tasks) + 1:
                        TodoListManager.complete_task(id, third_choice - 1)
            else:
                break
        if choice == 3:
            break


def main_menu():
    while True:
        print("\n======== MAIN MENU ========")
        print("1. Create a new To-Do List")
        print("2. View all To-Do Lists")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))
        if 1 <= choice <= 3:
            return choice
        else:
            print("\nError: Please enter a valid choice")


def view_all_todo_lists_menu():
    while True:
        print("\n======== TODO LISTS ========")
        TodoListManager.view_all_todo_lists()
        print(len(TodoListManager.todo_lists) + 1, "Remove a To-Do List", sep=": ")
        print(len(TodoListManager.todo_lists) + 2, "Back", sep=": ")
        choice = int(input("\nEnter your choice: "))

        if choice == len(TodoListManager.todo_lists) + 1 and len(TodoListManager.todo_lists) == 0:
            print("\nError: No To-Do Lists created")
        elif 1 <= choice <= len(TodoListManager.todo_lists) + 2:
            return choice
        else:
            print("\nError: Please enter a valid choice")


def new_todo_list_menu():
    print("\n======== NEW TODO LIST ========")
    return input("Name: ")


def remove_todo_list_menu():
    while True:
        print("\n======== REMOVE TODO LIST ========")
        choice = int(input("Enter your choice: "))

        if 1 <= choice <= len(TodoListManager.todo_lists):
            return choice
        else:
            print("\nError: Please enter a valid choice")


def selected_todo_list_menu(id):
    while True:
        print(f"\n======== {TodoListManager.todo_lists[id].name} ========")
        TodoListManager.view_todo_list(id)
        print(len(TodoListManager.todo_lists[id].tasks) + 1, "Create a new Task", sep=": ")
        print(len(TodoListManager.todo_lists[id].tasks) + 2, "Remove a Task", sep=": ")
        print(len(TodoListManager.todo_lists[id].tasks) + 3, "Back", sep=": ")
        choice = int(input("\nEnter your choice: "))

        if choice == len(TodoListManager.todo_lists[id].tasks) + 2 and len(TodoListManager.todo_lists[id].tasks) == 0:
            print("\nError: No Tasks created")
        elif 1 <= choice <= len(TodoListManager.todo_lists[id].tasks) + 3:
            return choice, id
        else:
            print("\nError: Please enter a valid choice")


def new_task_menu():
    print("\n======== NEW TASK ========")
    return input("Task: ")


def remove_task_menu(id):
    while True:
        print("\n======== REMOVE TASK ========")
        choice = int(input("Enter your choice: "))

        if 1 <= choice <= len(TodoListManager.todo_lists[id].tasks):
            return choice
        else:
            print("\nError: Please enter a valid choice")


if __name__ == "__main__":
    main()
