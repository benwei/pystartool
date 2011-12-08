#!/usr/bin/env python
# Ben Wei 2011.12 freeware
# simple tool to convert file encoding

import sys

if len(sys.argv) < 2:
    print "syntax: <file> [converted file] [file charset]"
    sys.exit(1)
filename = sys.argv[1]

dstname = 'convert.txt'
if len(sys.argv) >= 3:
    dstname = sys.argv[2]

mcharset='HKSCS'
if len(sys.argv) >= 4:
    mcharset=sys.argv[3]

print "%s(%s) - %s" % (filename, mcharset, dstname)

f = open(filename, 'r')
data = f.read()

trandata = unicode(data, mcharset)
str_utf8 = trandata.encode("utf-8")

f = open(dstname, "w")
f.write(str_utf8)
f.close()
