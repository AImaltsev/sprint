# Проект Sprint

Проект Sprint - это Django-проект для работы с данными о перевалах. 

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваш_юзернейм/sprint.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Создайте и примените миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

5. Установите подключение к БД.

   Нужно создать файл .env и прописать в нём настройки в соответствии с настройками вашей БД в таком формате:
   ```bash
   FSTR_DB_NAME='Имя базы данных'
   FSTR_DB_LOGIN='Пользователь базы данных'
   FSTR_DB_PASS='пароль'
   FSTR_DB_HOST='хост'
   FSTR_DB_PORT=порт
   ```

   _*Используется БД PostreSQL_

## Использование

Проект Sprint предоставляет REST API для работы с данными о перевалах. 

### Добавление нового перевала

Используйте метод POST для `/api/submitData/`, отправив JSON с необходимыми данными.

Пример:

```bash
curl -X POST http://localhost:8000/api/submitData/ -H "Content-Type: application/json" -d '{"beauty_title": "Mount Everest", "title": "Everest", ...}'
```

## Получение информации о перевале по ID
Используйте метод GET для /api/submitData/<id>.

Пример:

```bash
curl http://localhost:8000/api/submitData/1/
```

## Редактирование перевала по ID
Используйте метод PATCH для /api/submitData/<id>. Редактирование доступно только для записей со статусом "new".

Пример:
```bash
curl -X PATCH http://localhost:8000/api/submitData/1/ -H "Content-Type: application/json" -d '{"beauty_title": "New Title", ...}'
```

## Получение списка перевалов по email пользователя
Используйте метод GET для /api/submitData/?user__email=<email>.

Пример:
```bash
curl http://localhost:8000/api/submitData/?user__email=user@example.com
```