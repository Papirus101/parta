FROM python

WORKDIR /app

COPY . .

RUN python3.10 -m pip install -r requirements.txt

RUN python parta/manage.py migrate

RUN parta/manage.py loaddata parta/db.json
