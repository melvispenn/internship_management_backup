# InPACE Internship Management

## Project principles

- Backend first: each functionality is designed, implemented and tested in the backend before its frontend is built.
- Security by Design: authentication, authorization, validation, CSRF, safe file handling, dependency hygiene and secure configuration are considered for every change.
- Internationalization by default: the interface uses the browser/device 'Accept-Language' header through Django 'LocaleMiddleware'. Supported languages are English (en-US), French (fr-FR) and Brazilian Portuguese (pt-BR).
- Modular code: URLs, forms, views, serializers, services, permissions, tasks and configuration are split into focused modules as the project grows.
- Consistent formatting: Python, templates and stylesheets must remain indented and linted.

## Architecture and workflow

Each business application should add, when needed, 'permissions.py', 'services.py', 'configuration.py', and separate 'urls/', 'forms/', 'views/', 'tasks/' and 'api/' modules as the domain grows. Shared validators and exceptions belong in 'internship_management/core/'.

For each feature: define the backend contract and validation, implement authorization, add tests for success/failure/unauthorized access, document the security considerations, then build the translated frontend with protected forms.

## Design system

The visual language is based on the supplied InPACE logo: navy '#0B2A6B', blue '#0E86E8', cyan '#11B9F2', green '#42C72A', and white/slate surfaces. The CSS exposes these as design tokens. Tailwind CSS should consume the same tokens when the frontend build pipeline is introduced.

## Installation

    uv sync
    uv run python manage.py migrate --settings=config.settings.local
    uv run pytest

Alternatively, install runtime dependencies with 'pip install -r requirements.txt', then configure the database and environment variables required by the selected Django settings module.

## Security baseline

Secrets must come from environment variables and must never be committed. Production deployments must use 'DEBUG=False', restricted 'ALLOWED_HOSTS', HTTPS, secure cookies, a configured CSRF origin list, PostgreSQL, and a reviewed dependency lockfile. User input is validated server-side even when client-side validation exists.

## Administration

The project uses Django Admin as the initial administration interface. A dedicated administration experience may be added later as a separate feature, with explicit roles and permissions defined before implementation.

## Frontend tooling

Tailwind CSS v4 and the official @tailwindcss/cli package are installed through npm.

- Build CSS: npm run css:build
- Watch CSS during development: npm run css:watch
- Equivalent Just commands: just css and just css-watch

The generated file is internship_management/static/css/output.css. Do not edit that generated file manually; edit internship_management/static/css/input.css.

## Locale detection (browser/device language)

We added a small JavaScript helper at `internship_management/static/js/locale_detect.js` which sets a `django_language` cookie based on `navigator.language` on first visit when the cookie is not already present. The script is included in the base template so translations apply on initial load.

Developers should ensure that translatable strings in templates and JavaScript are marked appropriately and that `LocaleMiddleware` remains enabled in `config/settings/base.py`.

## Protecting forms and error handling

- All Django templates that render forms must include `{% csrf_token %}` inside the `<form>` tag.
- Use Django's `Form` and `ModelForm` classes for server-side validation; for DRF use `Serializer` validation.
- Wrap risky operations in `try/except` blocks to avoid leaking internal errors. Prefer catching specific exceptions and logging them before returning a safe response.
- Example pattern in views:

```python
from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    try:
        # operation that may fail
        pass
    except ValueError as e:
        # handle expected error
        return HttpResponse(status=400)
    except Exception:
        # log unexpected errors and return generic message
        return HttpResponse(status=500)
```

Keep error handlers minimal and avoid revealing sensitive details to end users.
