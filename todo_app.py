import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, title, due_date=None):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': due_date,
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task {task_id} not found!")
    
    def list_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks found!")
            return
            
        print("\nYour Todo List:")
        print("-" * 60)
        for task in self.tasks:
            if not show_completed and task['completed']:
                continue
            status = "✓" if task['completed'] else " "
            due = f"(Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{task['id']}. [{status}] {task['title']} {due}")
        print("-" * 60)
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task {task_id} not found!")
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['id']}|{task['title']}|{task['completed']}|{task['created_at']}|{task['due_date']}\n")
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    id, title, completed, created_at, due_date = line.strip().split('|')
                    self.tasks.append({
                        'id': int(id),
                        'title': title,
                        'completed': completed == 'True',
                        'created_at': created_at,
                        'due_date': due_date if due_date != 'None' else None
                    })

def main():
    todo = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            due_date = due_date if due_date else None
            todo.add_task(title, due_date)
        
        elif choice == '2':
            show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
            todo.list_tasks(show_completed)
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo.complete_task(task_id)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()