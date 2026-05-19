from task_manager import TaskManager
from utils import (
    print_success,
    print_error,
    print_warning,
    Fore,
    Style,
    format_task
)


def show_menu():
    print("\n" + "="*40)
    print("               TaskFlow")
    print("="*40)
    print("1. Добавить новую задачу")
    print("2. Показать все задачи")
    print("3. Показать невыполненные")
    print("4. Показать выполненные")
    print("5. Отметить выполнение")
    print("6. Удалить задачу")
    print("7. Поиск")
    print("0. Выход")
    print("="*40)


def main():
    manager = TaskManager()
    print("Приложение TaskFlow запущено!")

    while True:
        show_menu()
        try:
            choice = input("\nВыберите действие (0-7): ").strip()

            if choice == "1":
                title = input("Название задачи: ").strip()
                if not title:
                    print_error("Название не может быть пустым!")
                    continue
                desc = input("Описание (Enter — пропустить): ").strip()
                manager.add_task(title, desc)

            elif choice == "2":
                manager.list_tasks("all")
            elif choice == "3":
                manager.list_tasks("pending")
            elif choice == "4":
                manager.list_tasks("completed")
            elif choice == "5":
                try:
                    tid = int(input("Введите ID задачи: "))
                    manager.toggle_complete(tid)
                except ValueError:
                    print_error("Пожалуйста, введите число!")
            elif choice == "6":
                try:
                    tid = int(input("Введите ID задачи для удаления: "))
                    manager.delete_task(tid)
                except ValueError:
                    print_error("Пожалуйста, введите число!")
            elif choice == "7":
                keyword = input("Введите ключевое слово для поиска: ").strip()
                if keyword:
                    manager.search_tasks(keyword)
            elif choice == "0":
                print_success("Спасибо за использование TaskFlow!")
                break
            else:
                print_error("Неверный выбор!")
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена.") 
            break
        except Exception as e:
            print_error(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
