# todoist-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/todoist-to-sqlite.svg)](https://pypi.org/project/todoist-to-sqlite/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/rixx/goodreads-to-sqlite/blob/master/LICENSE)

Save data from Todoist to a SQLite database.

## How to install

    $ pip install todoist-to-sqlite

## Authentication

Run this command and paste in your API token:

    $ goodreads-to-sqlite auth

This will create a file called `auth.json` in your current directory containing the required value. To save the file at
a different path or filename, use the `--auth=myauth.json` option.

## Thanks

This package is heavily inspired by [goodreads-to-sqlite](https://github.com/rixx/goodreads-to-sqlite/) by [Tobias Kunze
](https://github.com/rixx) and [github-to-sqlite](https://github.com/dogsheep/github-to-sqlite/) by [Simon
Willison](https://simonwillison.net/2019/Oct/7/dogsheep/).
