#!/usr/bin/env python

"""SQL INSERT

Usage:
  tmplrun.py COMMAND TEMPLATE [ options ]
  tmplrun.py COMMAND TEMPLATE (-h | --help)

Options:
  -h --help   Show help screen.
"""

import os
import sys
from pprint import pprint
from docopt import docopt

__VERSION__="1.0.0"


def main():
    args = docopt(__doc__, argv=sys.argv[1:3])
    pprint("The args passed are as follows:")
    pprint(args)


if __name__ == '__main__':
    main()
