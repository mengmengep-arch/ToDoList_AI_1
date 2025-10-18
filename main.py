import sys

# In-memory storage for tasks during runtime
tasks = []
# simple increasing id counter for new tasks
next_id = 1


def add_task():
	"""Add a new task by prompting the user and appending to `tasks`.

	Each task is a dict with keys: id, title, description, due_date, completed
	"""
	global next_id, tasks

	print("\n=== เพิ่มงานใหม่ ===")
	title = input("ชื่อเรื่อง: ").strip()
	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (เช่น 2025-10-20 หรือ ข้อความ): ").strip()

	task = {
		"id": next_id,
		"title": title,
		"description": description,
		"due_date": due_date,
		"completed": False,
	}

	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย (id={next_id})\n")
	next_id += 1


def list_tasks():
	"""List all tasks (empty stub)."""
	pass


def edit_task():
	"""Edit an existing task (empty stub)."""
	pass


def delete_task():
	"""Delete a task (empty stub)."""
	pass


def show_menu():
	print("""
To-Do List - Main Menu

1. เพิ่มงานใหม่
2. ดูงานทั้งหมด
3. แก้ไขงาน
4. ลบงาน
5. ออกจากโปรแกรม
""")


def main():
	while True:
		show_menu()
		choice = input("เลือกตัวเลือก (1-5): ")

		if choice == '1':
			add_task()
		elif choice == '2':
			list_tasks()
		elif choice == '3':
			edit_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			print("ออกจากโปรแกรม")
			sys.exit(0)
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง\n")


if __name__ == '__main__':
	main()