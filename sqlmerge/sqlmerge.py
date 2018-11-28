#!/usr/bin/env python

"""sqlmerge.
Take a column list and generate a T-SQL MERGE statement.

Usage:
  sqlmerge.py [--table=<table>] [--pk=<pk>] <columns>...
  sqlmerge.py (-h | --help)
  sqlmerge.py --version

Options:
  -t --table=<table>  The table name
  --pk=<pk>           Primary key field indexes [default 0].
  -h --help           Show this screen.
  --version           Show version.
"""
import os
from docopt import docopt
from collections import namedtuple
from pathlib import Path
from jinja2 import Template


Column = namedtuple('Column', 'name is_pk')


def get_tmpl(name):
    script = Path(os.path.abspath(__file__))
    tmpl_file = script.parent / (script.stem + ".jinja2")
    return tmpl_file.read_text()


def main(arguments):
    t = Template(get_tmpl("sqlmerge"))
    all_columns = []

    table = arguments["--table"] or "{table_name}"

    for i, colname in enumerate(arguments["<columns>"]):
        is_pk = (i == 0)
        column = Column(colname, is_pk)
        all_columns.append(column)
    columns = [c for c in all_columns if not c.is_pk]
    join = " and ".join(["target.{0} = source.{0}".format(c.name)
                         for c in all_columns if c.is_pk])

    result = t.render(table=table, columns=columns, join=join)
    print(result)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='sqlmerge 1.0')
    main(arguments)
