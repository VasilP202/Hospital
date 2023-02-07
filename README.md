# Hospital application
    - FIT VUT
    - Databázové systémy 
    - April 2022

## Requirements
    - Python 3.8+

## Run
```shell
$ cd hospital
$ python -m venv .venv
$ source .venv/bin/activate         #.venv\Scripts\activate on Windows(cmd)
$ pip install django
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```



## Access admin site
```shell
$ python manage.py createsuperuser
```
Fill in username and password. After running a server navigate to ```http://127.0.0.1:8000/admin``` and use your credentials.
