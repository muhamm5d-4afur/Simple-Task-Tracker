from datetime import datetime


class NotifierMixin:
	def notify(self, message):
		print(f"   [NOTIFY] {message}")


class Task:
	total_tasks = 0

	def __init__(self, title):
		self.title = title
		self.status = "pending"
		self.created_at = datetime.now().strftime("%H:%M:%S")
		Task.total_tasks += 1

	def execute(self):
		print(f"   Executing task: {self.title}")

	def show_details(self):
		print(f"   Title  : {self.title}")
		print(f"   Status : {self.status}")
		print(f"   Created: {self.created_at}")

	def get_status(self):
		return self.status


class UrgentTask(Task, NotifierMixin):
	def __init__(self, title):
		super().__init__(title)  
		self.priority = "HIGH"

	def execute(self):           
		print(f"   URGENT: {self.title}")
		self.notify("This task must be done NOW!")

	def show_details(self):       
		print(f"   Title   : {self.title}")
		print(f"   Status  : {self.status}")
		print(f"   Priority: {self.priority}")
		print(f"   Created : {self.created_at}")


class HomeTask(Task):
	def __init__(self, title):
		super().__init__(title)
		self.location = "Home"

	def execute(self):
		print(f"   Doing at {self.location}: {self.title}")


class TaskManager:
	def __init__(self):
		self.tasks = []

	def add_task(self, task):
		self.tasks.append(task)
		print(f"   Task added: {task.title}")

	def show_dashboard(self):
		print("\n===== DASHBOARD =====")
		if not self.tasks:
			print("No tasks yet.")
			return
		for t in self.tasks:
			print(f"- {t.title}  |  Status: {t.get_status()}")

	def execute_all(self):
		print("\n===== EXECUTING ALL TASKS =====")
		if not self.tasks:
			print("Nothing to execute.")
			return
		for t in self.tasks:    
			t.execute()

	def count_tasks(self):
		return len(self.tasks)