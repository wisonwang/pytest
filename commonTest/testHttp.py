import http.httpTestCaseItem
from http.httpTestCaseItem import HttpTestCaseItem

import json

def readTestCaseFromFile(fileName):
    with open(fileName, 'r') as f:
        content = f.readlines()
    return ''.join(content)

def testHttpTestCaseItem(filePath, testName, testType):
    content = readTestCaseFromFile(filePath)
    
    #print 'file content', content
    testcase = HttpTestCaseItem(testName, testType, content)
    # TODO: input valite variable
    #testcase.urlParams['ksid'] = 'L1cKJxaxrtla3YWETPRdBVB8d7IG0Bk7RIWQ'
    print testcase.toString()
    testcase.run()
    print testcase.toString()