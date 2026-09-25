# Local development commands. Docker is intentionally not used for now.

default:
    @just --list

css:
    @npm run css:build

css-watch:
    @npm run css:watch

manage +args:
    @uv run python manage.py {{args}}

pytest *args:
    @uv run pytest {{args}}
