import requests
from bs4 import BeautifulSoup as bs4
import pyperclip as clipboard
import os

def fetch_and_parse_content(url):
    """Отримує HTML-джерело сторінки та повертає відформатований вміст потрібного розділу."""
    try:
        source = requests.get(url).text
        soup = bs4(source, 'lxml')
        # Знаходимо розділ 'slides' всередині тега body
        content_div = soup.find('body').find('div', class_='slides')
        # Форматуємо HTML для зручного вигляду
        formatted_content = content_div.prettify()
        return formatted_content
    except Exception as e:
        print('Не вдалося проаналізувати:', e)
        return None

def copy_to_clipboard(content):
    """Копіює переданий вміст у буфер обміну."""
    try:
        clipboard.copy(content)
        print("Вміст скопійовано до буфера обміну.")
    except Exception:
        print('Немає що копіювати.')

def save_to_file(directory, filename, content):
    """Зберігає переданий вміст у текстовий файл за вказаним шляхом."""
    try:
        file_path = os.path.join(directory, filename + '.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Файл збережено за адресою {file_path}')
    except Exception as e:
        print(f'Сталася помилка: {e}')

def process_command(command):
    """Виконує команду користувача на основі вказаного вводу."""
    available_commands = ['-p', '-cop', '-save', '-help', '-terminate']

    if command == '-help':
        # Виводимо список команд
        print(available_commands)
    elif command == '-p':
        # Запитуємо користувача для введення посилання
        url = input('Введіть посилання: ')
        global parsed_content
        parsed_content = fetch_and_parse_content(url)
        if parsed_content:
            print("Аналіз успішний.")
    elif command == '-cop':
        # Копіюємо вміст, якщо він доступний
        if 'parsed_content' in globals():
            copy_to_clipboard(parsed_content)
        else:
            print("Нічого копіювати. Спочатку проаналізуйте вміст.")
    elif command == '-save':
        # Зберігаємо вміст, якщо він доступний
        if 'parsed_content' in globals():
            directory = input('Введіть директорію для збереження: ')
            filename = input('Введіть назву файлу: ')
            save_to_file(directory, filename, parsed_content)
        else:
            print("Нічого зберігати. Спочатку проаналізуйте вміст.")
    elif command in ['-terminate', '-t', 'ter']:
        # Завершуємо роботу програми
        global script_running
        script_running = False

# Умова для запуску циклу
script_running = True    
parsed_content = None
while script_running:
    # Чекаємо введення команди від користувача
    user_command = input("Введіть команду: ")
    process_command(user_command)
