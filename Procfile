web: pip install --upgrade pip && python3 lazyreload/manage.py migrate --settings=lazyreload.lazyreload.settings.prod && gunicorn lazyreload.lazyreload.wsgi --env DJANGO_SETTINGS_MODULE=lazyreload.lazyreload.settings.prod