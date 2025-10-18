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


def view_tasks():
	"""Display all tasks with index, title, due_date and status.

	If no tasks exist, print a friendly message.
	"""
	if not tasks:
		print("\nยังไม่มีงานในรายการ\n")
		return

	print("\n=== รายการงานทั้งหมด ===")
	for i, t in enumerate(tasks, start=1):
		status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
		title = t.get("title") or "(ไม่มีชื่อ)"
		due = t.get("due_date") or "-"
		print(f"{i}. {title}  | วันครบกำหนด: {due}  | {status}")
	print("")


def list_tasks():
	"""List all tasks (empty stub)."""
	view_tasks()


def update_task():
	"""Update a task selected by index (0-based display to user as 1-based).

	User can edit title, description, and completed status. Index is validated.
	"""
	global tasks

	if not tasks:
		print("\nยังไม่มีงานในรายการ\n")
		return

	view_tasks()

	try:
		idx_str = input("ป้อนลำดับงานที่ต้องการแก้ไข (ตัวเลข): ").strip()
		idx = int(idx_str) - 1
	except ValueError:
		print("ตัวเลขไม่ถูกต้อง\n")
		return

	if idx < 0 or idx >= len(tasks):
		print("ลำดับงานไม่ถูกต้อง\n")
		return

	task = tasks[idx]

	print(f"\nแก้ไขงาน id={task['id']} (ปล่อยว่างเพื่อคงค่าเดิม)")
	new_title = input(f"ชื่อเรื่อง [{task['title']}]: ").strip()
	new_description = input(f"รายละเอียด [{task['description']}]: ").strip()
	new_completed = input(f"สถานะเสร็จแล้ว? (y/N) [{'y' if task['completed'] else 'N'}]: ").strip().lower()

	if new_title:
		task['title'] = new_title
	if new_description:
		task['description'] = new_description
	if new_completed in ('y', 'yes'):
		task['completed'] = True
	elif new_completed in ('n', 'no'):
		task['completed'] = False

	print("แก้ไขงานเรียบร้อย\n")



def edit_task():
	"""Compatibility wrapper: call update_task()."""
	update_task()


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