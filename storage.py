import json
from pathlib import Path
from typing import List, Dict
from models import Task


class Storage:
    def __init__(self, filename: str = "tasks.json"):
        self.file_path = Path(filename)

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из JSON-файла"""
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except Exception:
            return []

    def save_tasks(self, tasks: List[Task]):
        """Сохраняет задачи в JSON-файл"""
        data = [task.to_dict() for task in tasks]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)