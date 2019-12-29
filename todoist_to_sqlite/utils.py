import sys

import click

FOREIGN_KEYS = [
    ("items", "parent_id", "items", "id"),
    ("items", "project_id", "projects", "id"),
    ("notes", "item_id", "items", "id"),
    ("notes", "project_id", "projects", "id"),
    ("projects", "parent_id", "projects", "id"),
    ("users", "inbox_project", "projects", "id"),
]


def error(message):
    click.secho(message, bold=True, fg="red")
    sys.exit(-1)


def add_foreign_keys(db, tables=None):
    for fk in FOREIGN_KEYS:
        if tables and fk[0] not in tables:
            continue
        db.add_foreign_keys([fk])
