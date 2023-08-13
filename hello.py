#!/usr/bin/python
# -*- coding: UTF-8 -*-
#pip install -r requirements.txt

import sys
import argparse
import requests

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--name', default='мир')

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    # print (namespace)

    print ("Привет, {}!".format (namespace.name) )
