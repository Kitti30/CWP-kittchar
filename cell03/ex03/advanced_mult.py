#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        line = f"Table de {i}:"
        while j <= 10:
            line += f" {i * j}"
            j += 1
        print(line)
        i += 1