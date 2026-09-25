# Testing History

This file records important verification activities. Executable tests remain in the project test directories.

| Date | Area | Test or verification | Purpose | Result |
|---|---|---|---|---|
| 2026-09-25 | Tailwind CLI | npm run css:build | Verify the official Tailwind CLI generates Django's static CSS output | Passed |
| 2026-09-25 | Tailwind assets | tests/frontend/test_tailwind_assets.py | Verify input configuration, template integration, and CLI output | Passed: 3 tests |

| 2026-09-25 | Project test environment | uv run python -m pytest | Check the normal project test command | Blocked: existing test settings require POSTGRES_DB |
