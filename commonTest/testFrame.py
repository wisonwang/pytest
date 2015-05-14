import frame.case
from frame.case import TestCaseItem

def testFrame():
    testItem = TestCaseItem('sample', 'test', '{}')
    testItem.run()
    print testItem.toString()


