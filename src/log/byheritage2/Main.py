from Logging import Logger

'''
Created on May 21, 2010

@author: akamanouche
'''

class MyClass(Logger):


    def __init__(self):
        self.logger.debug("in constructor")
   
    
    def doJob(self):
        self.logger.debug("Doing the job")
        
        
        
# MAIN

myclass = MyClass()
myclass.doJob()
