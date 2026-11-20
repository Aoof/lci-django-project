# Django Product Directory

A Django 5 site that lists businesses from a database on a Bootstrap theme, built for a course at Collège LaSalle (November 2025). The pages are in French (`/accueil/`, `/contact/`).

## Features
- A `Product` model (name, image, description, rating, number of ratings, price range, category), managed through the Django admin
- The home page renders every product from the database as an "explore" card
- A contact page
- `populate.py` loads six sample listings so the site has content on first run
- Settings read the secret key, debug flag and allowed hosts from environment variables

## Tech
Python, Django 5.2, SQLite, Django templates, Bootstrap 3 theme with jQuery

## Run it
```bash
git clone https://github.com/Aoof/lci-django-project.git
cd lci-django-project
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python populate.py             # optional: sample listings
python manage.py runserver
```

Open http://127.0.0.1:8000 (it redirects to `/accueil/`). To manage listings, run `python manage.py createsuperuser` and go to `/admin/`.

### Environment variables
| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | a development key | Set a real key outside local development |
| `DJANGO_DEBUG` | `True` | Set to `False` in production |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated host names |

## Author
Abdulrahman (Aoof) Mousa · [aoof.ca](https://aoof.ca)
