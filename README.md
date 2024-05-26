# Мобильное приложение для собак
### Идея проекта
Идея проекта представляет собой систему мониторинга и управления за бездомными животными с использованием приложения. Основными компонентами системы являются носимые устройства - умные ошейники, снабженные различными датчиками, модулями и микроконтроллерами для отслеживания местоположения, состояния и поведения животного в реальном времени. Пользователи могут наблюдать за местоположением и состоянем собак, давать задание другим пользователям, например: проведать собаку, покормить, окозать мед.помощь.


# Регистрация пользователя
Пользователь регистрируется в приложении по имени, фамилии и номеру телефона. Дальше ему генерируется свой уникальный идентификатор(id). Данные пользователя вносятся в базу данных sql под названием people с восьмью столбцами: id, имя, фамилия и номер, координаты, избранные собаки (id собак), запрос на выполнение задания, верификация выполнения задания.

# Регистрация нового ошейника
База данных dogs с шестью столбцами: id и серийный номер производства ошейника, состояние собаки, заряд ошейника, местоположение собаки, комментарий с информацией задания для собаки.

# Привязка ошейников﻿ и пользователей, модерирование
Ошейники могут быть привязаны к пользователям, чтобы они могли мониторить конкретных животных и получать уведомление о их состоянии и местонахождении. Для этого их надо будет добавить в «избранное». Добавить в «избранное» можно любое количество ошейников.
Для добавления новых животных пользователь может зайти на карту в приложении и выбрать собак в своём районе.

Сам персонал устанавливает новые ошейники и мониторит состояние старых, иногда занимается их обслуживанием. У персонала есть сервисный аккаунт, в котором они могут изменять базу данных и мониторить состояние всех собак. Также работники сервисного аккаунт имеют доступ к базе данных people, для получения информации о пользователях.

# Задание от одних пользователям другим, верификация выполнения заданий
Пользователь может выбрать другого пользователя по его местонахождению на карте и дать ему задание, напирмер: погладить собаку, покормить, проведать и т.п. В случае если надо погладить, то выполнение задания произойдет если координаты пользователя и собаки будут находится рядом в течении 5 минут. Если покормить или проведать, то пользователь, которому пришло задание делает фото с выполнением и отправляет его тому, кто дал это задание. Всё это будет работать на запросах и храниться в базах данных.
Запрос: 

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
