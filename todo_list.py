class TodoList:
    def __init__(self, name):
        self._name = name
        self._tasks = []

    def add_task(self, task):
        self._tasks.append({"task": task, "completed": False})

    def complete_task(self, task_id):
        self._tasks[task_id]["completed"] = not self._tasks[task_id]["completed"]

        if self._tasks[task_id]["completed"]:
            self._tasks[task_id]["task"] = self._tasks[task_id]["task"][0] + self._tasks[task_id]["task"][1:].replace(
                "", "\u0336")
        else:
            self._tasks[task_id]["task"] = self._tasks[task_id]["task"].replace("\u0336", "")

    def remove_task(self, task_id):
        self._tasks.pop(task_id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks
