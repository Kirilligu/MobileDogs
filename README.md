# Мобильное приложение для собак
### Идея проекта
Идея проекта представляет собой систему мониторинга и управления за бездомными животными с использованием приложения. Основными компонентами системы являются носимые устройства - умные ошейники, снабженные различными датчиками, модулями и микроконтроллерами для отслеживания местоположения, состояния и поведения животного в реальном времени. Пользователи могут наблюдать за местоположением и состоянем собак, давать задание другим пользователям, например: проведать собаку, покормить, окозать мед.помощь.

## Сценарий проекта
#### 1. Регистрация пользователя
Пользователь регистрируется в приложении по имени, фамилии и номеру телефона, которые задаются в таблице Пользователей 
#### 2. Авторизация пользователя
Пользователь вводит запрос в номер телефона и пароль и получает ключ API
#### 3. Регистрация нового ошейника и собак
Указывается уникальный номер и характеристики ошейника и он записывается в таблицу "ошейники". 
Для регистрации собаки указывается кличка собаки и ее внешнее описание, все это записывается в таблицу Dogs
#### 4. Привязка ошейников﻿ к животному
Создается связь между ошейником и животным
#### 5. Получение списка животных 
Получение списка животных, есть возможность посмотреть местоположение по координатам.
#### 6. Создание, проверка, обновление статуса задания
Пользователь отправляет запрос на сервер с заданием, id собаки и api пользователя для записи в таблицу Tasks. Проверка выполнения задания осуществляется с помощью отправки id задания и фото для подтверждения. Обновление статуса задания происходит с помощью отправки id задания и статуса, который записывается в соответсвующую колонку таблицы Tasks


## Запросы
- Успешный ответ
  ```
    "success": true,
    "exception": null
  ```
- Ошибка
  ```
    "detail": "Unknown Error"
  ```
- Регистрация пользователя
  ```
    "first_name": "Kirill",
    "last_name": "Deg",
    "phone_number": "0987654321",
    "password": "123789999"
  ```
- Вход пользователя
   ```
    "phone_number": "0987654321",
    "password": "supersecret"
  ```
- Регистрация ошейника
   ```
    "unique_number": "1234-5678",
    "characteristics": "Red color, Medium size"
  ```
- Регистрация собаки
   ```
    "name": "Buddy",
    "description": "Golden Retriever"
  ```
#### Создание задания
- Запрос
   ```
    "title": "Walk the dog",
    "description": "Take Buddy for a walk in the park",
    "due_date": "2024-06-01T10:00:00"
  ```
- Ответ
   ```
    "id": 1,
    "title": "Walk the dog",
    "description": "Take Buddy for a walk in the park",
    "due_date": "2024-06-01T10:00:00",
    "status": "pending"
  ```
#### Обновление статуса задания
- Запрос
   ```
    "task_id": 1,
    "status": "completed"
  ```
- Ответ
   ```
    "id": 1,
    "title": "Walk the dog",
    "description": "Take Buddy for a walk in the park",
    "due_date": "2024-06-01T10:00:00",
    "status": "completed"
  ```
#### Список заданий
- Запрос
   ```
   {}
  ```
- Ответ
   ```
    {
        "id": 1,
        "title": "Walk the dog",
        "description": "Take Buddy for a walk in the park",
        "due_date": "2024-06-01T10:00:00",
        "status": "completed"
    },
    {
        "id": 2,
        "title": "Feed the dog",
        "description": "Give Buddy his dinner",
        "due_date": "2024-06-01T18:00:00",
        "status": "pending"
    }

  ```
## Установка и запуск приложения
1. Установите репозиторий к себе на виртуальную машину
   ```
   sudo apt update
   sudo apt install git
   git clone https://github.com/Kirilligu/MobileDogs
    ```
#### Либо же используйте следующий пример для установки, в таком случае 3 пункт можно пропустить:
```
pip install git+https://github.com/Kirilligu/MobileDogs#egg=MobileDogs
```

2. Перейдите в корневую папку
   ```
    cd MobileDogs
    ```
3. Перед запуском установите:
#### Можно установить все библиотеки командой:
```
python3 setup.py install --user
```
#### Либо же установить вручную
- uvicorn
   ```
    sudo apt install uvicorn
    ```
- fastapi
    ```
  sudo pip install fastapi
    ```
- sqlalchemy
  ```
  sudo pip install sqlalchemy
    ```
- passlib
  ```
  sudo pip install passlib
  ```

4. Запустите приложение
  ```
  uvicorn src.main:app --host 0.0.0.0 --port 8000
  ```


- Замените 0.0.0.0 на ip адресс вашей машины и перейдите на сайт, указав послеадреса /docs
![image](https://github.com/Kirilligu/MobileDogs/assets/149255706/32bddaab-de27-4bae-b178-ddff5d05b402)


