from datetime import datetime
from typing import List
from models import Task
from storage import Storage
from utils import (
    print_success,
    print_error,
    print_warning,
    Fore,
    Style,
    format_task
)


class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks: List[Task] = self.storage.load_tasks()
        self.next_id = max([t.id for t in self.tasks], default=0) + 1

    def add_task(self, title: str, description: str = ""):
        """Добавляет новую задачу"""
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.storage.save_tasks(self.tasks)
        print_success(f"Задача добавлена: {title}")

    def delete_task(self, task_id: int) -> bool:
        """Удаляет задачу по ID"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.storage.save_tasks(self.tasks)
                print_success(f"Задача #{task_id} удалена")
                return True
        print_error(f"Задача #{task_id} не найдена")
        return False

    def toggle_complete(self, task_id: int) -> bool:
        """Переключает статус выполнения задачи"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                if task.completed:
                    task.completed_at = datetime.now().isoformat()
                else:
                    task.completed_at = None
                self.storage.save_tasks(self.tasks)
                status = "завершена" if task.completed else "не завершена"
                print_success(f"Задача #{task_id} отмечена как {status}")
                return True
        print_error(f"Задача #{task_id} не найдена")
        return False

    def list_tasks(self, filter_type: str = "all"):
        """Выводит список задач"""
        print(f"\n{Fore.YELLOW}=== СПИСОК ЗАДАЧ ==={Style.RESET_ALL}\n")
        filtered = self.tasks
        
        if filter_type == "completed":
            filtered = [t for t in self.tasks if t.completed]
        elif filter_type == "pending":
            filtered = [t for t in self.tasks if not t.completed]

        if not filtered:
            print("Задач пока нет.")
            return

        for task in filtered:
            print(format_task(task))
            print()

        # Статистика
        total = len(self.tasks)
        done = len([t for t in self.tasks if t.completed])
        if total > 0:
            print(f"Прогресс: {done}/{total} ({done/total*100:.1f}%)")
        else:
            print("Прогресс: 0/0")

    def search_tasks(self, keyword: str):
        """Поиск задач по ключевому слову"""
        keyword = keyword.lower()
        results = [t for t in self.tasks if keyword in t.title.lower() or keyword in t.description.lower()]
        
        if not results:
            print_warning(f"Задачи с ключевым словом '{keyword}' не найдены")
            return
        print(f"\nРезультаты поиска по '{keyword}':\n")
        for task in results:
            print(format_task(task))
            print()