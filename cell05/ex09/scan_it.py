#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = text.count(keyword)

    if matches == 0:
        print("none")
    else:
        print(matches)