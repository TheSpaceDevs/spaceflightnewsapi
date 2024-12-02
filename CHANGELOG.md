# CHANGELOG


## v4.16.4 (2024-11-22)

### Chores

- Update harvester dependency version to 0.9.0 in pyproject.toml and uv.lock
  ([`83150a0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/83150a07661d8a6470121b70aab9d02220579ff9))


## v4.16.3 (2024-11-21)

### Chores

- Package updates
  ([`b62599a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b62599a3e5ef185d971a5a7ebd5c780d15310f33))


## v4.16.2 (2024-11-20)

### Refactoring

- Simplify existence checks for articles, blogs, and reports by removing title filter
  ([`05748a6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/05748a641ee26c052d63b5df6495856a0bf7aeb8))


## v4.16.1 (2024-11-19)

### Chores

- Update harvester dependency version to 0.7.0 in pyproject.toml and uv.lock
  ([`49c2f98`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/49c2f986a00e03b75004fe874f9f86dd240955ab))

- Revert "feat: update Dockerfile to install Google Chrome and wget (#3623)"
  ([#3624](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3624),
  [`d455fef`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d455fef5197a4d42f62b1f41827057dbaf7cbbba))

This reverts commit dcd179dee3aaaded83a25777b44c9c0e5c103d8d.

- Remove AMQP configuration from .env.example and update Dockerfile to use apt-get upgrade
  ([`82bb1b3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/82bb1b3ad12e8a1a42fa24b824d3beec75029092))

### Features

- Update Dockerfile to install Google Chrome and wget
  ([#3623](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3623),
  [`dcd179d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/dcd179dee3aaaded83a25777b44c9c0e5c103d8d))

* feat: update Dockerfile to install Google Chrome and wget

* chore: update harvester dependency to version 0.5.0 in pyproject.toml and uv.lock

### Refactoring

- Change log level from info to debug for existing blog and report checks
  ([#3622](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3622),
  [`2ac68b8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2ac68b8234f463e18047df86bd76382e446586dd))

* refactor: change log level from info to debug for existing blog and report checks

* chore: package updates


## v4.16.0 (2024-11-18)

### Bug Fixes

- Docker build ([#3621](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3621),
  [`561b279`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/561b2792d7d3a140a3898381881552c36d903075))

* feat: add repository credentials as inputs for build-image action

* feat: optimize Dockerfile by adding multi-stage build for improved image size

### Chores

- Add UV_INDEX_TSD credentials to GitHub workflows for enhanced security
  ([`a013715`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a013715bb71006da0fd4960b96d8b34bf745c6e5))

- **deps**: Bump mikepenz/action-junit-report from 4 to 5
  ([#3618](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3618),
  [`28a0543`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/28a0543929aca9db1c51d8ec0695139da2e39324))

### Features

- Add repository credentials as inputs for build-image action
  ([#3620](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3620),
  [`cc14fe4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/cc14fe4b7bf31eeb023ea2eb413c617012351479))

- Add harvester & django-admin commands
  ([#3619](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3619),
  [`b17a498`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b17a49846eb98f4a30c980761775849fca4714c1))

* chore: remove deprecated importer

* feat: add the new importer app

* feat: add uv variables for private packages

* feat: new importer app with the harvester lib

* feat: add logging configuration to settings

* chore: update pre-commit hooks to latest versions

* feat: implement news processing commands with logging

* feat: add harvester dependency and configure uv sources

* feat: enhance news processing with blog and report handling, improve logging

* refactor: optimize news site retrieval by caching news_sites query

* refactor: remove Celery integration and add ll commands

* refactor: remove timeout from client options and set it directly in httpx.Client

* refactor: remove timeout from client options to comply with security guidelines

* chore: add UV_INDEX_TSD credentials to GitHub workflows for enhanced security

* refactor: remove Makefile as it is no longer needed

* chore: add UV_INDEX_TSD credentials to setup-python action for enhanced security

* chore: add registry credentials inputs to setup-python action for improved security

* chore: Revert "chore: add registry credentials inputs to setup-python action for improved
  security"

This reverts commit 18c5a670450606fbe0c65cbc770f9f0a1f9010bf.

* chore: Revert "chore: add UV_INDEX_TSD credentials to setup-python action for enhanced security"

This reverts commit 47769de0472e5927c4b0ad1a99bd4d640745c098.

* chore: update setup-python action for improved security and credential management

* chore: update UV version and action reference in setup-python action

* chore: remove unused AMQP settings from configuration


## v4.15.1 (2024-11-03)

### Chores

- Update dependencies for improved performance
  ([`b3e7791`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b3e77918fa253459749819b063d9648694489296))

- Remove logfire ([#3616](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3616),
  [`a73ecdb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a73ecdb5c723d7d9e649c836d3a7696db9fbb849))


## v4.14.1 (2024-10-11)

### Bug Fixes

- Revert "chore: move to file based version (#3612)"
  ([#3613](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3613),
  [`8f547f1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8f547f1beb913299c939e9135153e189c35626f6))

This reverts commit efe115308501d033e8738495f3af82ea9b9504ea.

### Chores

- Move to file based version ([#3612](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3612),
  [`efe1153`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/efe115308501d033e8738495f3af82ea9b9504ea))

* chore: Update project configuration and dependencies

- Remove unused build-system configuration - Add version.py file to store project version - Update
  usage of importlib.metadata to use __version__ from version.py - Update uv.lock to use virtual
  source for snapy package

* chore: Update version in src/version.py

* chore: Update test workflow and mypy configuration

* chore: Update pytest configuration and add pythonpath to pyproject.toml

- Update django-stubs-ext to version 4.2.7
  ([#3611](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3611),
  [`2404866`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2404866202ccf4da93f0c2c0cd1341a6d7a6a0e5))

- Add migrate command to Makefile
  ([#3610](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3610),
  [`0c6ce30`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0c6ce307af3c150ab416bb38458d333e99ac9248))

- Src layout ([#3609](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3609),
  [`253df3b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/253df3b6dec512e7ffd36dda320a08a3b41fe457))

* feat: add profiles to docker-compose services

Add the "profiles" configuration to the docker-compose services for consuming, beat, and worker.
  This allows for better management and customization of the services.

Refactor the docker-compose.yml file to include the "profiles" option with the value "all" for each
  service.

Closes #<issue_number>

* feat: going to a src layout

* chore: making life a bit easier

* refactor: update exclude path for ruff linting

* refactor: update Dockerfile to include src directory

* refactor: remove unnecessary VSCode configuration files

* refactor: remove CodSpeed benchmark workflow

### Features

- Start using uv ([#3606](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3606),
  [`81c7c60`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/81c7c603f566142646912fb805ae33eb8171ccd8))

* feat: start using uv

* chore: update workflows to use uv

* chore: update project name to "spaceflightnewsapi"

* chore: update project name to "snapy"

* chore: Update Dockerfile to use uv for project dependencies

* chore: Update Dockerfile to use uv for project dependencies

* chore: Update workflows to use uv for dependency management

* chore: Update Python version in production and staging workflows

* chore: Update version in pyproject.toml using inputs.version


## v4.14.0 (2024-09-16)

### Chores

- **deps**: Bump the package-updates group with 3 updates
  ([#3605](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3605),
  [`5f78229`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5f78229457832f9db8323bdeaf86f567bb52adda))

Bumps the package-updates group with 3 updates: [boto3](https://github.com/boto/boto3),
  [logfire](https://github.com/pydantic/logfire) and [ruff](https://github.com/astral-sh/ruff).

Updates `boto3` from 1.35.18 to 1.35.19 - [Release notes](https://github.com/boto/boto3/releases) -
  [Commits](https://github.com/boto/boto3/compare/1.35.18...1.35.19)

Updates `logfire` from 0.51.0 to 0.52.0 - [Release
  notes](https://github.com/pydantic/logfire/releases) -
  [Changelog](https://github.com/pydantic/logfire/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pydantic/logfire/compare/v0.51.0...v0.52.0)

Updates `ruff` from 0.6.4 to 0.6.5 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.4...0.6.5)

--- updated-dependencies: - dependency-name: boto3 dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: package-updates - dependency-name: logfire
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  package-updates - dependency-name: ruff dependency-type: direct:development update-type:
  version-update:semver-patch dependency-group: package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

### Features

- Add environment variable for Sentry environment
  ([#3604](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3604),
  [`86ab9e2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/86ab9e2811aed05b7939d233f00a67b2eaaa2a31))


## v4.13.0 (2024-09-13)

### Chores

- **deps**: Update logfire to version 0.51.0
  ([`24023bc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/24023bce0e18843c8b76246b78c08a4f8c01f69d))

- **deps**: Bump the package-updates group with 6 updates
  ([#3603](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3603),
  [`d3530d6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d3530d6252034ddf05413b56e5ac86ff148b854a))

- **deps**: Bump the package-updates group with 4 updates
  ([#3602](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3602),
  [`b08ab11`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b08ab1120875ec8aa8549cd5cb8c6bdad488edfd))

- **deps**: Bump the package-updates group with 4 updates
  ([#3601](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3601),
  [`af0346b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/af0346b74c132d5a0f5cbdf55797eae615ce9ac2))

Bumps the package-updates group with 4 updates:
  [django-celery-beat](https://github.com/celery/django-celery-beat),
  [boto3](https://github.com/boto/boto3), [logfire](https://github.com/pydantic/logfire) and
  [ruff](https://github.com/astral-sh/ruff).

Updates `django-celery-beat` from 2.6.0 to 2.7.0 - [Release
  notes](https://github.com/celery/django-celery-beat/releases) -
  [Changelog](https://github.com/celery/django-celery-beat/blob/main/Changelog) -
  [Commits](https://github.com/celery/django-celery-beat/compare/v2.6.0...v2.7.0)

Updates `boto3` from 1.35.0 to 1.35.5 - [Release notes](https://github.com/boto/boto3/releases) -
  [Commits](https://github.com/boto/boto3/compare/1.35.0...1.35.5)

Updates `logfire` from 0.50.1 to 0.51.0 - [Release
  notes](https://github.com/pydantic/logfire/releases) -
  [Changelog](https://github.com/pydantic/logfire/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pydantic/logfire/compare/v0.50.1...v0.51.0)

Updates `ruff` from 0.6.1 to 0.6.2 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.1...0.6.2)

--- updated-dependencies: - dependency-name: django-celery-beat dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  boto3 dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: package-updates - dependency-name: logfire dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name: ruff
  dependency-type: direct:development update-type: version-update:semver-patch dependency-group:
  package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

### Features

- Add health checks ([#3586](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3586),
  [`5cac9f3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5cac9f3d87a5130dfe82ea2155f4d0b181a486c4))

* feat: add health checks

* chore: Remove unused psycopg2_binary packages

* chore(deps): bump the package-updates group with 4 updates (#3602)

* chore(deps): bump the package-updates group with 6 updates (#3603)

* refactor: Optimize code for better performance

* chore(deps): bump the package-updates group with 6 updates (#3603)

---------

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>


## v4.12.3 (2024-08-23)

### Chores

- **deps**: Bump the package-updates group with 4 updates
  ([#3600](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3600),
  [`3e74c91`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3e74c9124bc54982242caf8b12db410353403260))

Bumps the package-updates group with 4 updates:
  [markdown](https://github.com/Python-Markdown/markdown),
  [sentry-sdk](https://github.com/getsentry/sentry-python), [boto3](https://github.com/boto/boto3)
  and [ruff](https://github.com/astral-sh/ruff).

Updates `markdown` from 3.6 to 3.7 - [Release
  notes](https://github.com/Python-Markdown/markdown/releases) -
  [Changelog](https://github.com/Python-Markdown/markdown/blob/master/docs/changelog.md) -
  [Commits](https://github.com/Python-Markdown/markdown/compare/3.6...3.7)

Updates `sentry-sdk` from 2.12.0 to 2.13.0 - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/2.12.0...2.13.0)

Updates `boto3` from 1.34.158 to 1.35.0 - [Release notes](https://github.com/boto/boto3/releases) -
  [Commits](https://github.com/boto/boto3/compare/1.34.158...1.35.0)

Updates `ruff` from 0.5.7 to 0.6.1 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.7...0.6.1)

--- updated-dependencies: - dependency-name: markdown dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  sentry-sdk dependency-type: direct:production update-type: version-update:semver-minor
  dependency-group: package-updates - dependency-name: boto3 dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name: ruff
  dependency-type: direct:development update-type: version-update:semver-minor dependency-group:
  package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>


## v4.12.2 (2024-08-18)

### Features

- Add lazy loading to admin ([#3598](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3598),
  [`0a1e91d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0a1e91de40f6502399eddff48deb3496923b5c21))


## v4.12.1 (2024-08-16)

### Chores

- Revert log settings to defaults
  ([#3597](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3597),
  [`250dcc6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/250dcc6e7ebbad00e6d5e46c3ca73dd362d314e2))


## v4.12.0 (2024-08-16)

### Chores

- **deps**: Bump the package-updates group with 6 updates
  ([#3596](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3596),
  [`86f0b94`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/86f0b94b195c78a9d9117a2d6760baf722909c75))

Bumps the package-updates group with 6 updates:

| Package | From | To | | --- | --- | --- | | [django](https://github.com/django/django) | `4.2.14`
  | `4.2.15` | | [pyyaml](https://github.com/yaml/pyyaml) | `6.0.1` | `6.0.2` | |
  [gunicorn](https://github.com/benoitc/gunicorn) | `22.0.0` | `23.0.0` | |
  [boto3](https://github.com/boto/boto3) | `1.34.153` | `1.34.158` | |
  [logfire](https://github.com/pydantic/logfire) | `0.48.1` | `0.50.1` | |
  [ruff](https://github.com/astral-sh/ruff) | `0.5.6` | `0.5.7` |

Updates `django` from 4.2.14 to 4.2.15 -
  [Commits](https://github.com/django/django/compare/4.2.14...4.2.15)

Updates `pyyaml` from 6.0.1 to 6.0.2 - [Release notes](https://github.com/yaml/pyyaml/releases) -
  [Changelog](https://github.com/yaml/pyyaml/blob/main/CHANGES) -
  [Commits](https://github.com/yaml/pyyaml/compare/6.0.1...6.0.2)

Updates `gunicorn` from 22.0.0 to 23.0.0 - [Release
  notes](https://github.com/benoitc/gunicorn/releases) -
  [Commits](https://github.com/benoitc/gunicorn/compare/22.0.0...23.0.0)

Updates `boto3` from 1.34.153 to 1.34.158 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.153...1.34.158)

Updates `logfire` from 0.48.1 to 0.50.1 - [Release
  notes](https://github.com/pydantic/logfire/releases) -
  [Changelog](https://github.com/pydantic/logfire/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pydantic/logfire/compare/v0.48.1...v0.50.1)

Updates `ruff` from 0.5.6 to 0.5.7 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.6...0.5.7)

--- updated-dependencies: - dependency-name: django dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: package-updates - dependency-name: pyyaml
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  package-updates - dependency-name: gunicorn dependency-type: direct:production update-type:
  version-update:semver-major dependency-group: package-updates - dependency-name: boto3
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  package-updates - dependency-name: logfire dependency-type: direct:production update-type:
  version-update:semver-minor dependency-group: package-updates - dependency-name: ruff
  dependency-type: direct:development update-type: version-update:semver-patch dependency-group:
  package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump django from 4.2.14 to 4.2.15
  ([#3595](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3595),
  [`5b6b1be`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5b6b1be9d84667470db24cb38227c07f3ac0fb9c))

Bumps [django](https://github.com/django/django) from 4.2.14 to 4.2.15. -
  [Commits](https://github.com/django/django/compare/4.2.14...4.2.15)

--- updated-dependencies: - dependency-name: django dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>


## v4.11.0 (2024-08-05)

### Chores

- **deps**: Bump the package-updates group with 6 updates
  ([#3594](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3594),
  [`fefc21a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fefc21a479069911e805e8947a4f6784f6fd0525))

Bumps the package-updates group with 6 updates:

| Package | From | To | | --- | --- | --- | |
  [django-filter](https://github.com/carltongibson/django-filter) | `24.2` | `24.3` | |
  [sentry-sdk](https://github.com/getsentry/sentry-python) | `2.11.0` | `2.12.0` | |
  [boto3](https://github.com/boto/boto3) | `1.34.149` | `1.34.153` | |
  [logfire](https://github.com/pydantic/logfire) | `0.48.0` | `0.48.1` | |
  [coverage](https://github.com/nedbat/coveragepy) | `7.6.0` | `7.6.1` | |
  [ruff](https://github.com/astral-sh/ruff) | `0.5.5` | `0.5.6` |

Updates `django-filter` from 24.2 to 24.3 - [Release
  notes](https://github.com/carltongibson/django-filter/releases) -
  [Changelog](https://github.com/carltongibson/django-filter/blob/main/CHANGES.rst) -
  [Commits](https://github.com/carltongibson/django-filter/compare/24.2...24.3)

Updates `sentry-sdk` from 2.11.0 to 2.12.0 - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/2.11.0...2.12.0)

Updates `boto3` from 1.34.149 to 1.34.153 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.149...1.34.153)

Updates `logfire` from 0.48.0 to 0.48.1 - [Release
  notes](https://github.com/pydantic/logfire/releases) -
  [Changelog](https://github.com/pydantic/logfire/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pydantic/logfire/compare/v0.48.0...v0.48.1)

Updates `coverage` from 7.6.0 to 7.6.1 - [Release
  notes](https://github.com/nedbat/coveragepy/releases) -
  [Changelog](https://github.com/nedbat/coveragepy/blob/master/CHANGES.rst) -
  [Commits](https://github.com/nedbat/coveragepy/compare/7.6.0...7.6.1)

Updates `ruff` from 0.5.5 to 0.5.6 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.5...0.5.6)

--- updated-dependencies: - dependency-name: django-filter dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  sentry-sdk dependency-type: direct:production update-type: version-update:semver-minor
  dependency-group: package-updates - dependency-name: boto3 dependency-type: direct:production
  update-type: version-update:semver-patch dependency-group: package-updates - dependency-name:
  logfire dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: package-updates - dependency-name: coverage dependency-type: direct:development
  update-type: version-update:semver-patch dependency-group: package-updates - dependency-name: ruff
  dependency-type: direct:development update-type: version-update:semver-patch dependency-group:
  package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump CodSpeedHQ/action from 2 to 3
  ([#3592](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3592),
  [`3b01de5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3b01de558304183da55388d31ffa38ee7d099703))

- **deps**: Bump the package-updates group with 6 updates
  ([#3591](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3591),
  [`14ad9c5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/14ad9c5f8ec7283989a9c7843d3ab88982aa6bc1))

### Features

- Favicon for admin ([#3593](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3593),
  [`9d4ddbf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9d4ddbf45db1da008862080cddfe29b4b52d9f6a))


## v4.10.0 (2024-07-24)

### Chores

- **deps**: Bump the package-updates group with 5 updates
  ([#3588](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3588),
  [`3c1704e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3c1704ec868e3b747013076b2056905b33904e2b))

Bumps the package-updates group with 5 updates:

| Package | From | To | | --- | --- | --- | |
  [sentry-sdk](https://github.com/getsentry/sentry-python) | `2.9.0` | `2.10.0` | |
  [boto3](https://github.com/boto/boto3) | `1.34.144` | `1.34.145` | |
  [logfire](https://github.com/pydantic/logfire) | `0.46.1` | `0.47.0` | |
  [pytest](https://github.com/pytest-dev/pytest) | `8.2.2` | `8.3.1` | |
  [ruff](https://github.com/astral-sh/ruff) | `0.5.2` | `0.5.4` |

Updates `sentry-sdk` from 2.9.0 to 2.10.0 - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/2.9.0...2.10.0)

Updates `boto3` from 1.34.144 to 1.34.145 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.144...1.34.145)

Updates `logfire` from 0.46.1 to 0.47.0 - [Release
  notes](https://github.com/pydantic/logfire/releases) -
  [Changelog](https://github.com/pydantic/logfire/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pydantic/logfire/compare/v0.46.1...v0.47.0)

Updates `pytest` from 8.2.2 to 8.3.1 - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.2.2...8.3.1)

Updates `ruff` from 0.5.2 to 0.5.4 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.2...0.5.4)

--- updated-dependencies: - dependency-name: sentry-sdk dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  boto3 dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: package-updates - dependency-name: logfire dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  pytest dependency-type: direct:development update-type: version-update:semver-minor
  dependency-group: package-updates - dependency-name: ruff dependency-type: direct:development
  update-type: version-update:semver-patch dependency-group: package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump the package-updates group with 5 updates
  ([#3587](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3587),
  [`67457bc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/67457bc596ce0cd886f7a7e94b7554c3dea5744f))

Bumps the package-updates group with 5 updates:

| Package | From | To | | --- | --- | --- | |
  [sentry-sdk](https://github.com/getsentry/sentry-python) | `2.7.1` | `2.9.0` | |
  [django-storages](https://github.com/jschneier/django-storages) | `1.14.3` | `1.14.4` | |
  [boto3](https://github.com/boto/boto3) | `1.34.140` | `1.34.144` | |
  [coverage](https://github.com/nedbat/coveragepy) | `7.5.4` | `7.6.0` | |
  [ruff](https://github.com/astral-sh/ruff) | `0.5.1` | `0.5.2` |

Updates `sentry-sdk` from 2.7.1 to 2.9.0 - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/2.7.1...2.9.0)

Updates `django-storages` from 1.14.3 to 1.14.4 -
  [Changelog](https://github.com/jschneier/django-storages/blob/master/CHANGELOG.rst) -
  [Commits](https://github.com/jschneier/django-storages/compare/1.14.3...1.14.4)

Updates `boto3` from 1.34.140 to 1.34.144 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.140...1.34.144)

Updates `coverage` from 7.5.4 to 7.6.0 - [Release
  notes](https://github.com/nedbat/coveragepy/releases) -
  [Changelog](https://github.com/nedbat/coveragepy/blob/master/CHANGES.rst) -
  [Commits](https://github.com/nedbat/coveragepy/compare/7.5.4...7.6.0)

Updates `ruff` from 0.5.1 to 0.5.2 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.1...0.5.2)

--- updated-dependencies: - dependency-name: sentry-sdk dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: package-updates - dependency-name:
  django-storages dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: package-updates - dependency-name: boto3 dependency-type: direct:production
  update-type: version-update:semver-patch dependency-group: package-updates - dependency-name:
  coverage dependency-type: direct:development update-type: version-update:semver-minor
  dependency-group: package-updates - dependency-name: ruff dependency-type: direct:development
  update-type: version-update:semver-patch dependency-group: package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- Add pytest-codspeed for benchmarking
  ([#3585](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3585),
  [`1e76eff`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1e76eff862654670cca43cc3ce99410516ebe8e5))

* chore: Add pytest-codspeed for benchmarking (#3585)

* chore: Add benchmarking with pytest-codspeed for info and reports endpoints

* chore: Add CSRF_TRUSTED_ORIGINS=localhost to pyproject.toml

* chore: Update environment variables in codspeed.yml and pyproject.toml

* fix: correct pytest command

* chore: update the name

* chore: clean-up

### Features

- **#3589**: Optimize admin querysets
  ([#3590](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3590),
  [`c689638`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c68963824c07f39d9aca35395771938f8d227b5d))

* feat(#3589): optimize admin querysets

* chore: add docstrings and cleanup

---------

Co-authored-by: Derk Weijers <derk@weijers.xyz>


## v4.9.1 (2024-07-11)

### Chores

- Update deployment workflows to use GITHUB_TOKEN instead of CR_PAT
  ([`ebc38e7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ebc38e7b3057c5ebb92b4b832047f3f338030fe0))


## v4.9.0 (2024-07-11)

### Bug Fixes

- Cleanup action ([#3582](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3582),
  [`4210d35`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4210d3533dd96131dbc43f9f8135b20368f45a8f))

* chore: Add write permissions to delete_runs job in cleanup workflow

* chore: Remove token from cleanup workflow

Remove the token from the cleanup workflow to ensure that it is not exposed in the repository. The
  token was previously used for authentication but is no longer necessary. This change improves the
  security of the repository.

* chore: Schedule cleanup tasks to run daily at midnight

To automate the cleanup tasks, the cleanup workflow has been updated to include a schedule that runs
  the workflow daily at midnight. This change ensures that the cleanup tasks are executed regularly,
  improving the maintenance of the repository.

### Chores

- Update deployment workflows to use GITHUB_TOKEN instead of CR_PAT
  ([#3584](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3584),
  [`0dbfba1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0dbfba1df3c90f753ab43d4afe025b654f007741))

- Add logfire library for Django logging
  ([#3583](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3583),
  [`dc0db25`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/dc0db25d30b51941a6b0183348cd72b08e9271e8))

- **deps**: Bump django from 4.2.13 to 4.2.14
  ([#3581](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3581),
  [`4e002c2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4e002c24bd9e4bead2f4149569d91e78710b1a2f))

- **deps**: Bump the package-updates group with 2 updates
  ([#3580](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3580),
  [`a078bc1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a078bc1647af364f2febb90c55a358f02f35a887))

Bumps the package-updates group with 2 updates: [boto3](https://github.com/boto/boto3) and
  [ruff](https://github.com/astral-sh/ruff).

Updates `boto3` from 1.34.136 to 1.34.140 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.136...1.34.140)

Updates `ruff` from 0.5.0 to 0.5.1 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.0...0.5.1)

--- updated-dependencies: - dependency-name: boto3 dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: package-updates - dependency-name: ruff
  dependency-type: direct:development update-type: version-update:semver-patch dependency-group:
  package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump certifi from 2024.6.2 to 2024.7.4
  ([#3579](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3579),
  [`430463d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/430463d05d1ea733cedd61b9668bc27543f2a788))

Bumps [certifi](https://github.com/certifi/python-certifi) from 2024.6.2 to 2024.7.4. -
  [Commits](https://github.com/certifi/python-certifi/compare/2024.06.02...2024.07.04)

--- updated-dependencies: - dependency-name: certifi dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- Update Python and Poetry setup in tests workflow
  ([#3578](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3578),
  [`7ed7fcf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7ed7fcf686e7334de29c1ad226c7abb19a181089))

* chore: Update Python and Poetry setup in tests workflow

* chore: Update Python and Poetry setup in tests workflow

* chore: Update linters and set SECRET_KEY in tests workflow

* chore: Update tests workflow with environment variables

* chore: Update tests workflow with secrets and environment variables

* chore: Update tests workflow with CSRF_TRUSTED_ORIGIN environment variable

* fix: fix version that's being tested

* chore: Update Python and Poetry setup in tests workflow

* chore: Update tests workflow to install project in editable mode

* chore: Update tests workflow to include CELERY_BROKER_URL environment variable

* chore: Update LL_URL with default value in settings.py

* chore: Update tests workflow to include project installation in editable mode

* chore: Update tests workflow to include SENTRY_DSN environment variable


## v4.8.3 (2024-07-02)

### Chores

- Update workflow name to reflect deployment to staging environment
  ([`a2ed519`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a2ed51953cb7e5c768cecc458fee8240eede1ca5))

- Refactor Dockerfile for improved file copying and project installation
  ([#3577](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3577),
  [`38a5392`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/38a5392a8560b364a03459a37875f42a35d574bf))


## v4.8.2 (2024-07-02)

### Chores

- Refactor Dockerfile for improved file copying and project installation
  ([`b070e27`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b070e27abd33fd9bfee20631d8af1c521c63df68))

- Copy files to temporary directory for build context
  ([`b3faf29`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b3faf29372969023c61f5f2d38ffaf6438b11dbf))

- Bump version to ${{ inputs.version }}
  ([`e93ac33`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e93ac33b5898edab1f073cf31b4c38a1803fb8a9))

- Load all
  ([`d96d21f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d96d21f094ae8752392383d41adb4b6675b24df4))

- Commit through an action
  ([`3f21753`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3f217531c8ff6f46c04fdc7af06906b5e3f8d80b))

- Also commit so it gets picked up by the build context
  ([`00d2ba5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/00d2ba5f64bb2cc09740e70edf185a9cafdac253))


## v4.8.1 (2024-07-02)

### Chores

- Update Dockerfile to include manage.py in file copying
  ([`cf10c86`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/cf10c864a01fbc29476eeca0fa16c9f42112a490))

- Remove unused files and configurations from repository
  ([`66d8d0f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/66d8d0fb4c6223e75c815ea554bdf3580cd35a71))

- Update Dockerfile to include README.md in file copying
  ([`9f83d32`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9f83d322d4582f7dc4ea0b02fef57cad9baed79e))

- Update Dockerfile to use COPY instead of ADD for file copying
  ([`9f30a2d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9f30a2de4337864ca4cd7244db419e9d833ed815))


## v4.8.0 (2024-07-01)

### Bug Fixes

- Fix n-related issue
  ([`7bd8a78`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7bd8a78bb5580e3fad0b4269ea6d656b240fa230))

- Use the correct user and db
  ([`38faffd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/38faffd732fb20f5375d7119248f2c227c6202fc))

- **admin**: Add `image_url` field to news items admin
  ([`81a621b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/81a621b5ca3782467645a60b661b39d15692b79d))

- Make mypy happy again
  ([`f3ff85b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f3ff85b137685f0ae089e54c579041ed1492c058))

- Call to `super()` as required by the linter
  ([`2a799a6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2a799a6c918e2544bd8d7f9b4aed0a53ab2f8d55))

- Search on id as well
  ([`770652b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/770652b0373c5dc2563d28de2533e30c31c87a87))

- Remove space from updated_at field
  ([`6bd3188`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6bd31887e25b287fc5c23dd2bdd3476db209aa78))

- Remove black and use ruff
  ([`3a7b057`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3a7b05704015c35fab5199bc453b01a1933664f4))

- Get news_site by primary key
  ([`2d0f0af`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2d0f0afa1205cf2af1420646f77a66a8cc9fd9fd))

- Test match the new code
  ([`9154e64`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9154e642c6cfd202a113ebb314dd34c5cf17b7df))

- Content not saving
  ([`7f6f585`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7f6f585aba6c607ce1415f5c5402b5154afe9830))

- Missing deps
  ([`2fb6b7b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2fb6b7b653aa19b9891ad7384f1eda2dff716385))

- Automatically set the date when not present
  ([`b53ffea`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b53ffeaf5c2acee3ad33cfefef2e0ca6fa086f38))

- Cleanup
  ([`59e171b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/59e171b9c0ef021aa72acfdc2a4b17451face1f9))

- Typo ([#3428](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3428),
  [`5e6c80b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5e6c80b5705ed97e12c67ba7544a5217d02b7776))

- Handle non existing launches when syncing
  ([#3425](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3425),
  [`d82aeeb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d82aeeb8dcdda0ca92adee7e7e5c1ebd554cce62))

- Fix ll url parsing ([#3417](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3417),
  [`22d3e58`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/22d3e58bd9ab82895293e587a59187abb3acb7cd))

- Minio ([#3400](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3400),
  [`a4725e4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a4725e4713217b62aba8fe4c01c82b848e6e207c))

- Default debug is false
  ([`b6a100a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b6a100ac39a5e7e77a136a90e3c45c450e83b74f))

- Link back to the org profile page
  ([#3344](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3344),
  [`a8707a3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a8707a3bb118f22edbdb41453642bf2e768a2a5c))

- Use the tag as version in the compose file
  ([#3335](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3335),
  [`6338ba3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6338ba30bef31ab3d4257afe01b6c9aa1889f920))

- Readme updates
  ([`7b50237`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7b50237a1f74de9557302654f30958fb99fbed81))

- Back to minio for now
  ([`fa48041`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fa480416fb611fb4adb79209fab1ecf418718019))

- Back to minio for now
  ([`4153864`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/415386454c99fbf7ea8a32c785bae39150f4b99e))

- Set the max limit to 500. fixes #857
  ([#862](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/862),
  [`5640b21`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5640b21671eee5a0dc3562e0428a5a2981d18d79))

- Correct health check for postgres
  ([#242](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/242),
  [`9863f76`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9863f76ef439f9a77551fd1a99b52f5bc253d1e0))

- Move to python 3.11
  ([`3fdb362`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3fdb362809319acb136ba45bf83f4d46b7420a64))

- Updated readme through a pr
  ([`b3f4242`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b3f4242e30cc837c0e672849bea0a55462e28700))

- Updated readme through a pr
  ([`200e293`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/200e29398c46eb3d67dd417b43f8c31c6c01847b))

- Also search on news_site__names
  ([#220](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/220),
  [`44efd0e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/44efd0e2e74f9644038050afa185bc569034847a))

- Exposed Django port
  ([`e5f0790`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e5f0790d26958512d83eb77bf6d0d98a11c53b49))

- **snapy/settings.py**: Set the correct timezone
  ([`278b7b1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/278b7b1273df6f96997f082381899e9b19a13278))

### Build System

- **deps-dev**: Bump ruff from 0.1.2 to 0.1.3
  ([#3367](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3367),
  [`e6839ba`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e6839bac96d023b9156c9488c7b0516957684251))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.1.2 to 0.1.3. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.1.2...v0.1.3)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:development update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps-dev**: Bump pytest-django from 4.5.2 to 4.6.0
  ([#3368](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3368),
  [`71ab66d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/71ab66d0fd478c52ffa3bed86cf5405cff0b629b))

Bumps [pytest-django](https://github.com/pytest-dev/pytest-django) from 4.5.2 to 4.6.0. - [Release
  notes](https://github.com/pytest-dev/pytest-django/releases) -
  [Changelog](https://github.com/pytest-dev/pytest-django/blob/master/docs/changelog.rst) -
  [Commits](https://github.com/pytest-dev/pytest-django/compare/v4.5.2...v4.6.0)

--- updated-dependencies: - dependency-name: pytest-django dependency-type: direct:development
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps-dev**: Bump pytest-env from 1.1.0 to 1.1.1
  ([#3369](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3369),
  [`215d9ad`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/215d9adf3eef54959be6e168706c8036aff17d6a))

Bumps [pytest-env](https://github.com/pytest-dev/pytest-env) from 1.1.0 to 1.1.1. - [Release
  notes](https://github.com/pytest-dev/pytest-env/releases) -
  [Commits](https://github.com/pytest-dev/pytest-env/compare/1.1.0...1.1.1)

--- updated-dependencies: - dependency-name: pytest-env dependency-type: direct:development
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps-dev**: Bump djangorestframework-stubs from 3.14.3 to 3.14.4
  ([#3356](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3356),
  [`9432e7c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9432e7c9417263ab02e001412644eb711fa30caa))

Bumps [djangorestframework-stubs](https://github.com/typeddjango/djangorestframework-stubs) from
  3.14.3 to 3.14.4. - [Release
  notes](https://github.com/typeddjango/djangorestframework-stubs/releases) -
  [Commits](https://github.com/typeddjango/djangorestframework-stubs/compare/3.14.3...3.14.4)

--- updated-dependencies: - dependency-name: djangorestframework-stubs dependency-type:
  direct:development update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps-dev**: Bump black from 23.9.1 to 23.10.0
  ([#3355](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3355),
  [`0e08352`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0e083529b13d5cd88991eff7e3452530a0f0dac5))

Bumps [black](https://github.com/psf/black) from 23.9.1 to 23.10.0. - [Release
  notes](https://github.com/psf/black/releases) -
  [Changelog](https://github.com/psf/black/blob/main/CHANGES.md) -
  [Commits](https://github.com/psf/black/compare/23.9.1...23.10.0)

--- updated-dependencies: - dependency-name: black dependency-type: direct:development update-type:
  version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump markdown from 3.4.4 to 3.5
  ([#3349](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3349),
  [`04cd023`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/04cd02353d1b0109c81926120c148fcd4d7c94e1))

* build(deps): bump markdown from 3.4.4 to 3.5

Bumps [markdown](https://github.com/Python-Markdown/markdown) from 3.4.4 to 3.5. -
  [Changelog](https://github.com/Python-Markdown/markdown/blob/master/docs/changelog.md) -
  [Commits](https://github.com/Python-Markdown/markdown/compare/3.4.4...3.5)

--- updated-dependencies: - dependency-name: markdown dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

* chore: updated lock

---------

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com> Co-authored-by: Derk Weijers <derk@weijers.xyz>

- **deps-dev**: Bump django-stubs from 4.2.4 to 4.2.5
  ([#3350](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3350),
  [`643d5e8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/643d5e84ab408d9c9c6189311d535fe58f25bb9e))

Bumps [django-stubs](https://github.com/typeddjango/django-stubs) from 4.2.4 to 4.2.5. - [Release
  notes](https://github.com/typeddjango/django-stubs/releases) -
  [Commits](https://github.com/typeddjango/django-stubs/compare/4.2.4...4.2.5)

--- updated-dependencies: - dependency-name: django-stubs dependency-type: direct:development
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump sentry-sdk from 1.31.0 to 1.32.0
  ([#3348](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3348),
  [`7c4f328`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7c4f328f106cd269f9608a55f2b97f2d587a37e6))

Bumps [sentry-sdk](https://github.com/getsentry/sentry-python) from 1.31.0 to 1.32.0. - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/1.31.0...1.32.0)

--- updated-dependencies: - dependency-name: sentry-sdk dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump urllib3 from 2.0.6 to 2.0.7
  ([#3347](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3347),
  [`9c2af8a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9c2af8a0cb511c7c316a60d9cc17f7dd53c62292))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.6 to 2.0.7. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.0.6...2.0.7)

--- updated-dependencies: - dependency-name: urllib3 dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump django-cors-headers from 4.2.0 to 4.3.0
  ([#3346](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3346),
  [`7525e8f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7525e8fd3f91274779f8a45bfa01cf4fc24ffb8a))

Bumps [django-cors-headers](https://github.com/adamchainz/django-cors-headers) from 4.2.0 to 4.3.0.
  - [Changelog](https://github.com/adamchainz/django-cors-headers/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/adamchainz/django-cors-headers/compare/4.2.0...4.3.0)

--- updated-dependencies: - dependency-name: django-cors-headers dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps**: Bump urllib3 from 2.0.5 to 2.0.6
  ([#3322](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3322),
  [`f0daddc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f0daddc1bf75245f813d46a296c100ba442103fe))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.5 to 2.0.6. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/v2.0.5...2.0.6)

--- updated-dependencies: - dependency-name: urllib3 dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sentry-sdk from 1.23.1 to 1.25.0
  ([#524](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/524),
  [`d0edd21`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d0edd217864f6baa2e7d31c291570f85129be6de))

Bumps [sentry-sdk](https://github.com/getsentry/sentry-python) from 1.23.1 to 1.25.0. - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/1.23.1...1.25.0)

--- updated-dependencies: - dependency-name: sentry-sdk dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- Added github workflow logic
  ([`b00a238`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b00a238f81d4838da0bc4abb4ccbe9d40d39d118))

### Chores

- Update Dockerfile to include project installation in final image
  ([`eb83bbc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/eb83bbc439d29d16f21cd3f62fa0efa3544ef3d7))

- Update Django and Sentry configurations
  ([`78ac827`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/78ac82718467e7cb454eaf08f217b5d411b81904))

- Update Dockerfile to include image source label
  ([`d8b8278`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d8b8278fd976e3662a1856e67197025a9f13cc84))

- Update Python and Poetry setup in staging workflow
  ([`c47f92f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c47f92fcc2f1b11b0dcbe4c39a9d3272b6ec81dd))

- Remove unused services from docker-compose files
  ([`8872873`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8872873914aa729c0a00c6b66dcdd8fac85ae06a))

- Update staging workflow for k8s deployment
  ([`4b6b550`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4b6b550515d09e1f1719d28a83dbd699cdde0b49))

- Update staging workflow for k8s deployment
  ([`bd3a36f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/bd3a36fb81fed078f4447cb5bd9b23c680aec6e7))

- Update staging workflow for k8s deployment
  ([`631311e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/631311e43fbb3fa86d4c891b1b0a045246c8e50f))

- Update staging workflow for k8s deployment
  ([`c1a7825`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c1a7825bedfd215c7ce36168f72af061e10ad94f))

- Update staging workflow for k8s deployment
  ([`d14681b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d14681bdbc270b8a700d074b2433af41c9e88e4e))

- Update staging workflow for k8s deployment
  ([`b64085e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b64085e14028fa5d273620302d9a33b6ca0a5de2))

- Update staging workflow for k8s deployment
  ([`4ba87a1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4ba87a1ebd8d3150b80397bf37364940e69eb3ea))

- Update staging workflow for k8s deployment
  ([`22fcd46`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/22fcd460e883008a7947563eddccec7e07d77df0))

- Update staging workflow for k8s deployment
  ([`df21117`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/df2111772ea15bf8f14d18e8a701635aa145ddc8))

- Update staging workflow for k8s deployment
  ([`0d5fa54`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0d5fa54c463ca8ba32f9d133aeb592c8910041e1))

- Update staging workflow for k8s deployment
  ([`da518c8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/da518c819184376850bb3d8f35c6f1948d00ded6))

- Update staging workflow for k8s deployment
  ([`8247fde`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8247fde32399ae45df4771486f91555a064fdfee))

- Update staging workflow for k8s deployment
  ([`76b8a6d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/76b8a6ddb5bacd6c7ce664ac2e9c53d1804b8183))

- Update staging workflow for k8s deployment
  ([`6764bd8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6764bd81021af183d1c6f00ea1f2eef029efc0dd))

- Update staging workflow for k8s deployment
  ([`9d5f2ac`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9d5f2acddd5c4148253ca919fce626e2fb6d5e24))

- Update permissions in staging workflow for k8s deployment
  ([`521fd57`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/521fd57a7f6cd3e87d21ce28fdd02ded554ade16))

- Update staging workflow for k8s deployment
  ([`df1ac65`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/df1ac650225627a198eb5a89489e1c8901804351))

- Update staging workflow for k8s deployment
  ([`221bc42`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/221bc42a8b8356a2bc544e35a9cdf6bb6c4824bd))

- **deps**: Bump boto3 in the package-updates group
  ([#3576](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3576),
  [`fc4e92e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fc4e92e8f17294d06256678592e845697960b8fb))

Bumps the package-updates group with 1 update: [boto3](https://github.com/boto/boto3).

Updates `boto3` from 1.34.135 to 1.34.136 - [Release notes](https://github.com/boto/boto3/releases)
  - [Commits](https://github.com/boto/boto3/compare/1.34.135...1.34.136)

--- updated-dependencies: - dependency-name: boto3 dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com> Co-authored-by: Derk Weijers
  <derkweijers@users.noreply.github.com>

- **deps-dev**: Bump ruff ([#3575](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3575),
  [`b43a7d6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b43a7d6f9cc7c84c9ad1d61c91ef6fc683ceb49a))

Bumps the package-updates group with 1 update in the / directory:
  [ruff](https://github.com/astral-sh/ruff).

Updates `ruff` from 0.4.10 to 0.5.0 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.10...0.5.0)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:development update-type:
  version-update:semver-minor dependency-group: package-updates ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump docker/build-push-action from 5 to 6
  ([#3573](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3573),
  [`2b09363`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2b09363c377c417f0e66a42727dea9c287b12782))

Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 5 to 6. -
  [Release notes](https://github.com/docker/build-push-action/releases) -
  [Commits](https://github.com/docker/build-push-action/compare/v5...v6)

--- updated-dependencies: - dependency-name: docker/build-push-action dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- Version configs ([#3572](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3572),
  [`6ad86d5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6ad86d5ee7f92e2b0c4b9bda079ee5c285a09060))

* chore: group dependabot update

* chore: update django-stubs to version 4.2

* chore: update django-stubs to version 4.2

* chore: update pre-commit hooks and dependencies

- **deps-dev**: Bump ruff from 0.4.3 to 0.4.8
  ([#3561](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3561),
  [`e2bd7b6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e2bd7b6bb76208f9f72a84b4cef1a8b99224f02f))

- **deps**: Bump django from 4.2.12 to 4.2.13
  ([#3553](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3553),
  [`1bb1318`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1bb1318b247a183057a1bc7ccc7ff802e939a73a))

- **deps-dev**: Bump requests from 2.31.0 to 2.32.2
  ([#3563](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3563),
  [`62ea6ee`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/62ea6eeee15af684deff760f1ced3842182a00ff))

- **deps**: Bump sentry-sdk from 2.1.1 to 2.5.1
  ([#3562](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3562),
  [`7578dcb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7578dcb56c8cc986fb394b3f4ae7ae68b2908e41))

- **deps**: Bump boto3 from 1.34.99 to 1.34.108
  ([#3555](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3555),
  [`13ff9a8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/13ff9a82189e56d6ca47cc8944ea9d4f6a4b17dc))

Bumps [boto3](https://github.com/boto/boto3) from 1.34.99 to 1.34.108. - [Release
  notes](https://github.com/boto/boto3/releases) -
  [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst) -
  [Commits](https://github.com/boto/boto3/compare/1.34.99...1.34.108)

--- updated-dependencies: - dependency-name: boto3 dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sentry-sdk from 1.45.0 to 2.1.1
  ([#3549](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3549),
  [`c614b08`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c614b08618a16424888269b37d54290fa4f18beb))

Bumps [sentry-sdk](https://github.com/getsentry/sentry-python) from 1.45.0 to 2.1.1. - [Release
  notes](https://github.com/getsentry/sentry-python/releases) -
  [Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/getsentry/sentry-python/compare/1.45.0...2.1.1)

--- updated-dependencies: - dependency-name: sentry-sdk dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot]
  <49699333+dependabot[bot]@users.noreply.github.com>

- Reformat test ([#3548](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3548),
  [`74b59d1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/74b59d1aa97b63999a0a631ecd835ab5c0cbf468))

* chore: reformat test

* fix: add env variables

* chore: more envs

* chore: add services to the right job

* chore: add services to the right job

* chore: cleanup

* chore: cleanup

* chore: cleanup

* chore: cleanup

- Updated variables
  ([`defa92f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/defa92f276d5ab54096422459696bb87543b1cf9))

- **deps**: Bump django-filter from 23.5 to 24.2
  ([`59dc7fc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/59dc7fc4f2f87fd6dcc3981e68d566dffce07273))

Bumps [django-filter](https://github.com/carltongibson/django-filter) from 23.5 to 24.2. - [Release
  notes](https://github.com/carltongibson/django-filter/releases) -
  [Changelog](https://github.com/carltongibson/django-filter/blob/main/CHANGES.rst) -
  [Commits](https://github.com/carltongibson/django-filter/compare/23.5...24.2)

--- updated-dependencies: - dependency-name: django-filter dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Update dependency gunicorn to v22
  ([`6f0ddf2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6f0ddf241a787fe761141d5ad0cf3d0dbbc540cf))

- **deps**: Update dependency ruff to ^0.4.0
  ([`0d62e29`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0d62e29bda9fa9907f5999b9738603e0d4839330))

- **deps**: Update dependency boto3 to v1.34.88
  ([`cc22bd4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/cc22bd470cb3050f2770549813527a4c89702e87))

- **deps**: Update dependency celery to v5.4.0
  ([`90d2023`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/90d202378f3a56f6f6058b6933d22caedacb03d7))

- **deps**: Update dependency boto3 to v1.34.87
  ([`ff5e0a7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ff5e0a7f9075dd2eb2655b15fd69bb82aa63838d))

- **deps**: Update dependency boto3 to v1.34.86
  ([`f748a57`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f748a5727a16412c3958ffbb883c67b82f9852c9))

- **deps**: Lock file maintenance
  ([`bf3694d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/bf3694d58e84729ac754c292250c8b38de034d0b))

- **deps**: Update dependency ruff to v0.3.7
  ([`949b9ed`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/949b9edb34393f3efe46909db8b4f259177bf6cc))

- **deps**: Update dependency boto3 to v1.34.84
  ([`065a707`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/065a7071733ce45c3445dc9388937eb6a462b0f2))

- **deps**: Update dependency boto3 to v1.34.83
  ([`ea93795`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ea93795dffe00012a3bcb832793997f12bc5422e))

- **deps**: Update dependency sentry-sdk to v1.45.0
  ([`0e45d86`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0e45d86573a38069a405e9efeac5d58e25cd75d1))

- **deps**: Update dependency boto3 to v1.34.82
  ([`fc487f9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fc487f964dc208bd8e34b2f04616d3afde671127))

- **deps**: Update dependency boto3 to v1.34.81
  ([`ae2e1e4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ae2e1e48ba2cde33b80df8b560744dd85f281bab))

- **deps**: Update dependency boto3 to v1.34.80
  ([`c95ea4e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c95ea4ec698d217d1fd99a7ef06b47a30c020d34))

- **deps**: Lock file maintenance
  ([`626bd30`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/626bd30163ff1f430383c3461da7a7ba5d5757c6))

- **deps**: Update dependency boto3 to v1.34.79
  ([`66ea6bb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/66ea6bb10e2da993766e73920f57bcca10c8e841))

- **deps**: Update dependency boto3 to v1.34.78
  ([`b5be966`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b5be966c480593356ca3705cc3013d4d6d16bdfd))

- **deps**: Update dependency boto3 to v1.34.77
  ([`7500f54`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7500f54bf6c50a516f3fbf0dd30ee6aa91d1cc39))

- **deps**: Update dependency sentry-sdk to v1.44.1
  ([`4fb6741`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4fb6741954d93fe4cee59bf2fdc084fbefacff4d))

- **deps**: Update dependency boto3 to v1.34.76
  ([`3aa4415`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3aa44150596d6eed7b0faaa549e04ee43b8f44ab))

- **deps**: Update dependency drf-spectacular to v0.27.2
  ([`f4fbf2f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f4fbf2f905507e63cdbeabaf259b6a8af9183988))

- **deps**: Update dependency ruff to v0.3.5
  ([`b49df92`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b49df92c41c3232f6188f718bff2a1bd8d12f95d))

- **deps**: Update dependency sentry-sdk to v1.44.0
  ([`a0764af`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a0764afde56bff0816f442c83366ece25daad00b))

- **deps**: Update dependency pytest-cov to v5
  ([`6d90415`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6d9041529babc23dbd844b6756b96c75a077c48a))

- **deps**: Update dependency boto3 to v1.34.71
  ([`3b695e5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3b695e5d50af27c3525beda192c8d49bff59587b))

- **deps**: Update dependency django-filter to v24
  ([`4cb6c9f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4cb6c9f3823d7cae02bc2a3cd0b25c9470de4fca))

- Updates
  ([`81bba08`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/81bba08f9be3f54a122cf085cb3bf0009ccff37d))

- Cleanup
  ([`f8862a4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f8862a489fc9534800da5d3328f450ee47c39d03))

- Updated docker config
  ([`45600e6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/45600e64c1baa890e6c52744d64f33adaefe7659))

- Update all references to python 3.12
  ([`4c82e43`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4c82e4368ca1406306e74974a71addad701a605c))

- Restart db when needed
  ([`70243eb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/70243eb0a2d04db50ce4466ea3023123991e1ed7))

- **deps**: Update dependency boto3 to v1.34.70
  ([`6cfdb4d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6cfdb4d3869f16186d4a3adca85a6901d09fc583))

- **deps**: Update dependency pyupgrade to v3.15.2
  ([`22dc193`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/22dc1932c9d9ff4d2d72175ac22d622d13ec35f5))

- **deps**: Update dependency boto3 to v1.34.69
  ([`164dbee`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/164dbeec03c04dd3b8f94e8399bfde130a8cd159))

- **deps**: Update dependency djangorestframework to v3.15.1
  ([`d9c4876`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d9c48762af01319ffc32f3c38d786b7ccb7cc07b))

- **deps**: Update dependency ruff to v0.3.4
  ([`aae52b1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/aae52b159d82eeb1406f6ca9abec5467b4b2ef45))

- **deps**: Update dependency boto3 to v1.34.68
  ([`a294fb7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a294fb700079653bfefb62f09bd36f05a491aaf7))

- **deps**: Update dependency boto3 to v1.34.67
  ([`b6d056a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b6d056a386ed71a924e3be860ba34a360c9801f0))

- **deps**: Update dependency sentry-sdk to v1.43.0
  ([`2dd4261`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2dd4261b1cc2f8506cc87e2c24d1f5ec11e66f44))

- Switch from using attributes to a decorator for custom admin stuff
  ([`9c8a016`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9c8a016f8447d8886b067c108451318900bff154))

- Linting
  ([`0bce20a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0bce20a200bafd4e3ccf081a998758c4fd9666b3))

- Linting
  ([`7896d43`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7896d43ed2dfc279867669906d78dcff4c5a15ac))

- Linting
  ([`9bc52d4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9bc52d464ca9ddfdc72baa2a9fd51db4b9c8248e))

- Linting
  ([`63eef22`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/63eef22759f696768e2a4566569ecd2c736c6e99))

- Cleanup
  ([`846e749`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/846e7497c52699215afc08e72f4ce45f8921e911))

- Update all deps
  ([`e07556f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e07556f31e70af545aaf4552c1d0d1f4e67fca9f))

- More aws setings
  ([`5c8fad1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5c8fad1eb8a42afa3f302c79aedf01f91536c0ca))

- Consistent urls
  ([`544e0fb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/544e0fb4653de5cd8fa9580078459f866f6dcee9))

- **deps**: Update dependency boto3 to v1.34.65
  ([`be9935e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/be9935e392ad7facad7ab9d581ce6f87e21fbb0f))

- **deps**: Update dependency djangorestframework to v3.15.0
  ([`447bef0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/447bef02f6f8105faa0331c425526106a0ea69df))

- **deps**: Update dependency ruff to v0.3.3
  ([`d7ee70f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d7ee70f28cf69a7f99af952a140b87e2dc43baac))

- **deps**: Update dmvict/clean-workflow-runs action to v1.2.2
  ([`618cdee`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/618cdeef37fb39053923d354bece29c1ce3252f1))

- **deps**: Update dependency boto3 to v1.34.64
  ([`d46698e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d46698efbc82672033880bfb72996f79293dd610))

- **deps**: Update dependency coverage to v7.4.4
  ([`170a9be`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/170a9beb8bb22de36f1795cb9bf7a85b76742c7c))

- **deps**: Update dependency markdown to v3.6
  ([`e614e61`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e614e613f6e177511c82a35495da60338a8a4400))

- **deps**: Update dependency boto3 to v1.34.63
  ([`e03baa8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e03baa82bb569260bdd2c3e02ba0b6835a27efad))

- **deps**: Update dependency sentry-sdk to v1.42.0
  ([`e0de6fb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e0de6fb0570265c9b16ca0b1f8e0e37ac1ccbfaa))

- Cleanup
  ([`900648b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/900648beb2f9df1ff0da15c134b80a229330a31f))

- Switch to ruff format
  ([`2fc5869`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2fc586918a0ff113674570baa0998b558b4dd5bc))

- Type checking is done with mypy
  ([`ad6d79b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ad6d79b182669f60c4a09d06d2c05017af7a0e29))

- Package updates
  ([`1b0d66b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1b0d66bd5a72b1ead8601a5060bd2b42ca406448))

- Speedup health check
  ([`d421280`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d421280d44ab3bb54aa8f83b448ddee9830285a0))

- **deps**: Update dependency boto3 to v1.34.61
  ([`822f7f7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/822f7f75da0cfbc93f41dff0e88fe600c9e52da2))

- **deps**: Update dependency django-filter to v24
  ([`504b11d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/504b11d8d3d9651ecd19ea5ea37f6d34260ac147))

- Env example with s3 stuff
  ([`5e81a90`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5e81a90a9634d1b94d3de2d0288498ef68e5faf2))

- Maunally ran pre-commit with new black
  ([`c73b127`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c73b1277f8e25d7d840192580e0484d0c2c95410))

- **deps**: Update dependency black to v24
  ([`7673d60`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7673d60cfa9f742dcdad6ea6469568e4e43e11ec))

- Cleanup and vscode settings
  ([`4675d2f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4675d2ffe8e27e2d157df01e1ae6c7c8e1420f1b))

- **deps**: Update dependency ruff to v0.3.2
  ([`ffa60b0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ffa60b0880707c5297783a446e2ef5547d4a286b))

- **deps**: Update dependency bandit to v1.7.8
  ([`970c1fc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/970c1fc65c337251d6041ec74619c0b15d7335b8))

- **deps**: Update dependency pytest to v8.1.1
  ([`15d62ec`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/15d62ec5295116d1827164c22e4adde15d279e9b))

- **deps**: Update dependency sentry-sdk to v1.41.0
  ([`c7042ee`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c7042ee9a7bbf9e7f0e741cdf2b1b24bf050d085))

- **deps**: Update dependency ruff to ^0.3.0
  ([`13b1e26`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/13b1e26611f04bc4bd70c8d4957204966fea9407))

- **deps**: Update dependency environs to v11
  ([`9ed4acc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9ed4acc2c115d3390e6243acb75bfc54e47e18bd))

- **deps**: Update dependency django to v4.2.11
  ([`e1e04db`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e1e04db2e6b2dd0186f8adf543c5b3879edb72c0))

- **deps**: Update dependency django-celery-beat to v2.6.0
  ([`9693676`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9693676d7ebdc85a70784fb37091e8d09541d76c))

- **deps**: Update dependency pyupgrade to v3.15.1
  ([`0e8a4e6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0e8a4e6952c300e29a78cff738ab96fc74a78a73))

- **deps**: Update dependency ruff to v0.2.2
  ([`6f5a6bf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6f5a6bfda4b6bfc99d5e53d90be1e93eecff52ef))

- **deps**: Update dependency pytest to v8.0.2
  ([`d947253`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d947253b14b177f53f4d5346be16cf9eda9ff151))

- **deps**: Update dependency httpx to ^0.27.0
  ([`529c5d2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/529c5d2fc67a89451e8d4fe567905ed5ed3496cb))

- **deps**: Update dependency coverage to v7.4.3
  ([`526a1c8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/526a1c85c049e0a56935f726a1d45fecb0f56341))

- **deps**: Update dependency sentry-sdk to v1.40.5
  ([`5a6aae3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5a6aae3caddb2fbfca1688b9dfbaa91119c022bd))

- **deps**: Update dependency ruff to v0.2.1
  ([`1779225`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1779225b4ba9be35c17910fabe885407ff57c24b))

- **deps**: Update dependency pytest-django to v4.8.0
  ([`1d84e86`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1d84e863a59eb814cc629790af2e22f92a7b751a))

- **deps**: Update dependency mypy to v1.8.0
  ([`58221a5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/58221a5c6fb0d04fde701e51189cd743b76f4a5c))

- **deps**: Update dependency django to v4.2.10
  ([`05f0c04`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/05f0c048c788b136f0fb391553856c7bb8b3a63f))

- **deps**: Update dependency ruff to ^0.2.0
  ([`e63a99f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e63a99f7e991331c37640dc7f2eb538cd9c0d437))

- **deps**: Update dependency sentry-sdk to v1.40.3
  ([`447584e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/447584e2230ab9dd46f311c71fb39d73769792ba))

- **deps**: Update dependency pytest to v8
  ([`f47a323`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f47a3232d0696348b6c81bd072c8c4a50a067a84))

- **deps**: Update dependency coverage to v7.4.1
  ([`75c32fd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/75c32fda5b1e77569fb78d8ebccc1d44378db725))

- **deps**: Update dependency bandit to v1.7.7
  ([`c5f76d0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c5f76d0587c99f2e6a1930e5392df95d3a2756dd))

- Added id for newssites on admin
  ([`1a51ccd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/1a51ccd06bea4800d26ddcade37820003b031557))

- Make the queue durable
  ([`2d1ef91`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2d1ef9107b7e496188a2a01a4d33743c7cd23c63))

- Alter update_et fields
  ([`8887a76`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8887a765108b1299f104f4e84d0e671747405fc3))

- Moved the serializers to the correct app
  ([`4542868`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4542868097683098cd70f4a56d664702596c930e))

- **deps**: Update dependency drf-spectacular to v0.27.1
  ([`d67a124`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d67a124c30ccd31feadba5903f1e11623c122062))

- **deps**: Update dependency drf-spectacular to v0.27.1
  ([`7f8d25a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7f8d25ac625c321e011905bb646a7753cd305274))

- Improved logging, stolen from ll2 muahaha
  ([`42c62cf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/42c62cf86814ee0e5cf047fedec3831f5c0a6d51))

- Some cleanup
  ([`11d6db7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/11d6db7d973412d2b81f31f9f5b7ccd9670890cd))

- Moving the mq stuff to its own app
  ([`883f84c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/883f84cce66e7e94ad9d089917a90c6c1a222087))

- Cleanup
  ([`df76de8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/df76de880316c73855f3d061ffd138da2e720cdd))

- Clean-up tests
  ([`9b9630c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9b9630c4339d227cbd48309f54f23b38e58ee322))

- Cleanup
  ([`4b3b4fc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4b3b4fcdf9dd3042dd5a1752eef722f8d2f820ef))

- **deps**: Update dependency ruff to v0.1.13
  ([`54744cf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/54744cf0e10aae7b1ed63e37bed14778da7c17f1))

- **deps**: Update dependency environs to v10.3.0
  ([#3444](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3444),
  [`be73d7b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/be73d7b0677990b2f045a5f59e5baeeceb80b2ce))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency environs to v10.3.0
  ([`5e23da8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5e23da8bf298866db1dca5b9b403113a0509d362))

- **deps**: Update dependency markdown to v3.5.2
  ([#3443](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3443),
  [`4215382`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4215382752f935341ab377669cb3c3321a9183cf))

- **deps**: Update dependency environs to v10.2.0
  ([#3441](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3441),
  [`c308453`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/c308453e9c77068da1dcaccb1d62eba91991dea9))

- **deps**: Update dependency sentry-sdk to v1.39.2
  ([#3442](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3442),
  [`bb28e8b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/bb28e8b24c54461b8d56f68ef5f5bf70076be424))

- **deps**: Update dependency ruff to v0.1.11
  ([#3438](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3438),
  [`ad38a44`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ad38a446ad5651b10a20f05cb8487fc64d2dfed4))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency ruff to v0.1.10
  ([#3437](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3437),
  [`51cd8b2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/51cd8b2219c2a2f070fa62bd312b2ad45b7790f3))

- **deps**: Update dependency django to v4.2.9
  ([#3435](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3435),
  [`86bd906`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/86bd9066c13163f6390e4b55e4b15ca2e099cbc1))

- Cleanup
  ([`fef8bde`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fef8bdeb4592b2b9621544a6968ffc8d14294318))

- Added run config template for django
  ([`8581ec6`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8581ec6c00331577b2c184f801b3c566f5ffe828))

- Dev compose only starts secondary services
  ([`d39cddf`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d39cddf8f5348b31d1f94cdeb4e52eb0f2f848b1))

- **deps**: Update dependency pytest to v7.4.4
  ([#3434](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3434),
  [`d49843d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d49843df7786d40a87127639a42477a6023255a3))

- **deps**: Update dependency httpx to ^0.26.0
  ([#3430](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3430),
  [`45ff865`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/45ff86507bd23197b85abc1c024a46ad020b6f31))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency coverage to v7.4.0
  ([#3431](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3431),
  [`9396fc7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9396fc77914a9b3159bff280b701020d0179f244))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency ruff to v0.1.9
  ([#3432](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3432),
  [`adb1fd0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/adb1fd0a87cc8f698fa81a5fe6b13d13e1abae14))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency black to v23.12.1
  ([#3433](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3433),
  [`735bcf0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/735bcf06063ab8058a1db2cbdcb3bc860978527c))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency environs to v10
  ([#3429](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3429),
  [`26b4fa9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/26b4fa94c6760cba2f7ebff2138b2c1d7e7ced9b))

- Update all packages ([#3427](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3427),
  [`e5913b8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e5913b8ad2e6c66fc5a2465482a46de6419ea9bf))

- **deps**: Update dependency celery to v5.3.6
  ([#3405](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3405),
  [`0b1e6d3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0b1e6d3c85e2a026c7b3191569641000b3453e09))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency djangorestframework-stubs to v3.14.5
  ([#3420](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3420),
  [`0282148`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/02821481d6d414f8dcdc95ef65718c86477678f1))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency coverage to v7.3.3
  ([#3419](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3419),
  [`d99000e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d99000edddfa5337842f76002bbaf4d739101320))

- **deps**: Update dependency drf-spectacular to ^0.27.0
  ([#3422](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3422),
  [`28ab126`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/28ab126d3099d6e97005f257a3b8db66e72639a2))

- **deps**: Update dependency isort to v5.13.2
  ([#3423](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3423),
  [`eb7ae7a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/eb7ae7a88d470bab4314bfd6d5cc6fc595b8ee63))

- **deps**: Update actions/setup-python action to v5
  ([#3424](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3424),
  [`2bf7e1b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/2bf7e1b85b0a8b8a2d4749cb0ad254895f08c6b1))

- **deps**: Update dependency black to v23.12.0
  ([#3421](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3421),
  [`810c5d5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/810c5d5f616a15106b7d310dda6d47fab02a8262))

- **deps**: Update dependency pytest-env to v1.1.3
  ([#3408](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3408),
  [`ef05628`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ef05628a74383cf30f8ccff8cd16f8afc4cfc332))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency httpx to v0.25.2
  ([#3407](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3407),
  [`eb71e98`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/eb71e98710c62c1adc6054bc9dd152d73e900db6))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django to v4.2.8
  ([#3411](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3411),
  [`d07669c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d07669ccd94f87bbfe31b0dfd2267ebee4324c64))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency ruff to v0.1.8
  ([#3413](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3413),
  [`7fde3cc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7fde3cc9fc10774b0313ffa03d785acb3368b17d))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django-filter to v23.5
  ([#3414](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3414),
  [`59777dc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/59777dca5cf0ad6ce4dc510a708af4b48ab6fb5d))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django-stubs to v4.2.7
  ([#3415](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3415),
  [`473ee90`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/473ee90a74baa4848d25223dbeffeaa0757f7475))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django-stubs-ext to v4.2.7
  ([#3416](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3416),
  [`e09d66c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e09d66cc35140aaf730e5cb092c5fe9487b782d0))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency sentry-sdk to v1.36.0
  ([#3404](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3404),
  [`5e7ac80`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5e7ac8083a32b64b4ba574740020c1c3e8ef3610))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django-filter to v23.4
  ([#3403](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3403),
  [`a2c452b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a2c452b7017cfe0f8b6c64dd03a9f047da24aebf))

- **deps**: Update dependency ruff to v0.1.6
  ([#3402](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3402),
  [`6178896`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/617889619c471308ef5b7a5c8ec1825fee2e0612))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django-cors-headers to v4.3.1
  ([#3401](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3401),
  [`319b280`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/319b2808c3d6c12afe62ad6af200ed37f2ceed6d))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency sentry-sdk to v1.35.0
  ([#3398](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3398),
  [`d351f03`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d351f03fee18510b47864f9f90450b9af524e25a))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency mypy to v1.7.0
  ([#3396](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3396),
  [`cc33e19`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/cc33e1916e906c2c0303a07fe9b15873b1442b79))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency celery to v5.3.5
  ([#3395](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3395),
  [`df59cd2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/df59cd2a51d1912daec6ff9e54cb4775e78a4a18))

- **deps**: Update dependency ruff to v0.1.5
  ([#3393](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3393),
  [`ab7dafb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ab7dafb6776d628e2a9b1d5c2b28f66a5df9dd2d))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency pytest-django to v4.7.0
  ([#3392](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3392),
  [`82ccd3a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/82ccd3ac680e86559183a5e1c987e1d29e9dc515))

- **deps**: Update dependency black to v23.11.0
  ([#3391](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3391),
  [`e2c19b1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e2c19b19ecaba2899c6c90a1b068552e8e412c6e))

- **deps**: Update dependency ruff to v0.1.4
  ([#3390](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3390),
  [`8de9ecd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8de9ecd7fdf07e9b64e74448be13cbe344612190))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency sentry-sdk to v1.34.0
  ([#3388](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3388),
  [`6f134d7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6f134d714195f0ba3898756d07bd596ec9a8529f))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency httpx to v0.25.1
  ([#3389](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3389),
  [`78bbdb0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/78bbdb09cab93598e64cb5a35eb66e89f59386c1))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency django to v4.2.7
  ([#3386](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3386),
  [`e3a6ae9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e3a6ae988dbfccbdfd7696b6b2052bf271843096))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency markdown to v3.5.1
  ([#3384](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3384),
  [`147c8f0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/147c8f05b60de8471f051a955eb9c35974914fc3))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency sentry-sdk to v1.33.1
  ([#3383](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3383),
  [`fec0c89`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fec0c8952d79ab3038677b0b9d0f53862c220b2f))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update docker/setup-buildx-action action to v3
  ([#3381](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3381),
  [`67c6bf1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/67c6bf1a0a8dad87af7039732d6bf67f40433092))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dependency sentry-sdk to v1.33.0
  ([#3379](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3379),
  [`5dbc1fc`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/5dbc1fc835cd5cccfe06f5825ed19c87ee12c5d3))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update docker/metadata-action action to v5
  ([#3380](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3380),
  [`f5dc759`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/f5dc759f353ce6d1205fa9fb29a627118a723348))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update docker/build-push-action action to v5
  ([#3377](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3377),
  [`3c60043`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3c60043db4622d1c2fc75cc56d42cf15bb78a3b7))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update docker/login-action action to v3
  ([#3378](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3378),
  [`51e0cb3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/51e0cb37e0db7cbab4a37c76d075f2cd87160e54))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update actions/checkout action to v4
  ([#3376](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3376),
  [`27ac760`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/27ac760cbf3647796efc346d00db15057920d523))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update codacy/codacy-analysis-cli-action digest to 240c610
  ([#3372](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3372),
  [`14588cb`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/14588cb62757b2eeac3b5f4db99276adf698d3fd))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- **deps**: Update dmvict/clean-workflow-runs action to v1.2.1
  ([#3373](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3373),
  [`0cff04c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/0cff04c08ddf9df0e4750a0f0d1c60aa91c35dbf))

Co-authored-by: Renovate Bot <bot@renovateapp.com>

- Track performance ([#3370](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3370),
  [`02322b7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/02322b7d8e0ecc9ee350b593256d2a994259754e))

- Various cleanup scripts ([#3339](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3339),
  [`7557a9b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7557a9b3e912f4916cb1f682502f6ef5c9533928))

- No sonarqube
  ([`9674e90`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9674e90d1a3231b72b801235e896ff81b0eecbcd))

- Don't update readme for now
  ([`b33b79f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b33b79f75550e5e63123b303ee4f5064dbf88971))

- Don't update readme for now
  ([`7b08e52`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/7b08e52cc6add15722d93d44656fea63b266181b))

- Updates ([#3306](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3306),
  [`8f17f94`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8f17f940a6bd6fd00c2b480d3bffa97163379348))

* chore: updates

* chore: renaming some things

- Updates ([#2990](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/2990),
  [`cfd52e9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/cfd52e91af1ec54c4b4f20a04807c0d59c734be6))

- Updates ([#2389](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/2389),
  [`b4d86ac`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b4d86ac23cae44c12b010be3bdfc1839c7ef8ed2))

- Remove unused variables
  ([`fba77e5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fba77e5d33e46cf688f3268a57e70f12db52403c))

- Move to DATABASE_URL ([#1799](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/1799),
  [`a5ad10c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a5ad10c61134c7c82702310843a4e153926ef4a5))

- Package updates ([#863](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/863),
  [`a27cca0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a27cca0f25e7073ee839c3f27647394005254bf1))

* fix: set the max limit to 500. fixes #857

* chore: package updates

- Package updates ([#243](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/243),
  [`9789f01`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9789f01c693eff2b12a9646dd61c8c64e870f1ac))

- Package updates
  ([`e369f5a`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e369f5a41be5bae297e759e5149ae31be2eedb18))

### Code Style

- Cleanup
  ([`12fdee0`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/12fdee08bd8fbb056f07b95b4f1a54f977673fe5))

- Added v4 versioning
  ([`bfd643d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/bfd643db753600767d9f98ead56cdc3b62f8d94c))

- Sync celery and django timezone
  ([`e3e4147`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e3e414744feea99741a4aa94d3d9c14ab9fe0135))

### Documentation

- Fixes #210 ([#213](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/213),
  [`72c2be5`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/72c2be52196d19226481bc03a5fefa3c767d9e8a))

- Fixes #207 ([#212](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/212),
  [`d014a52`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d014a523c07191e77853a277e15a0503dd15a75a))

- Readme fixes ([#211](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/211),
  [`76ff866`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/76ff86611693cfdf357f6054f55bc7d70a6a1eba))

- **README.md**: Removed the shield as Poetry is not supported
  ([`9e7716f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9e7716f1bb8cb07c82d2470c8ea8b6222131e9a8))

Closes #160

### Features

- Add staging workflow for k8s
  ([`ba47566`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ba47566d2d5aa09be1f8b3f505c29a83cc2bb491))

- **admin,#3492**: Big overhaul of the SNAPI admin panel
  ([`ef3b1b4`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ef3b1b4072f6e21bca2356602edc0bb5d7cf1ecc))

- Extend autocomplete fields
  ([`11d415d`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/11d415dbae2dedbd23e37b17a254c502fd173c24))

- Add jet to the stack
  ([`27214a9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/27214a91fe83d50ba11e4663995202b416a3a30b))

- Scraper logic
  ([`69f742f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/69f742fe67b166e77bdb654bd140f27b52364e6b))

- Move to do s3 for statics
  ([`ff3a981`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ff3a9819639e32f4ec081ad8f4f7ea5b0a28c15a))

- Add amqp settings
  ([`34a5c3e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/34a5c3eecfd4e716657428fc4775d2a6b02a98d8))

- Added docker config
  ([`a5cb628`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a5cb628fd41eaa591b86e0703fdfe5716fa5edb3))

- Added tests for the consumer
  ([`88492e1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/88492e145d49a0828772a7f0bcbe80bbc83c12c7))

- Add more tests
  ([`ac2da63`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/ac2da63702ef2db03dad6ad23cb42dcaecbb897c))

- Tests for amqp stuff
  ([`d70bf4e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d70bf4e61517d7c58ffe7ad02e6c8fd3dcc71d1a))

- Moved to match/case
  ([`361cf1f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/361cf1f5a4d12b325c7dea695f974ab21bffabb7))

- Added logging when data is saved
  ([`3cd299b`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/3cd299bdea676742daa6f57c9321ebbd64dc63ce))

- Moved consumer stuff to its own app
  ([`6e95245`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6e9524572ef183ab15de919c94590cf74c777950))

- Made it configurable
  ([`a66e78c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a66e78c41a3cddc2b1bfc21b2ecd5202f0d6c33e))

- Main logic implemented
  ([`a0462c3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a0462c38a0cc7489f2701519e88033a4ba104aaa))

- Making sure the queues exist
  ([`a05121c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/a05121c1c04170f63bd6954d55f7a730e9d2451d))

- Hooking up django to the importer queues
  ([`dbcd70c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/dbcd70c5f4003c3e1cb8b9039b4be74cee7cdfdf))

- Add filter to check on featured status
  ([#3440](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3440),
  [`6e613d3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6e613d3949bef21748c519c025099b12c7bb044c))

- Exclude news sites ([#3426](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3426),
  [`da7b350`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/da7b3502b35319c445f05cedd5f9ca3b7141def8))

- Run bandit with pre-commit ([#3332](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/3332),
  [`52a81dd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/52a81dd34a8b9e6c9a2ff16ffa4db25f95ec67d7))

- Added ruff and pre-commit config
  ([#2391](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/2391),
  [`15f44a9`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/15f44a90ca1e13a80b5cbd810bede1e502632787))

* feat: added ruff and pre-commit config

* feat: added ruff and pre-commit config

* feat: added ruff and pre-commit config

* feat: added ruff and pre-commit config

* feat: added ruff and pre-commit config

* feat: added ruff and pre-commit config

* feat: ruff

* feat: ruff

* feat: ruff

* feat: ruff

* feat: ruff

- Added config for sonarqube ([#2721](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/2721),
  [`fa11bbd`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/fa11bbdf31e89860b76fb8b28b380d4a9f31c193))

- **auto generate**: Updated content
  ([#229](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/229),
  [`9bcde39`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/9bcde395c136e55a11263afb648160f37d7425cc))

- **auto generate**: Updated content
  ([#227](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/227),
  [`600f1b1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/600f1b1f748591eb1f17920cbb2ef32ffb52a306))

- **auto generate**: Updated content
  ([#226](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/226),
  [`e276f65`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e276f65848ac0df5c65c208a7754730b137e64fe))

- **auto generate**: Updated content
  ([#225](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/225),
  [`d4eaf25`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/d4eaf251bde03f591f945f53804b4aedde11491f))

- **auto generate**: Updated content
  ([`4f4e4f7`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4f4e4f799cbfe2e70621f500dc09dc57138fa5d8))

- **auto generate**: Updated content
  ([`6c61834`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/6c618341959f5478e18682447efd65bd52b2551d))

- Clean and lean
  ([`e3719e2`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/e3719e252708e045221c1a64949dc2296d7769eb))

- Clean and lean ([#217](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/217),
  [`15aa1b1`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/15aa1b12587538029b6748cf5fd7b37b22c83e51))

- Use a non-root user to run the app
  ([#216](https://github.com/TheSpaceDevs/spaceflightnewsapi/pull/216),
  [`b4d96df`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b4d96dfee7475bbd6c0d133b889372bd0fe3bdf8))

- Added a results backend
  ([`791fa5f`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/791fa5f1511f18adfbd00e3b2ed404766816ff69))

- Switched to drf_spectacular for openapi generation
  ([`837a977`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/837a977d2aab8fdde9ae20f3462d943d56ea31b6))

- Added CORS support
  ([`8c4505e`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/8c4505e5b64c736f67d46512aa2df796b6674667))

Closes #163

- Added filters to the Articles, Blogs and Reports endpoints
  ([`4b2f5b3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/4b2f5b3476d7b6665b0dac3ea592ae1793e28651))

Closes #154

- Added tasks to migrate blogs and reports
  ([`28da950`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/28da950b2e8a538087c6caddaa67a89c2ec22d51))

Closes #162

- **api/admin.py**: Added sorting on the published_at column
  ([`b3d7434`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/b3d7434dc2a266a4ed089219ce7b088bf9c8c502))

Closes #157

### Refactoring

- Changed url conf and added version
  ([`da9d53c`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/da9d53cd84123f748b1b759b42989f945de851bf))

- Split views and filters
  ([`20f1fa8`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/20f1fa84766706827dc4b1857aa7a22ed3398fd4))

- Clean-up
  ([`748aed3`](https://github.com/TheSpaceDevs/spaceflightnewsapi/commit/748aed38d33a416ebf5a2af8058dfccbcf76c940))
