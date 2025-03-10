# Test task

This document contains a brief description of the solution and instructions how to run it from Docker and in development mode.

## Table of contents

- [Quickly start from Docker](#quickly-start-from-docker) [API](#api)
  - [API endpoints](#api-endpoints)
  - [Starting in development mode (MacOS and Linux)](#starting-in-development-mode-macos-and-linux)
- [Frontend](#frontend)

## Quickly start from Docker

```bash
docker-compose up --build
```
> [!IMPORANT]
> Make sure to somehow provide `GEMINI_API_KEY` environment variable.

Either run
```bash
export GEMINI_API_KEY=<your_api_key>
```

or add it to `.env` file and provie to docker-compose
```bash
docker-compose --env-file docker.env up --build
```

or add it inline
```bash
API_KEY=<your_api_key> docker-compose up --build
```

By default API runs on port `6969` and frontend on `8080`.

## API

Python [Flask](https://flask.palletsprojects.com/en/stable/) used to create a REST API for the application.
For input validation and output marshalling [Marshmallow](https://marshmallow.readthedocs.io/en/3.x-line/) is used.
Auto-generated apispec Swagger docs are available at `/swagger` and `/swagger-ui` ### API endpoints

There are default handlers setup for `pageNotFound` and `serverError` errors.

Logging is handled by Python's builtin `logging` module. There are two handlers for stdout and file handler with log rotation.
In Docker setup logs are stored in volume.

Rate limiting by IP address is handled by [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/). In the setup an in-memory cache is used.
For production something like [Redis](https://redis.io/) should be used.
For `/` and `/gemini/models` rate limiting is disabled.
For other routes arbitrary rate limiting is used `["1000 per day", "200 per hour", "4 per second"]`.

### API endpoints

#### GET `/`
Returns a hello message

#### GET `/gemini/models`
Returns a list of available models.
```json
{
    "models": ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-pro"]
}
```

#### POST `/gemini/query`
Input schema:
```json
{
  "model": "string",
  "query": "string" // required
}
```
Outputs a stream of `text/plain`

### Starting in development mode (MacOS and Linux)

Create a virtual environment and install dependencies
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Install dev dependencies (optional)
```bash
pip install -r requirements.dev.txt
```

Make sure to set environment variables:
- `LOGLEVEL` => one of `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` defaults to `INFO`
- `GEMINI_API_KEY`
- `PORT` => defaults to `8080`

For example:
.env file
```bash
export LOGLEVEL=DEBUG
export GEMINI_API_KEY=1234567890abcdef
export PORT=6969
```

Do not forget to read env file
```bash
source .env
```

Run dev server
```bash
python flaskapp.py
```

## Frontend

On the frontend I use [Vue3](https://vuejs.org/) with TypeScript and [Vite](https://vite.dev/).
[Tailwind CSS](https://tailwindcss.com/) is used for styling.

In case of API errors a toast is shown.

Frontend consists of one view containing a select model dropdown and a textarea for query input.
API output is shown gradually as it is streamed from the server.

### Starting in developement mode

Install dependencies
```bash
npm install
```

Run dev server
```bash
npm run dev
```
