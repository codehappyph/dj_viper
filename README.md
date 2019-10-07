Viper Project
=============

A sample Django project with a good production setup.


## Pre-requisites

- Python 3.6.x
- PostgreSQL 10.x
- Redis (or Memurai for Windows)
- RabbitMQ


## Development setup (Windows)

1) Create a virtual environment and install requirements

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

**NOTE:**

The commands in the succeeding steps should be run while the virtualenv is
activated.


2) Apply migrations and create superuser

```
cd viper
python manage.py migrate
python manage.py createsuperuser
```

3) Run Django server

```
python manage.py runserver
```

4) Running celery and celerybeat

You need to run each commands in a seperate shell

```
cd viper
celery -A viper worker -P gevent --loglevel info -E
```

```
cd viper
celery -A viper beat --pidfile=..\var\run\celery\beat.pid --loglevel info
```

Optional:

Run celery flower (web monitoring tool)


```
celery -A viper flower --port=5555
```

Allow it through Windows firewall and then open your browser to
`http://127.0.0.1:5555`.


**NOTE:**

Use Chrome or Firefox when opening Celery Flower page as it there are
incompatibilities with Edge or IE.


## Production setup (Linux)

1) Clone project to /srv/src/

```
cd /srv/src/
git clone https://github.com/codehappyph/dj_viper.git
```


2) Create virtualenv called `viper` and set it as local python version
  for the project directory

```
cd /srv/src/dj_viper/
pyenv virtualenv 3.6.9 viper
pyenv local viper
```


3) Install requirements

Whenever you are inside the project folder, the virtualenv, `viper`, will
always be activated by default.

```
cd /srv/src/dj_viper/
pip install -r requirements.txt
```

4) Setup the celery systemd service

Copy all systemd service files to the system settings

```
cd /srv/src/dj_viper/
sudo cp -r var/etc/systemd/system/viper-celery* /etc/systemd/system/
systemctl daemon-reload
```

**NOTE:**

When you make changes to the celery service files, you will need to copy
them again to the `/etc/systemd/system` folder and reload the systemctl
daemon.


5) Setup nginx gunicorn

Make sure user is part of www-data group

```
sudo usermod -aG www-data pydev
```

Copy the nginx sites

```
cd /srv/src/dj_viper/
sudo cp var/etc/nginx/sites-available/viper /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/viper /etc/nginx/sites-enabled/viper
```


6) Start the gunicorn and celery services

```
systemctl start viper-celery.service
systemctl start viper-celerybeat.service

systemctl start viper-gunicorn.sock
systemctl enable viper-gunicorn.sock

systemctl restart nginx
```

There are also: stop and restart commands

Whenever you make code changes, you will need to restart the celery services.

References:

Celery Daemonizing

- http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#usage-systemd

Django Gunicorn / NGINX

- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#configure-nginx-to-proxy-pass-to-gunicorn
