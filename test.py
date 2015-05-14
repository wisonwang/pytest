#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

import getopt, sys
import commonTest.testFrame
import commonTest.testHttp


def usage():
    print '''
NAME
    description
Usage
    python test.py test_case_file_path
'''[1:-1]

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    #commonTest.testFrame.testFrame()
    #commonTest.testHttp.testHttpTestCaseItem('./cases/login.json', 'httptest', 'post' )
    commonTest.testHttp.testHttpTestCaseItem(args[0], 'httptest', 'post' )
    #commonTest.testHttp.testHttpTestCaseItem('./cases/misc_device_unbund.json', 'httptest', 'post' )
    