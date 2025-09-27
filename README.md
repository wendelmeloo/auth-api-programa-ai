# auth-api-programa-ai
Api de autenticação desenvolvida como parte do curso de AppSec da Programa.AI

pip freeze > requirements.txt


flask db init
flask db migrate -m "init: users"
flask db upgrade
flask run ou flask run --port=8080