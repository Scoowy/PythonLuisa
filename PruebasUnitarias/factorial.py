#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    num = 6
    x = factorial(num)
    print(x)


if __name__ == "__main__":
    main()
