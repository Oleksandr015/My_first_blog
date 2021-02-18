=====================
Simple blog on Python
=====================


Description
=====================


This is my first training project written in Python using the Django framework.
The functionality of the blog includes the ability for authorized users to add articles, comment on them; there is also a personal account for authors.
To create the front end, I used a simple HTML template.


Subject
=======


The blog is dedicated to the topic of F1 royal races, as I am a big fan of motorsport. If you are too, you will be pleased to see some funny references in the names of the authors of the article and not only 😊.


 Getting Started
 ===============
 
**Make virtualenv**

>On Linux::

   `$ python3.6 -m venv venv`
   `$ . venv/bin/activate`

>On Windows::

   `python -m venv venv`
   `venv/Scripts/activate`

****Install python****

   `install Python 3.6: pyenv install 3.6`

****Clone this repository****

   `git clone git@github.com:Oleksandr015/My_first_blog.git`
   

****Install requirements****

   `(venv)$ pip install -r requirements.txt`

****Migrate****

   `(venv)$ cd myproject`
   `(venv)$ python manage.py migrate`

****Make admin user****

   `(venv)$ python manage.py createsuperuser`

****Runserver****

   `(venv)$ cd myproject`
   `(venv)$ python manage.py runserver`
