[![](https://img.shields.io/pypi/pyversions/django-redirects.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-redirects?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-redirects.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-redirects/)
[![](https://pepy.tech/badge/django-redirects/month)](https://pepy.tech/project/django-redirects)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-redirects?logo=github)](https://github.com/fabiocaccamo/django-redirects/)
[![](https://badges.pufler.dev/visits/fabiocaccamo/django-redirects?label=visitors&color=blue)](https://badges.pufler.dev)
[![](https://img.shields.io/pypi/l/django-redirects.svg?color=blue)](https://github.com/fabiocaccamo/django-redirects/blob/master/LICENSE.txt)

[![](https://img.shields.io/github/workflow/status/fabiocaccamo/django-redirects/Test%20package?label=build&logo=github)](https://github.com/fabiocaccamo/django-redirects)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-redirects?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-redirects)
[![](https://img.shields.io/codacy/grade/6bc31cfdbc2b463b808bd3dc23a44444?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-redirects)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-redirects?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-redirects/)
[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# django-redirects

**django-redirects** fills the gap of `django.contrib.redirects` offering **redirects with full control**.

## Features

- Sites framework support.
- Custom redirect type: `301`, `302`, `303`, `307`, `308`.
- Custom redirect match condition: `EXACT`, `PREFIX` or `REGEX`.
- Regex support, match and replace groups using group reference: `$1`, `$2`, `$3`, ...
- Counter to monitor requests count handled by each redirect.
- Admin integration with list filters and the possibility to test the redirect.

## Installation

- Run `pip install django-redirects`.
- Add `redirects` to `settings.INSTALLED_APPS`.
- Add `redirects.middleware.RedirectMiddleware` to `settings.MIDDLEWARE` before other middlewares.
- Run `python manage.py migrate`.
- Restart your application server.

## Testing

```bash
# clone repository
git clone https://github.com/fabiocaccamo/django-redirects.git && cd django-redirects

# create virtualenv and activate it
python -m venv venv && . venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt -r requirements-test.txt

# run tests
tox
# or
python setup.py test
# or
python -m django test --settings "tests.settings"
```

## License

Released under [MIT License](LICENSE.txt).

## Supporting

- :star: Star this project on [GitHub](https://github.com/fabiocaccamo/django-redirects)
- :octocat: Follow me on [GitHub](https://github.com/fabiocaccamo)
- :blue_heart: Follow me on [Twitter](https://twitter.com/fabiocaccamo)
- :moneybag: Sponsor me on [Github](https://github.com/sponsors/fabiocaccamo)

## See also

- [`django-admin-interface`](https://github.com/fabiocaccamo/django-admin-interface) - the default admin interface made customizable by the admin itself. popup windows replaced by modals. 🧙 ⚡

- [`django-colorfield`](https://github.com/fabiocaccamo/django-colorfield) - simple color field for models with a nice color-picker in the admin. 🎨

- [`django-extra-settings`](https://github.com/fabiocaccamo/django-extra-settings) - config and manage typed extra settings using just the django admin. ⚙️

- [`django-maintenance-mode`](https://github.com/fabiocaccamo/django-maintenance-mode) - shows a 503 error page when maintenance-mode is on. 🚧 🛠️

- [`django-treenode`](https://github.com/fabiocaccamo/django-treenode) - probably the best abstract model / admin for your tree based stuff. 🌳

- [`python-benedict`](https://github.com/fabiocaccamo/python-benedict) - dict subclass with keylist/keypath support, I/O shortcuts (base64, csv, json, pickle, plist, query-string, toml, xml, yaml) and many utilities. 📘

- [`python-codicefiscale`](https://github.com/fabiocaccamo/python-codicefiscale) - encode/decode Italian fiscal codes - codifica/decodifica del Codice Fiscale. 🇮🇹 💳

- [`python-fontbro`](https://github.com/fabiocaccamo/python-fontbro) - friendly font operations. 🧢

- [`python-fsutil`](https://github.com/fabiocaccamo/python-fsutil) - file-system utilities for lazy devs. 🧟‍♂️
