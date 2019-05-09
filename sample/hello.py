#!/usr/bin/env python

"""
Generate Hello, World!
"""

import os
import sys
from pathlib import Path
from jinja2 import Template


def get_tmpl(name):
    script = Path(os.path.abspath(__file__))
    tmpl_file = script.parent / (script.stem + ".jinja2")
    return tmpl_file.read_text()


def main():
    t = Template(get_tmpl("hello"))
    if len(sys.argv) < 2:
        name="World"
    else:
        name = ", ".join(sys.argv[1:])
    result = t.render(name=name)
    print(result)


if __name__ == '__main__':
    main()
