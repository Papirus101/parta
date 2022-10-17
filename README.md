# HOW TO START
# With docker
- `run cp .env_dist .env` and change value in .env file
- run `docker compose up`
# Without docker
- run `mv .env_dist .env` and change value in .env file
- run `python -m venv venv`
- run `source venv/bin/activate`
- apply migrations `python manage.py migrate`
- load test data `python manage.py loaddata db.json`
- run django `python manage.py runserver`
