## При установке на стороннюю ВМ нужно прописать путь к flask окружению для работы
source /home/entrant/venv/myproject/bin/activate;
cd /home/entrant/rest-api-yandex;
gunicorn --bind 0.0.0.0:8080 main:app

