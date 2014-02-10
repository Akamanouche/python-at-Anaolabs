import logging.config

'''
Created on May 21, 2010

@author: sylvain
'''

class InnerLogger:
    '''
    classdocs
    '''
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("defaultLogger") 

    def __init__(self):
        '''
        Constructor
        '''
        
        # PAS BESOIN DE CE CONSTRUCTEUR
        print "[InnerLogger] - in constructor"
        
        
class MyClass(InnerLogger):


    def __init__(self):
        self.logger.debug("in constructor")
   
    
    def doJob(self):
        self.logger.debug("Doing the job")
        
        
        
# MAIN

myclass = MyClass()
myclass.doJob()
