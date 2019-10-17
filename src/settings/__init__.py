from os import environ

from split_settings.tools import include

ENV = environ.get('ENV', 'dev')

include(
    'components/*.py',
    f'environments/{ENV}.py'
)
