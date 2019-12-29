import sys

import click


def error(message):
    click.secho(message, bold=True, fg="red")
    sys.exit(-1)
