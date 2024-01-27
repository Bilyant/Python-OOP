from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        current_task = [t for t in self.tasks if t.name == task_name]
        if not current_task:
            return f'Could not find task with the name {task_name}'
        current_task.completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        cleared_tasks = 0
        uncompleted_tasks = []
        for t in self.tasks:
            if t.completed:
                cleared_tasks += 1
            else:
                uncompleted_tasks.append(t)
        self.tasks = uncompleted_tasks
        return f'Cleared {cleared_tasks} tasks.'

    def view_section(self, ):
        result = [f'Section {self.name}:']
        for t in self.tasks:
            result.append(t.details())
        return '\n'.join(result)


