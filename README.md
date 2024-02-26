# **Micro-Ugin**

Пет проект для огранизации системы учета оборудования. Реализован на Django


## **Требования к окружению**

Для работы с проектом вам понадобится установить следующие компоненты:

- Python не ниже версии 3.9
- Django не ниже версии 3.2.4
- DRF 3.14
- drf-yasg 1.21.7


# **Установка**

1. Клонируйте репозиторий:
  https://github.com/TimBait/Ugin.git

2. Перейдите в каталог проекта:
  cd Ugin

3. Создайте виртуальное окружение и активируйте его:
  python3 -m venv venv
  source venv/bin/activate

4. Установите зависимости проекта:
   pip install -r requirements.txt

5. Настройте базу данных Postgresql

6. Выполните миграции:
   python manage.py migrate

7. Запуск сервера:
   python manage.py runserver


# **Структура проекта**

Ugin/ - основная директория проекта.

devices/ - директория вашего приложения.

requirements.txt - список зависимостей проекта.

manage.py - управляющий скрипт Django.



# **Детали:**
- Создание устройств доступно только через админку.
- Через админку можно просмотреть все модели проекта.
- Привязки параметров к типам и моделям нет. :(
- При создании обьекта Device и выборе DeviceType нужно тыкнуть сохранить, иначе не появится выбор DeviceModel. Пока не понял как победить :(

**Для получения данных есть несколько способов**

1. **Через админку Django**


2. **Через формы**
- device/ - отображение списка устройств на сети + форма для указания ID и перехода к 'device/<int:device_id>/'   ![image](https://github.com/TimBait/Ugin/assets/151711444/48955d6c-7727-49a6-bc1e-dd5f724e1bcd)

- device/<int:device_id>/ - отображение параметров устройства   ![image](https://github.com/TimBait/Ugin/assets/151711444/a05cf2d6-6241-447c-9649-91de83f94c46)



3. ~~**Через API**~~ 
- ~~path('api_devices/', DeviceListView.as_view(), name='product-list'),     #get на все~~  

- ~~path('api_device/<int:device_id>/', DeviceAPIView.as_view(), name='device_api'),      #get по id device~~ 


- ~~path('api_device_models/', DeviceModelListView.as_view(), name='device_model_api'),     #get всех моделей~~    

- ~~path('api_device_types/', DeviceTypeListView.as_view(), name='device_model_api'),      #get всех типов ~~~~   

  **Через Swagger**
  - /swagger/    ![image](https://github.com/TimBait/Ugin/assets/151711444/6c0df084-9c8e-4417-952a-a60ddee34cd4)

