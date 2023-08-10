class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number > (len(self.comments) - 1) or comment_number < 0:
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

        # [1, 2, 3, 4, 5] -> len = 5
        # idx = from 0 to 4

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

