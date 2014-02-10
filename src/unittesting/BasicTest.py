'''
Created on Feb 6, 2014
@author: akamanouche

http://docs.python.org/2/library/sys.html
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def inactiveTest(self):
        self.fail("Forced failure in inactiveTest()")


    def testForceFailure(self):
        self.fail("Forced failure in testForceFailure()")


    def testAnotherFailure(self):
        self.fail("Forced failure in testAnotherFailure()")


#------- 
# MAIN
#-------
if __name__ == "__main__":
    
    
    #import sys;
    #sys.argv = ['Test.testForceFailure']
    
    unittest.main()