#!/usr/bin/env python
import json
import sys

def usage():
    print("syntax: <json file> [indent]")
    return 1

def main():
    if len(sys.argv) < 2:
        return 1

    jsonFile=sys.argv[1]
    try:
        f = open(jsonFile)
        data = f.read()
    except IOError:
        print "%s cannot be read" % jsonFile
        return 2

    argIndent = 2
    try:
        s = sys.argv[2]
        argIndent = int(s)
    except:
        pass

    jsd = json.loads(data)
    print("%s" % json.dumps(jsd, indent=argIndent))
    return 0

if __name__ == "__main__":
    main()
