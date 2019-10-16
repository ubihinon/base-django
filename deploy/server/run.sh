/etc/init.d/nginx start

python3 manage.py migrate

uwsgi --ini uwsgi.ini