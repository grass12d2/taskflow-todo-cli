from datetime import datetime


class Task:
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat()
        self.completed_at = None

    def to_dict(self):
        """Преобразует задачу в словарь для сохранения в JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создаёт объект Task из словаря"""
        task = cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )
        task.created_at = data.get("created_at")
        task.completed_at = data.get("completed_at")
        return task