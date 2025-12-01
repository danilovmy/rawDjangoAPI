
django-admin startproject rawapi . --template=https://raw.githubusercontent.com/danilovmy/rawDjangoAPI/refs/heads/main/docs/project_template.zip

python manage.py startapp api --template=https://raw.githubusercontent.com/danilovmy/rawDjangoAPI/refs/heads/main/docs/app_template.zip

uvicorn settings.asgi:application

pip install openapi-generator-cli
openapi-generator-cli generate --input-spec-root-directory media -o db_schema -g mysql-schema
mysql -p rawapi < mysql_schema.sql

python manage.py inspectdb > api\models.py

openapi-generator-cli generate --input-spec-root-directory media -o api2 -g python-flask --global-property apis

