#!/usr/bin/env python
import sys
def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    set_term_title(sys.argv[1])

    sys.exit(0)

def usage():
    print "syntax: <term title>"

def set_term_title(title):
    print "\033]0;%s\007" % title

if __name__ == '__main__':
    main()
