FROM python:3.7

WORKDIR /var/www

ENV ENV=production
RUN cd ..
COPY pyproject.toml poetry.lock ./

RUN apt update \
    && apt install -y nginx


COPY . .

RUN mkdir /var/scripts \
    && cp deploy/nginx/* /etc/nginx \
    && cp deploy/server/uwsgi.ini /var/www/uwsgi.ini \
    && cp deploy/server/* /var/scripts \
    && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
    && export PATH="$PATH:$HOME/.poetry/bin" \
    && poetry config settings.virtualenvs.create false \
    && poetry install --no-dev --no-interaction

CMD ["chmod", "+x", "/var/scripts/run.sh"]
CMD ["/bin/bash", "-c", "/var/scripts/run.sh"]

EXPOSE 80
