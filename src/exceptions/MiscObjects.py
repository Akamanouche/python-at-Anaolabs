'''
Created on Jun 1, 2010

@author: akamanouche
'''

class DummyObject(object):
    '''
    classdocs
    '''


    def __init__(self,name):
        '''
        Constructor
        '''
        print "in DummyObject constructor..."
        self.name = name
        
        self.doSomething()
        
        
    def doSomething(self):
        print "in DummyObject - doSomething()"
        
#        Ici, en JAVA, ca ne compilerait pas car le champ 'logger' n'est pas defini
#        Python etant un "langage interprete", pqs de souci pour lui !...
        self.logger.debug("this line should raise an AttributeError")
        
        