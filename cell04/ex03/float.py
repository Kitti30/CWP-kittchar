#!/usr/bin/env python3

num_str = float(input("Give me a number: "))

if num_str.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")