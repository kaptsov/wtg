## Проект «Куда пойти — Москва глазами Артёма»    

### Общая информация

Проект доступен по ссылке: http://u1741564.isp.regruhosting.ru/  
Панель администратора: http://u1741564.isp.regruhosting.ru//admin

Это код первого урока в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org)

Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).

### Инструкция по локальному запуску (для разработчика)

Скачать репозиторий:

   ```
   git clone https://github.com/kaptsov/wtg.git
   ```

Перейти в папку проекта:

   ```
   cd wtg
   ```

Создать и активировать виртуальное окружение удобным для вас способом:
   ```
   # например, через virtualenv
   python3 -m venv <your-venv-name>
   
   source <your-venv-name>/bin/activate
   ```

Установить зависимости:

   ```
   pip install -r requirements.txt
   ```

Создать и заполнить файл .env
```
SECRET_KEY='secret_key_secret_key_secret_key'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1'
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
MEDIA_ROOT=media
STATIC_ROOT=static
```

Запустить миграции:

```
   python manage.py migrate
   ```

Запустить сервер:

```
   python manage.py runserver
   ```

Сайт запущен на локалхосте по адресу http://127.0.0.1:8000. Теперь можно создать суперюзера...

```
   python manage.py createsuperuser
   ```

...и зайти в админку по адресу: http://127.0.0.1:8000/admin/

Пока на сайте нет локаций. Чтобы поместить локацию на карту, запустите скрипт cо ссылкой на файл локации:

```
   python manage.py load_place <link>
   ```

Ссылки можно взять [тут](urls.txt).    
Чтобы добавить сразу все локации из файла, запустите команду:

   ```
   python manage.py load_place urls.txt
   ```

Либо добавьте локации вручную через админ-панель.

### Создание/редактирование локации в админ-панели

Перейдите в админ-панель по адресу: http://127.0.0.1:8000/admin/ и введите логин и пароль.

Для создания локации нажмите кнопку ```Add``` в панели слева:

Для редактирования локаций откройте их список и выберите нужную, кликнув на нее в списке справа.

Заполните форму и загрузите картинки. Порядок загруженных картинок можно менять перетаскиванием.

Не забудьте нажать ```SAVE```!
   
