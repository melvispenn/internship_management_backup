# Bootstrap and default authentication removal report

## Changes made

- Removed the Bootstrap CDN CSS and JavaScript references from the base template.
- Removed Bootstrap-specific markup and `data-bs-*` attributes from the base, account, allauth, and user templates.
- Replaced the Bootstrap layout with semantic navigation, local project CSS, and native Django form rendering.
- Removed `crispy-bootstrap5` and `django-crispy-forms` from the project dependencies and Django configuration.
- Removed Django’s default `ModelBackend` from `AUTHENTICATION_BACKENDS`; django-allauth is now the only web authentication backend.
- Kept DRF `SessionAuthentication` so Django’s authenticated admin/test clients and browser-based API access continue to work; this is separate from Django’s default `ModelBackend`.
- Kept `django.contrib.auth` installed because the custom user model, permissions, admin, sessions, and allauth require Django’s auth framework. This does not enable the default `ModelBackend`.

## Verification

- Searched templates, settings, source, and dependency declarations for Bootstrap/crispy references.
- Ran the Django test suite and system checks after the changes.
