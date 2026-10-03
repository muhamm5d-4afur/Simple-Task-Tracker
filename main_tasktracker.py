from tasktracker_classes import Task, UrgentTask, HomeTask, TaskManager


def main():
	manager = TaskManager()

	while True:
		print("\n————— Smart Task Tracker —————")
		print("1. Add Normal Task")
		print("2. Add Urgent Task")
		print("3. Add Home Task")
		print("4. Show Report and Exit")
		choice = input("Choose (1-4): ").strip()

		if choice == "1":
			title = input("Task title: ").strip()
			if title:
				manager.add_task(Task(title))
			else:
				print("! Empty title, skipped.")

		elif choice == "2":
			title = input("Urgent task title: ").strip()
			if title:
				manager.add_task(UrgentTask(title))
			else:
				print("! Empty title, skipped.")

		elif choice == "3":
			title = input("Home task title: ").strip()
			if title:
				manager.add_task(HomeTask(title))
			else:
				print("! Empty title, skipped.")

		elif choice == "4":
			manager.show_dashboard()
			manager.execute_all()

			print("\n===== FINAL REPORT =====")
			print(f"Tasks in manager : {manager.count_tasks()}")
			print(f"Total tasks ever : {Task.total_tasks}")
			print("Goodbye...")
			break

		else:
			print("! Invalid choice, try again.")


if __name__ == "__main__":
	main()