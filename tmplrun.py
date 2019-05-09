#!/usr/bin/env python

"""tmplrun

Usage:
  tmplrun.py COMMAND TEMPLATE [ options ]
  tmplrun.py COMMAND TEMPLATE (-h | --help)

Options:
  -h --help           Show this screen.
"""

import os
import sys
import re
from docopt import docopt
from collections import namedtuple
from pathlib import Path
from jinja2 import Template

__VERSION__="1.0.0"

def get_tmpl(cmd, tmpl):
    script = Path(os.path.abspath(__file__))
    tmpl_file = Path.joinpath(script.parent, cmd, tmpl + ".jinja2")
    if not tmpl_file.exists():
        tmpl_file = Path.joinpath(script.parent, cmd, tmpl + f".{cmd}.jinja2")
    if not tmpl_file.exists():
        raise ValueError(f"No template found for {cmd}/{tmpl}")
    return tmpl_file.read_text()


def main():
    str_ver = f"tmplrun version {__VERSION__}"
    args = docopt(__doc__, argv=sys.argv[1:3], version=str_ver)
    template_str = get_tmpl(args["COMMAND"], args["TEMPLATE"])

    xms = re.X | re.M | re.S
    docopt_header_match = re.match("^\{\#\-?(.*?)\-?\#\}", template_str, xms)
    if docopt_header_match:
        docopt_header = docopt_header_match.groups()[0].strip()
        args = docopt(docopt_header, version=str_ver)

    t = Template(template_str, trim_blocks=True, lstrip_blocks=True)
    result = t.render(args=args)
    print(result)


if __name__ == '__main__':
    main()
