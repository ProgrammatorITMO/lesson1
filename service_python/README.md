# Документация по реализациям сервиса

Этот проект содержит две реализации одного и того же сервиса с использованием различных Python веб-фреймворков: Flask и FastAPI.

## Структура проекта

```
service_python/
├── flask_service.py   # Реализация с использованием Flask
├── fastapi_service.py # Реализация с использованием FastAPI
├── requirements.txt   # Зависимости для обеих реализаций
```

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-repo/lessons.git
    cd lessons/lesson1/service_python
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск сервисов

### Реализация на Flask
Для запуска сервиса на Flask выполните:
```bash
python main2.py
```
Сервис будет доступен по адресу `http://127.0.0.1:3000`.

### Реализация на FastAPI
Для запуска сервиса на FastAPI выполните:
```bash
uvicorn main1:app --reload --port 3000
```
Сервис будет доступен по адресу `http://127.0.0.1:3000`.

## Зависимости

Файл `requirements.txt` включает следующие зависимости:
```
flask
fastapi
uvicorn
```

Убедитесь, что вы установили эти зависимости перед запуском любой из реализаций.