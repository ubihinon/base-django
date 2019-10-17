/etc/init.d/nginx start

python3 manage.py migrate
python3 manage.py collectstatic --no-input

uwsgi --ini uwsgi.ini