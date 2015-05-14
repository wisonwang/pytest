import frame.case
from frame.case import TestCaseItem
import requests
import urllib
import util.jsonUtils


def sendRequest(url, urlParams, headers, payload):
    finalUrl = url + '?' + urllib.urlencode(urlParams)
    result = {}
    try:
        result = requests.post(finalUrl, headers = headers, data = util.jsonUtils.jsonToString(payload))
    except:
        return result
    return result


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
        data = util.jsonUtils.stringToJson(strParams)
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
        return util.jsonUtils.jsonToString(json)
        

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
        self.result = util.jsonUtils.stringToJson(''.join(result))

        
