<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Парсер веб-контенту</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        h1, h2, h3, h4 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        ul {
            list-style-type: disc;
            margin: 10px 0;
            padding-left: 20px;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>

<h1>Парсер веб-контенту</h1>

<p>Простий інструмент командного рядка для <strong>парсингу</strong>, <strong>копіювання</strong> та <strong>збереження</strong> конкретного контенту з веб-сторінки.</p>

<h2>Особливості</h2>
<ul>
    <li><strong>Парсинг контенту</strong>: Витягує контент з визначеного розділу веб-сторінки.</li>
    <li><strong>Копіювати в буфер обміну</strong>: Копіює витягнутий контент у ваш буфер обміну.</li>
    <li><strong>Зберегти у файл</strong>: Зберігає витягнутий контент як <code>.txt</code> файл у вибрану директорію.</li>
</ul>

<h2>Передумови</h2>
<p>Переконайтеся, що у вас встановлений <strong>Python 3.x</strong> та необхідні пакети:</p>
<ul>
    <li><code>requests</code></li>
    <li><code>beautifulsoup4</code></li>
    <li><code>pyperclip</code></li>
</ul>
<p>Щоб встановити ці пакети, скористайтеся наступною командою:</p>
<pre><code>pip install requests beautifulsoup4 pyperclip</code></pre>

<h2>Використання</h2>
<ol>
    <li>Клонуйте або завантажте цей репозиторій.</li>
    <li>Відкрийте термінал і перейдіть до директорії, що містить скрипт.</li>
    <li>Запустіть скрипт:
        <pre><code>python script_name.py</code></pre>
    </li>
</ol>

<h3>Команди</h3>
<table>
    <tr>
        <th>Команда</th>
        <th>Опис</th>
    </tr>
    <tr>
        <td><code>-p</code></td>
        <td>Запитує URL і парсить контент з визначеного розділу на веб-сторінці.</td>
    </tr>
    <tr>
        <td><code>-cop</code></td>
        <td>Копіює парсений контент у буфер обміну. Потрібно попередньо використати <code>-p</code>.</td>
    </tr>
    <tr>
        <td><code>-save</code></td>
        <td>Зберігає парсений контент у текстовий файл. Потрібно попередньо використати <code>-p</code>.</td>
    </tr>
    <tr>
        <td><code>-help</code></td>
        <td>Відображає список доступних команд.</td>
    </tr>
    <tr>
        <td><code>-terminate</code></td>
        <td>Виходить зі скрипту.</td>
    </tr>
</table>

<h2>Приклад роботи</h2>
<ol>
    <li>Запустіть скрипт у терміналі.</li>
    <li>Введіть <code>-p</code>, щоб парсити веб-сторінку, і введіть URL, коли буде запропоновано.</li>
    <li>Після парсингу використовуйте <code>-cop</code>, щоб скопіювати контент або <code>-save</code>, щоб зберегти його.</li>
    <li>Щоб вийти, введіть <code>-terminate</code>.</li>
</ol>

<h2>Обробка помилок</h2>
<p>Скрипт містить базову обробку помилок:</p>
<ul>
    <li>Якщо URL не може бути досягнутий або парсений, з'явиться повідомлення про помилку.</li>
    <li>Якщо ви спробуєте скопіювати або зберегти контент перед парсингом, скрипт запропонує спочатку провести парсинг.</li>
</ul>

<h2>Майбутні покращення</h2>
<p>Можливі майбутні покращення можуть включати:</p>
<ul>
    <li>Дозволити користувачам вказувати власні HTML-теги або класи для парсингу.</li>
    <li>Додавання опцій для різних форматів виводу, таких як JSON або CSV.</li>
    <li>Покращена обробка помилок для кращої надійності.</li>
</ul>
