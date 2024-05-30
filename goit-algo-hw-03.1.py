import os
import shutil
import argparse

def recursive_read_directory(directory):
    # Рекурсивно читає вміст директорії і виводить усі файли та піддиректорії.
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print("File:", item_path)
        elif os.path.isdir(item_path):
            print("Directory:", item_path)
            # Рекурсивний виклик для піддиректорії
            recursive_read_directory(item_path)

def copy_and_sort(source_dir, destination_dir):
    try:
        # Перевірка існування вихідної та цільової директорій
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Отримання списку файлів та піддиректорій у вихідній директорії
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            if os.path.isfile(source_item_path):
                # Отримання розширення файлу
                _, extension = os.path.splitext(item)
                # Створення піддиректорії за розширенням, якщо вона не існує
                destination_subdir = os.path.join(destination_dir, extension[1:])
                if not os.path.exists(destination_subdir):
                    os.makedirs(destination_subdir)
                # Копіювання файлу до піддиректорії
                shutil.copy(source_item_path, destination_subdir)
            elif os.path.isdir(source_item_path):
                # Рекурсивний виклик для піддиректорії
                copy_and_sort(source_item_path, destination_dir)
    except Exception as e:
        print("Помилка:", e)

def main():
    try:
        # Парсинг аргументів командного рядка
        parser = argparse.ArgumentParser(description="Copy files recursively and sort them by extension")
        parser.add_argument("source_dir", help="Path to the source directory")
        parser.add_argument("-d", "--destination_dir", help="Path to the destination directory (default: %(default)s)", default="dist")
        args = parser.parse_args()

        # Виклик функції для копіювання та сортування файлів
        copy_and_sort(args.source_dir, args.destination_dir)

        # Рекурсивне читання директорій (для перевірки)
        print("Contents of source directory:")
        recursive_read_directory(args.source_dir)
    except Exception as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()

