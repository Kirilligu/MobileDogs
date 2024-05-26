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
#### Привязка ошейников﻿ и пользователей, модерирование
Ошейники могут быть привязаны к пользователям, чтобы они могли мониторить конкретных животных и получать уведомление о их состоянии и местонахождении. Для этого их надо будет добавить в «избранное». Добавить в «избранное» можно любое количество ошейников.
Для добавления новых животных пользователь может зайти на карту в приложении и выбрать собак в своём районе.

Сам персонал устанавливает новые ошейники и мониторит состояние старых, иногда занимается их обслуживанием. У персонала есть сервисный аккаунт, в котором они могут изменять базу данных и мониторить состояние всех собак. Также работники сервисного аккаунт имеют доступ к базе данных people, для получения информации о пользователях.

#### Задание от одних пользователям другим, верификация выполнения заданий
Пользователь может выбрать другого пользователя по его местонахождению на карте и дать ему задание, напирмер: погладить собаку, покормить, проведать и т.п. В случае если надо погладить, то выполнение задания произойдет если координаты пользователя и собаки будут находится рядом в течении 5 минут. Если покормить или проведать, то пользователь, которому пришло задание делает фото с выполнением и отправляет его тому, кто дал это задание. Всё это будет работать на запросах и храниться в базах данных.


# Запросы
# Регистрация нового пользователя
POST(name: str, surname: str, phone_number: str)

# Регистрация нового ошейника
POST(serial_number: str)

# Привязка ошейника к пользователю
POST(user_id: int, collar_id: int):

# Добавление собаки в избранное пользователя
POST(user_id: int, dog_id: int):

# Добавление новой собаки на карту
POST(latitude: float, longitude: float):

# Дать задание другому пользователю
POST(user_id: int, task: str):

# Верификация выполнения задания
POST(task_id: int, photo: str):
