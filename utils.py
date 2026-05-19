from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)


def print_success(msg: str):
    print(Fore.GREEN + "✓ " + msg)


def print_error(msg: str):
    print(Fore.RED + "✗ " + msg)


def print_warning(msg: str):
    print(Fore.YELLOW + "⚠ " + msg)


def format_task(task, show_index=True):
    """Форматирует задачу для красивого вывода"""
    status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if task.completed else f"{Fore.RED}○{Style.RESET_ALL}"
    title = f"{Fore.CYAN}{task.title}{Style.RESET_ALL}" if task.completed else task.title
    
    created = datetime.fromisoformat(task.created_at).strftime("%d.%m.%Y %H:%M")
    line = f"{status} {task.id:2d}. {title}"
    if task.description:
        line += f"\n    └─ {task.description}"
    line += f"\n    └─ Создано: {created}"
    if task.completed and task.completed_at:
        completed_date = datetime.fromisoformat(task.completed_at).strftime("%d.%m.%Y %H:%M")
        line += f" | Завершено: {completed_date}"
    return line