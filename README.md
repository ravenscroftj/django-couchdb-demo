# ICML Django + Couch Example

By James Ravenscroft

## Installation

First make sure you have Apache CouchDB running on your system or another
machine. The file `icml/settings.py` has a `COUCHDB_SERVER` value which is used
to point Django to the correct location if it isn't installed locally.

Run the following code to install and run the django server:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

Use something like [Postman](https://www.getpostman.com/docs/introduction) to
test the API endpoints.

### POST /papers/create

You can post a JSON object to this URL to create a paper in Couchdb:

```json
{
  "title" : "Latent Dirichlet Allocation",
  "abstract" : "We describe latent Dirichlet allocation (LDA), a generative...",
  "type" : "journal"
}
```

The response will be a carbon copy of your input data plus the relevant ID

```json
{
  "id": "ba5379605c18a29368f7ec6dcb0022e0",
  "title" : "Latent Dirichlet Allocation",
  "abstract" : "We describe latent Dirichlet allocation (LDA), a generative...",
  "type" : "journal"
}
```

### GET /papers/<id>

Given an ID, return JSON representation of that paper from CouchDB.

```
GET /papers/ba5379605c18a29368f7ec6dcb0022e0
```

...

```json
{
  "id": "ba5379605c18a29368f7ec6dcb0022e0",
  "title" : "Latent Dirichlet Allocation",
  "abstract" : "We describe latent Dirichlet allocation (LDA), a generative...",
  "type" : "journal"
}
```
