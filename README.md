# Django Blog Practice

Небольшой учебный проект по Django: блог статей с категориями, списком, детальными страницами и формами создания/редактирования.

## Возможности
- категории и статьи
- список статей и детальная страница
- формы создания и редактирования
- админ-панель
- базовый тест представления

## Структура
- `blog_project/` — проект Django
- `articles/` — приложение статей

## Запуск
1. `python -m venv .venv`
2. `source .venv/bin/activate` или `.venv\Scripts\activate`
3. `pip install django`
4. `python manage.py migrate`
5. `python manage.py runserver`

Открыть: `http://127.0.0.1:8000/articles/`
