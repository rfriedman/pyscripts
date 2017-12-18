#!/usr/bin/python

import sys

if __name__ == "__main__":
    strLine = sys.stdin.readlines()
    for line in strLine:
        print line.splitlines()
        sys.stderr.write("DEBUG: got line: " + line)
        sys.stdout.write(line)