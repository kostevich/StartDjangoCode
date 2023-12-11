# StartDjangoCode
**StartDjangoCode** – учебный проект, используется для тренировки правильного оформления проектов на [Django](https://www.djangoproject.com/).

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [Django](https://www.djangoproject.com/), [dublib](https://github.com/DUB1401/dublib). 
```
pip install Django
pip install git+https://github.com/DUB1401/dublib
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. В среде исполнения запустить файл _manage.py_ командой:
```
python manage.py runserver
```
5. Перейти по ссылке (пример: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

# Отслеживание данных в административной панели Django.
1. В среде исполнения запустить команду:
```
python manage.py createsuperuser
```
2. Зарегистрироваться.
3. Перейти по ссылке добавив к ней admin (пример: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)).

# Отслеживание в базе данных.
Откройте файл db.sqlite3 в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы
**Главная страница:**

![image](https://github.com/kostevich/StartDjangoCode/assets/109979502/7d8026f6-d2c0-4357-b18e-338a94a18f32)

**Страница reversed text:**

![image](https://github.com/kostevich/StartDjangoCode/assets/109979502/a341dbe6-2019-40db-810a-fcb9040a598e)

**Страница about:**

![image](https://github.com/kostevich/StartDjangoCode/assets/109979502/f8f137a0-fa30-402b-923d-fea2b92a35d0)

_Copyright © Kostevich Irina. 2023._
