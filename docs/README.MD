
django-admin startproject rawapi . --template=https://raw.githubusercontent.com/danilovmy/rawDjangoAPI/refs/heads/main/docs/project_template.zip

django-admin startproject startapp api --template=https://raw.githubusercontent.com/danilovmy/rawDjangoAPI/refs/heads/main/docs/app_template.zip

uvicorn settings.asgi:application

pip install openapi-generator-cli
openapi-generator-cli generate --input-spec-root-directory media -o db_schema -g mysql-schema
mysql -p rawapi < mysql_schema.sql

python manage.py inspectdb > api\models.py
issue: https://forum.djangoproject.com/t/id-models-autofield/8085/6

openapi-generator-cli generate --input-spec-root-directory media -o api2 -g python-flask --global-property apis

