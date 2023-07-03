# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.5.0) - 2023-07-03
-   Add `Django 4.2` support.
-   Drop `Django 2.2` support.
-   Fix `Django 3.0` compatibility.
-   Add translations (`en`, `it`, `ru`).
-   Add `pyupgrade` to `pre-commit` config.
-   Add `django-upgrade` to `pre-commit` hooks.
-   Run `pre-commit` also with `tox`.
-   Switch from `setup.cfg` to `pyproject.toml`.
-   Replace `flake8` with `Ruff`.
-   Pin test requirements.
-   Bump requirements.

## [0.4.0](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.4.0) - 2022-12-13
-   Add `Python 3.11` and `Django 4.1` support.
-   Drop `Python < 3.8` and `Django < 2.2` support. #19
-   Add `pre-commit`.
-   Replace `str.format` with `f-strings`
-   Replace `setup.py test` in favor of `runtests.py`.
-   Bump GitHub actions versions.

## [0.3.1](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.3.1) - 2022-09-19
-   Improve tests coverage.

## [0.3.0](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.3.0) - 2022-07-07
-   Added `created_at` and `updated_at` fields. #4
-   Added tests. #5
-   Added `default_auto_field` setting.
-   Fixed `Redirect.MATCH_PREFIX` not working.

## [0.2.0](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.2.0) - 2021-05-04
-   Added `priority` to redirects. #2

## [0.1.0](https://github.com/fabiocaccamo/django-redirects/releases/tag/0.1.0) - 2020-09-08
-   Published `django-redirects`.
