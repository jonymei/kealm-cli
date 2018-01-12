# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import argparse
import base64
import urllib.parse
import random

def base64_encode(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decode', action='store_true', help='base64 decode')
    parser.add_argument('input', help='the str to be encode/decode')
    if not args:
        args = sys.argv[1:]
    result = parser.parse_args(args)
    if result.decode:
        __base64_decode(result.input)
    else:
        __base64_encode(result.input)


def url_encode(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decode', action='store_true', help='url decode')
    parser.add_argument('input', help='the str to be encode/decode')
    if not args:
        args = sys.argv[1:]
    result = parser.parse_args(args)
    if result.decode:
        __url_decode(result.input)
    else:
        __url_encode(result.input)

def roll(min=1, max=100):
    try:
        max = int(sys.argv[2])
    except IndexError as e:
        try:
            max = int(sys.argv[1])
        except:
            pass
    else:
        min = int(sys.argv[1])
    num = random.randint(min, max)
    print(num)


def __base64_encode(s):
    print(base64.standard_b64encode(s.encode()).decode())

def __base64_decode(s):
    print(base64.standard_b64decode(s.encode()).decode())

def __url_encode(s):
    print(urllib.parse.quote(s))

def __url_decode(s):
    print(urllib.parse.unquote(s))


def main():
    base64_encode(['hello'])
    url_encode(['https://www.baidu.com'])
    roll()
    roll(10)
    roll(12, 13)

if __name__ == '__main__':
    main()