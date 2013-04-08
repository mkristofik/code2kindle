#          Copyright Michael Kristofik 2013.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

"""
Create an e-book from source code files.

Convert all text files in a given directory to html files.  Write a table
of contents file (code.html) for Calibre to use to generate an e-book from the
html files.
"""

import cgi
import os
import sys
from __future__ import print_function

def getAllFiles(directory):
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            yield f

def getHtmlName(filename):
    return filename.replace('.', '_') + '.html'

def writeHtmlFile(directory, filename):
    html_file = getHtmlName(filename)
    src_file = os.path.join(directory, filename)
    with open(html_file, 'w') as f, open(src_file, 'r') as src:
        print('<html><body><h2>{0}</h2><pre>'.format(filename), file=f)
        lines = (cgi.escape(txt) for txt in src)
        print(*lines, sep='', file=f)
        print('</pre></body></html>', file=f)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python {0} <source-dir>'.format(sys.argv[0]))
        sys.exit(1)

    dir_path = sys.argv[1]
    with open('code.html', 'w') as toc:
        print('<html><body><h2>Table of Contents</h2><p>', file=toc)
        for f in getAllFiles(dir_path):
            writeHtmlFile(dir_path, f)
            print('<a href="{0}">{1}</a><br />'.format(getHtmlName(f), f),
                  file=toc)
            print(os.path.join(dir_path, f))
        print('</p></body></html>', file=toc)
