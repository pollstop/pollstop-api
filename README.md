# Pollstop API
Backend API server code for pollstop project


## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Structure](#structure)
  - [Data Models](#data-models)
  - [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- `GET` / `POST` / `PUT` endpoints using Django REST Framework.
- Modularized applications:
  - polls
  - tags
  - accounts
- PostgreSQL or SQLite3.
- Results pagination.
- Requests Throttling system.
- CMS Admin dashboard to edit database entries.
- API explorer.


## Getting Started

#### Install dependencies
This project requires Python and Django to build, if they are not installed on your device, you should install them first.

1. [Python3](https://www.python.org/downloads/)
2. [Django](https://www.djangoproject.com/)
3. [Django REST Framework](http://www.django-rest-framework.org/)
7. [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)

#### Install Python dependencies
```bash
pip3 install -r requirements.txt
```

#### Initial Server Setup
1. Collect Static Files
```bash
./manage.py collectstatic
```

2. Create Django Database
```bash
./manage.py makemigrations
./manage.py migrate
```

3. Create Admin account
```bash
./manage.py createsuperuser
```

_Note:_ users info can be changed later from *AUTHENTICATION AND AUTHORIZATION* section in the admin dashboard

#### Running the server
```bash
./manage.py runserver -p 8000
```

#### Administration Dashboard
Server admin dashboard can be accessed by visiting the URL `localhost:8000/admin`.

#### API Explorer
API Explorer is available for all [endpoints](#api-endpoints) via the URL `localhost:8000/<endpoint_url>`.


## Structure

#### Data Models
- [Poll](polls/models.py)
- [Choice](polls/models.py)
- [Tag](tags/models.py)
- [User](accounts/models.py)


#### API Endpoints

- **GET Endpoints**
  - Polls:
    - `api/v1/polls/latest/`: get latest 10 polls.
    - `api/v1/polls/<poll_id>/`: get specific poll.
  - Tags:
    - `api/v1/tags/`: get all tags (paginated).
    - `api/v1/tags/<tag_id>/`: get specific tag.
    - `api/v1/tags/<tag_id>/polls/`: get all polls having a tag (paginated).
  - Users:
    - `api/v1/users/<user_id>/`: get all info and votes for a user (requires authorization) / or get public info for a user (without authorization).
    - `api/v1/users/<user_id>/token/`: get auth token for a user (requires email and password fields in request).
    - `api/v1/users/<user_id>/polls/`: get all polls owned by a user (paginated).
- **POST Endpoints**:
  - Polls:
    - `api/v1/polls/`: create new poll and it's choices (requires authentication).
  - Users:
    - `api/v1/users/`: create new user (requires email, password fields in request).
  - Tags:
    - `api/v1/tags/`: create new tag (requires authentication).
- **PUT Endpoints**:
  - Votes:
    - `api/v1/choices/<choice_id>/vote`: vote for a choice (requires authentication).
    - `api/v1/choices/<choice_id>/unvote`: un-vote for a choice (requires authentication).
  - Users:
    - `api/v1/users/<user_id>/`: update user info (requires authorization).

## Contributing
This Project is still in progress. Your feedback is always appreciated and welcomed. If you find a bug in the source code or a mistake in the documentation, you can help us by submitting an issue [**here**](https://github.com/pollstop/pollstop-api/issues). Even better you can submit a Pull Request with a fix :)


## License
This repo is released under the [MIT License](LICENSE).
