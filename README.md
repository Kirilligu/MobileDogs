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
   /users/register
