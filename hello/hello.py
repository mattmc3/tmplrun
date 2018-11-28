#!/usr/bin/env python

"""
Generate Hello, World!
"""

import os
from pathlib import Path
from jinja2 import Template


def get_tmpl(name):
    script = Path(os.path.abspath(__file__))
    tmpl_file = script.parent / (script.stem + ".jinja2")
    return tmpl_file.read_text()


def main():
    t = Template(get_tmpl("hello"))
    result = t.render(name="World")
    print(result)


if __name__ == '__main__':
    main()
