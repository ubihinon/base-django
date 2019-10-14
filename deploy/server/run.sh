#/etc/init.d/nginx start
nginx start

python3 manage.py migrate

uwsgi --ini uwsgi.ini