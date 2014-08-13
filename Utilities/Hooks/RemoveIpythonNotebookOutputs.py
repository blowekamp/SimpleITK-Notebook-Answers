#!/usr/bin/env python
## This script was from a stack-overflow recommendation hosted on a github gist
"""strip outputs from an IPython Notebook

Opens a notebook, strips its output, and writes the outputless version to the original file.

Useful mainly as a git pre-commit hook for users who don't want to track output in VCS.

This does mostly the same thing as the `Clear All Output` command in the notebook UI.
"""

import io
import sys

from IPython.nbformat import current

def strip_output(nb):
    is_changed = False
    """strip the outputs from a notebook object"""
    nb.metadata.pop('signature', None)
    for cell in nb.worksheets[0].cells:
        if 'outputs' in cell:
            if len(cell['outputs']) != 0:
                is_changed = True
                cell['outputs'] = []
        if 'prompt_number' in cell:
            if cell['prompt_number'] is not None:
                is_changed = True
                cell['prompt_number'] = None
    return nb, is_changed

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "USAGE: {0} <filename.ipynb> [optional_outfilename.ipynb]".format(sys.argv[0])
        print ""
        print "for i in *.ipynb; do ./{0} $i $i; done".format(sys.argv[0])
        sys.exit(-1)
    filename = sys.argv[1]
    with io.open(filename, 'r', encoding='utf8') as f:
        nb = current.read(f, 'json')
    nb_out, is_changed = strip_output(nb)
    if is_changed:
        if len(sys.argv) == 3:
            outfilename = sys.argv[2]
            with io.open(outfilename, 'w', encoding='utf8') as f:
                current.write(nb_out, f, 'json')
        else:
            print("\nWARNING:   IPython Notebook Outputs not stripped!, run the following to command:")
            print("="*80)
            print("{0} {1} {1}".format(sys.argv[0],sys.argv[1]))
            sys.exit(-1)
    sys.exit(0)
