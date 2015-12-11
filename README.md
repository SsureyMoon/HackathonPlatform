pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

heroku config:add DJANGO_SETTINGS_MODULE=hackathon_platform.settings.production
heroku config:add SECRET_KEY=<add you secret key here>
git push heroku master
