import sys


def add_task():
	"""Add a new task (empty stub)."""
	pass


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