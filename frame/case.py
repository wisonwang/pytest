import time
import json

class TestCaseItem(object):
    name = ''
    testType = ''
    params = None
    result = None
    startTime = None
    endTime = None
    beforeHooks = []
    afterHooks = []
    @classmethod
    def __init__(self, name, testType, params):
        self.name = name # name 
        self.testType = testType # type 
        self.params = params # params normally json string.

    @classmethod
    def run(self):
        self.startTime = time.ctime()
        for f in self.beforeHooks:
            f(self.params)
        self.work()
        for f in self.afterHooks:
            f(self.result)
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
                }, indent = 4)

    @classmethod
    def addBeforeHook(self, function):
        
        return

    @classmethod
    def addAfterHook(self, function):
        
        return
