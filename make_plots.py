#! /usr/bin/env python

import user.axes
import user.spaces
import user.files
import py_modules.oldarrayindices


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filename', help='define input root file')

    return parser.parse_args()

if __name__ == '__main__':
    args=parse_args()
