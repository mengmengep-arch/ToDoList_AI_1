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
	"""Delete a task selected by index with confirmation.

	Prompts the user for an index (1-based). Validates the index and asks
	for confirmation before removing the task from `tasks`.
	"""

	if not tasks:
		print("\nยังไม่มีงานในรายการ\n")
		return

	# show a brief list with indexes
	print("\n=== รายการงาน ===")
	for i, t in enumerate(tasks, start=1):
		status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
		print(f"{i}. {t.get('title')}  -  {t.get('due_date')}  [{status}]")

	try:
		idx_str = input("เลือกงานที่ต้องการลบ (ลำดับ): ")
		idx = int(idx_str)
		if idx < 1 or idx > len(tasks):
			print("Index ไม่ถูกต้อง\n")
			return
	except ValueError:
		print("กรุณาใส่ตัวเลขที่ถูกต้อง\n")
		return

	task = tasks[idx - 1]
	print(f"คุณเลือก: {task.get('title')} (ครบกำหนด: {task.get('due_date')})")
	confirm = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
	if confirm == 'y':
		del tasks[idx - 1]
		print("ลบงานเรียบร้อย\n")
	else:
		print("ยกเลิกการลบ\n")


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