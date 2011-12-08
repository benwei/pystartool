#!/usr/bin/env python
# Ben Wei 2011.12 freeware
# simple to remove comma from the string cell in csv file

import sys

def leading_char(l):
    is_leading_string = 0
    a = ""
    for i in range(0, len(l)-1):
        c = l[i]
        if c == '"':
            if is_leading_string == 0:
                is_leading_string = 1
            else:
                is_leading_string = 0

        if c == ',' and is_leading_string == 1:
            continue
        a = a + c
    return a + '\n'

def main():
    if len(sys.argv) < 3:
        print "syntax: <file> <dstname>"
        sys.exit(1)

    filename = sys.argv[1]
    dstname = sys.argv[2]

    print "%s" % (filename)

    f = open(filename, 'r')

    dstf = open(dstname, "w")
    content = f.readline()
    while (content != "" ):
        line = leading_char(content)
        dstf.write(line.encode('utf-8'))
        # process content
        content = f.readline()

    dstf.close()
    sys.exit(0)

if __name__ == '__main__':
    main()
