'''
Created on May 20, 2010

@author: akamanouche
'''

from operators.binaire import settings

def isRunConf(run):
    return (run & settings.RUN_CONF == 1)

def isRunTest(run):
    return (run & settings.RUN_TEST == 2)

def isRunClean(run):
    return (run & settings.RUN_CLEAN == 4)


# MAIN
s1=settings.RUN_CONF
s2=settings.RUN_CONF|settings.RUN_TEST
s3=settings.RUN_CONF|settings.RUN_CLEAN
s4=settings.RUN_TEST|settings.RUN_CLEAN
s5=settings.RUN_TEST|settings.RUN_CONF|settings.RUN_CLEAN

s6=settings.RUN_ALL

print "s1: "+str(s1)
print "s2: "+str(s2)
print "s3: "+str(s3)
print "s4: "+str(s4)
print "s5: "+str(s5)

print
print


print isRunConf(s1)
print isRunConf(s2)
print isRunConf(s3)
print isRunConf(s4)
print isRunConf(s5)

print
print

print isRunTest(s1)
print isRunTest(s2)
print isRunTest(s3)
print isRunTest(s4)
print isRunTest(s5)


print
print

print isRunConf(s6)
print isRunTest(s6)
print isRunClean(s6)
