# todoist-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/todoist-to-sqlite.svg)](https://pypi.org/project/todoist-to-sqlite/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/bcongdon/todoist-to-sqlite/blob/master/LICENSE)

Save data from Todoist to a SQLite database. Supports saving tasks, projects, filters, notes, labels, and completed tasks.

(Some Todoist features require Premium, like fetching completed tasks)

## How to install

    $ pip install todoist-to-sqlite

## Authentication

In the Todoist client, go to the [Integrations tab](https://todoist.com/prefs/integrations) of Settings and issue/copy your personal API token. Run this command and paste in your API token:

    $ todoist-to-sqlite auth

This will create a file called `auth.json` in your current directory containing the required value. To save the file at
a different path or filename, use the `--auth=myauth.json` option.

## Saving Current Todoist Data

The `sync` command retrieves all "active" data associated with your Todoist account.

    $ todoist-to-sqlite sync todoist.db

This includes: uncompleted tasks, projects, labels, filters, and notes.

## Saving Completed Tasks

The `completed-tasks` command saves all completed tasks from your Todoist account. This may take a long time to download for active Todoist users.

    $ todoist-to-sqlite completed-tasks todoist.db

`completed-tasks` also will sync any associated metadata (i.e. archived projects) associated with completed tasks.

Note: This command requires Todoist Premium due to limitations of their API.

### `from_date` and `to_date`

You can specify `--from_date` and `--to_date` to place boundaries on the time range that `todoist-to-sqlite` will fetch completed tasks from.

```
    $ todoist-to-sqlite completed-tasks todoist.db \
        --to_date   2020-12-01 \
        --from_date 2020-12-30
```

## Attribution

This package is heavily inspired by [goodreads-to-sqlite](https://github.com/rixx/goodreads-to-sqlite/) by [Tobias Kunze
](https://github.com/rixx) and [github-to-sqlite](https://github.com/dogsheep/github-to-sqlite/) by [Simon
Willison](https://simonwillison.net/2019/Oct/7/dogsheep/).

This package was designed to fit nicely in the [dogsheep](https://dogsheep.github.io/) / [datasette](https://github.com/simonw/datasette) ecosystems.
