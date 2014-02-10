'''
Created on Feb 6, 2014
@author: akamanouche
    -------------------------------------------------------------------------------------------------------
    Quelques tests basiques...
    -------------------------------------------------------------------------------------------------------
'''


def getSomething(parm):
    print "\nin getSomething()"
    if not parm :
        print "\t param is empty (None)"

    result = parm
    return result


def doNothing(self):
    pass

if __name__ == '__main__':
    print __doc__
    
    #doNothing(None)
    
    print "==> result = %(result)s" % {'result' : getSomething("hello") }
    print "==> result = %(result)s" % {'result' : getSomething(None) }