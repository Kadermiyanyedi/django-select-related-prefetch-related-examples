# Django Select Related & Prefetch Related Example

This repository include the source codes of the article about [django optimization tips 2](https://kadermiyanyedi.medium.com/django-optimizasyon-i%CC%87pu%C3%A7lar%C4%B1-2-select-related-prefetch-related-24e0a5b2ba1d).

## Setup

## Create a virtual environment to isolate our package dependencies locally

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**For poetry users:**

```
poetry install
poetry shell
```

## Migrate Database & Load Initial Data

```
cd backend
python manage.py migrate

python manage.py loaddata user.yaml
python manage.py loaddata country.yaml
python manage.py loaddata product.yaml
```

## Admin Panel Login Credentials & Start Server

```
username: admin
password: secret1secret
```

If you want create a new super user : python manage.py createsuperuser --email xxx --username xxx

```python manage.py runserver```

Go to `localhost:8000` in your browser
