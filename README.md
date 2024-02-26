# **Micro-Ugin**

Пет проект для огранизации системы учета оборудования. Реализован на Django


## **Требования к окружению**

Для работы с проектом вам понадобится установить следующие компоненты:

- Python не ниже версии 3.9
- Django не ниже версии 3.2.4
- DRF 3.14


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
- Создание устройств доступно только через админку, привязки параметров к типам и моделям нет.
- Через админку можно просмотреть все модели проекта.

**Для получения данных есть несколько способов**

1. **Через админку Django**


2. **Через формы**
- device/ - отображение списка устройств на сети + форма для указания ID и перехода к 'device/<int:device_id>/'   ![image](https://github.com/TimBait/Ugin/assets/151711444/48955d6c-7727-49a6-bc1e-dd5f724e1bcd)

- device/<int:device_id>/ - отображение параметров устройства   ![image](https://github.com/TimBait/Ugin/assets/151711444/a05cf2d6-6241-447c-9649-91de83f94c46)



3. **Через API**
- path('api_devices/', DeviceListView.as_view(), name='product-list'),     #get на все  ![image](https://github.com/TimBait/Ugin/assets/151711444/44b7bf6a-e5ea-4a14-a59c-c1cad0101690)


- path('api_device/<int:device_id>/', DeviceAPIView.as_view(), name='device_api'),      #get по id device  ![image](https://github.com/TimBait/Ugin/assets/151711444/60804ecb-ab07-4ee8-812e-ad8312d3cdd3)


- path('api_device_models/', DeviceModelListView.as_view(), name='device_model_api'),     #get всех моделей    ![image](https://github.com/TimBait/Ugin/assets/151711444/4f7a8cf7-aca2-4ec9-bdaa-e04d57f948ed)

- path('api_device_types/', DeviceTypeListView.as_view(), name='device_model_api'),      #get всех типов    ![image](https://github.com/TimBait/Ugin/assets/151711444/344fd9a4-b795-4713-b0bd-5949b98fc6bf)


