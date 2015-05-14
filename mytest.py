#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

import getopt, sys
import json

def usage():
    print '''
NAME
    description
Usage
    python program.py [options]
'''[1:-1]

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    file=""

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file= a
        else:
            assert False, "unhandled option"

    
    #string =  r'{"query":{"filtered": {"filter":{"and":[{"term":{"restaurant_id":"s"}},{"term":{"_type":"eleme_order"}},  {"range":{"created_at":{"from":"s"}}}]},"query":{"bool":{"should":[{"prefix":{"phone":"s"}}]}}}},  "from":0,"sort":[{"created_at":"desc"}],"size":20}'
    string =    r"{"query":{"filtered":{"filter":{"and":[{"term":{"restaurant_id":123}},{"range":{"created_at":{"from":2015-05-11 8:00"}}}]},"query":{"bool":{"should":[{"prefix":{"phone":130}}]}}}},"sort":[{"created_at":"desc"}],"size":10}"
    #print string
    #print json.loads(string)
    obj = json.loads(string)
    print json.dumps(obj, indent = 1)
   
