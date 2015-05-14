#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib, urllib
import requests
import json

import time
from datetime import date

def testPostRequest():
    urlParams = {"ksid":'NAXfginoyymrveysLl7bdMWSBKV1vEIJGttg',
                               "appName":"melody",
                               "appVersion":"0.1.0"
                           }
    headers = {"Content-type": "application/json"}
    
    payload = {"ncp":"1.0.0","type":"invoke.request",
                           "id":"af992f46-ed4b-41a6-90a4-507eb33c733d", "method":"napos.order.seachOrders",
                               "params":{
                                   "restaurantId":89374929,
                                   "fuzzyPhrase":""
                               }
                           }

    url = 'http://localhost:8080'
    relativeUrl = '/app-api/invoke' + '?' + urllib.urlencode(urlParams)
    result = requests.post(url + relativeUrl, headers = headers, data = json.dumps(payload))
    print ''.join(result)

def sendRequest(url, urlParams, headers, payload):
    finalUrl = url + '?' + urllib.urlencode(urlParams)
    result = requests.post(finalUrl, headers = headers, data = json.dumps(payload))
    return result

class TestCaseItem(object):
    name = ''
    testType = ''
    params = None
    result = None
    startTime = None
    endTime = None
    @classmethod
    def __init__(self, name, testType, params):
        self.name = name # name 
        self.testType = testType # type 
        self.params = params # params normally json string.

    @classmethod
    def run(self):
        self.startTime = time.ctime()
        self.work()
        self.endTime = time.ctime()

    @classmethod
    def work(self):
        self.result = None

    @classmethod
    def toString(self):
        return json.dumps({'name':self.name,
                    'type':self.testType,
                    'params':self.params,
                    'result':self.result,
                    'startTime':self.startTime,
                    'endTime':self.endTime
                })


class TestExcutor(object):
    startTime = None
    endTime = None
    testCases = None
    @classmethod
    def __init__(self, testCases):
        self.testCases = testCases

    @classmethod
    def run(self):
        self.startTime = time.ctime()
        for case in self.testCases:
            case.run()
        self.endTime = time.ctime()

        
class HttpRequestParamsFormater(object):    
    name = '',
    testType = 'post',
    url = '',
    urlParams = {},
    requestType = 'POST',
    requestParams = {},
    headers = {}
    
    @classmethod
    def __init__(self, strParams):
        data = json.loads(strParams)
        self.name = data['name']
        self.testType = data['type']
        self.url  = data['url']
        self.urlParams = data['urlParams']
        self.requestType = data['requestType']
        self.requestParams = data['requestParams']
        self.headers = data['headers']

    def toString(self):
        json = {'name':self.name,
                'type':self.testType,
                'url':self.url,
                'urlParams':self.urlParams,
                'requestType':self.requestType,
                'requestParams':self.requestParams,
                'headers':self.headers
        }
        return  json

class HttpTestCaseItem(TestCaseItem):
    headers = None
    url = None
    urlParams = None
    requestType = None
    payload = None
    @classmethod
    def __init__(self, name, testType, params):
        super(HttpTestCaseItem, self).__init__(name, testType, params)
        formater = HttpRequestParamsFormater(params)
        #  TODO: some argument may check to use
        self.name = formater.name
        self.headers = formater.headers  #http head params
        self.url = formater.url  #http url
        self.urlParams = formater.urlParams  #apend to url params, like form's get request.
        self.requestType = formater.requestType  #
        self.payload = formater.requestParams
        #self.params = {self.url, self.headers, self.urlParams, self.requestType, self.payload}

    @classmethod
    def work(self):
        result = sendRequest(self.url, self.urlParams, self.headers, self.payload)
        self.result = {'isSucess': True}

class TestCaseRecord():
    testCaseItem = None
    @classmethod
    def __init__(self, testCaseItem):
        self.testCaseItem = testCaseItem
        
    def toCsv(self):
        return
    
    def toString(self):
        return


def readTestCaseFromFile(fileName):
    with open(fileName, 'r') as f:
        content = f.readlines()
    return ''.join(content)

def test():
    content = readTestCaseFromFile('./cases/login.json')
    print content
    formater = HttpRequestParamsFormater(content)
    print formater.toString()
    result = sendRequest(formater.url, formater.urlParams, formater.headers, formater.requestParams)
    print ''.join(result)
    #httpTestItem = HttpTestCaseItem('test', 'post', content)
    

def testHttpTestCaseItem():
    content = readTestCaseFromFile('./cases/login.json')
    print content
    testcase = HttpTestCaseItem('login', 'http-post', content)
    print testcase.toString()
    testcase.run()
    print testcase.toString()
    
if __name__ == '__main__':
    #testPostRequest()
    #test()
    testHttpTestCaseItem()
