**Simple blog on Python**

---
****Описание***
Это мой первый тренировочный проект, написанный на языке Пайтон с использованием фрэймворка Джанго.
Функционал блога включает в себя возможность авторизированным пользователям добавлять статьи, комментировать их, также имеется личный кабинет для авторов.
Для создания фронт-энда я использовал простой ХТМЛ шаблон.

****Тематика****
Блог посвящен теме королевских гонок Ф1, так как я являюсь большим фанатом автоспорта. Если и ты тоже, тебе будет приятно заметить некотоорые забавные отсылки в именах авторов стате и не только=).

---
 ***Getting Started***
 
 Make virtualenv
===============

On Linux::

   $ python3.6 -m venv venv
   $ . venv/bin/activate

On Windows::

   > python -m venv venv
   > venv/Scripts/activate

Install python
===============

::
Install Python 3.5.2: pyenv install 3.5.2.


Clone this repository
===============

::

git clone git@github.com:Oleksandr015/My_first_blog.git

Install requirements
===============

::

   (venv)$ pip install -r requirements.txt

migrate
=======

::

   (venv)$ cd myproject
   (venv)$ python manage.py migrate

Make admin user
===============

::

   (venv)$ python manage.py createsuperuser

runserver
=========

::

   (venv)$ cd myproject
   (venv)$ python manage.py runserver
