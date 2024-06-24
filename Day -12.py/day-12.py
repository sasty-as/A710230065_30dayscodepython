#implementasi program Object-Oriented Programming (OOP) Python 

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title}: {self.description} - {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

# Contoh penggunaan
task1 = Task("Belajar Python", "Selesaikan bab OOP")
task2 = Task("Olahraga", "Lari selama 30 menit")
manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)
manager.show_tasks()
task1.mark_as_completed()
manager.show_tasks()
