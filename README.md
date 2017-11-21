# Pollstop API
Backend API server code for pollstop project


## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Structure](#structure)
  - [Data Models](#data-models)
  - [API Endpoints](#api-endpoints)
- [Using the API](#using-the-api)
  - [Create new user](#create-new-user)
  - [Get user token](#get-user-token)
  - [Create new poll](#create-new-poll)
  - [Vote for a poll](#vote-for-a-poll)
  - [Unvote for a poll](#unvote-for-a-poll)
  - [Create new tag](#create-new-tag)
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
    - `api/v1/tags/`: get all tags.
    - `api/v1/tags/<tag_id>/`: get specific tag.
    - `api/v1/tags/<tag_id>/polls/`: get all polls having a tag.
  - Auth:
    - `api/v1/auth/<user_id>/token/`: get auth token for a user.
  - Users:
    - `api/v1/users/<user_id>/`: get all info and votes for a user (requires auth token in request header) / or get public info for a user (without auth token).
    - `api/v1/users/<user_id>/polls/`: get all polls owned by a user (paginated).
- **POST Endpoints**:
  - Polls:
    - `api/v1/polls/`: create new poll and it's choices.
  - Auth:
    - `api/v1/auth/`: create new user.
  - Tags:
    - `api/v1/tags/`: create new tag (requires auth token in request header).
- **PUT Endpoints**:
  - Votes:
    - `api/v1/choices/<choice_id>/vote`: vote for a choice (requires auth token in request header).
    - `api/v1/choices/<choice_id>/unvote`: un-vote for a choice (requires auth token in request header).


## Using the API

#### Create new user
- Method: `POST`
- Endpoint: `api/v1/auth/`
- Body:
  - `email` user email address (required).
  - `password` user password (required).
  - `display_name` display name for user (required).
  - `bio` user's bio (optional).

Example response:
```
{
    "type": "user",
    "id": 19652,
    "email": "email@test.com",
    "display_name": "Test User",
    "bio": "Nothing to see here, I'm a test user!",
    "date_joined": "2017-11-21T08:47:07.713294Z",
    "token": "027bb3a58728d6e3721b029ef45825ecdab64b83",
    "votes": []
}
```

#### Get user token
- Method: `POST`
- Endpoint: `api/v1/auth/token/`
- Body:
  - `email` user email address (required).
  - `password` user password (required).

Example response:
```
{
    "token": "027bb3a58728d6e3721b029ef45825ecdab64b83"
}
```


#### Create new poll
- Method: `POST`
- Endpoint: `api/v1/polls/`
- Headers:
  - `Authorization`: auth token, example: `Token 027bb3a58728d6e3721b029ef45825ecdab64b83`
- Body:
  - `title` poll's title (required).
  - `description` poll's description (optional).
  - `choice_1` first choice for the poll.
  - `choice_2` second choice for the poll.
  - `choice_3` third choice for the poll.
  - `choice_4` forth choice for the poll.

_Note:_ New poll must have at least 2 choices, and at max 4 choices.

Example response:
```
{
    "type": "poll",
    "id": 23128794,
    "title": "Do you like pollstop?",
    "description": "Assuming you have used the api or visited the website :)",
    "date_created": "2017-11-21T08:57:05.109839Z",
    "owner": 2131,
    "choices": [
        {
            "id": 5872513,
            "text": "Yes, I love it!",
            "votes": 0
        },
        {
            "id": 5872514,
            "text": "No I don't :(",
            "votes": 0
        }
    ]
}
```


#### Vote for a poll
- Method: `PUT`
- Endpoint: `api/v1/choices/5872513/vote/`
- Headers:
  - `Authorization`: auth token, example: `Token 027bb3a58728d6e3721b029ef45825ecdab64b83`

Example response:
```
{
    "id": 5872513,
    "text": "Yes, I love it!",
    "votes": 194
}
```


#### Unvote for a poll
- Method: `PUT`
- Endpoint: `api/v1/choices/5872513/unvote/`
- Headers:
  - `Authorization`: auth token, example: `Token 027bb3a58728d6e3721b029ef45825ecdab64b83`

Example response:
```
{
    "id": 5872513,
    "text": "Yes, I love it!",
    "votes": 193
}
```

#### Create new tag
- Method: `POST`
- Endpoint: `api/v1/tags/`
- Headers:
  - `Authorization`: auth token, example: `Token 027bb3a58728d6e3721b029ef45825ecdab64b83`
- Body:
  - `name` tag's name (required).

Example response:
```
{
    "type": "tag",
    "id": 1,
    "name": "Technology"
}
```


## Contributing
This Project is still in progress. Your feedback is always appreciated and welcomed. If you find a bug in the source code or a mistake in the documentation, you can help us by submitting an issue [**here**](https://github.com/pollstop/pollstop-api/issues). Even better you can submit a Pull Request with a fix :)


## License
This repo is released under the [MIT License](LICENSE).
