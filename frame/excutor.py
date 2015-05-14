import time
import frame.case as case
from case import TestCaseItem 

class LogicJump(object):
    cases = {}
    @classmethod
    def __init__(self):

    @classmethod
    def addCase(self, case):
        if case.name not in self.cases.keys:
            self.cases[case.name] = case
    
    @classmethod
    def addJudge(self, caseName, functionDoc):
        

class CaseJdugeLogic(object):
    @classmethod
    def __init__(self, testCase, jumpfailed, jumpsucced):
        

class TestExcutor(object):
    startTime = None
    endTime = None
    testCases = None
    beforeRunCaseHooks = []
    afterRunCaseHooks = []
    context = {}
    @classmethod
    def __init__(self, testCases):
        self.testCases = testCases

    @classmethod
    def run(self):
        self.startTime = time.ctime()
        for case in self.testCases:
            for f in self.beforeRunCaseHooks:
                f(case.params)
            case.run()
            for f in self.afterRunCaseHooks:
                f(case.result)
        self.endTime = time.ctime()

    @classmethod
    def addBeforeRunCaseHook(self, function):
        self.afterRunCaseHooks.append(function)
        return

    @classmethod
    def addAfterRunCaseHook(self, function):
        self.afterRunCaseHooks.append(function)
        return


