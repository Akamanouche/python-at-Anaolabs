'''
Created on Jun 2, 2010

@author: sylvain
'''

responseChecks = []
fileChecks = {}

print "responseChecks type: ", responseChecks.__class__
print "fileChecks type: ", fileChecks.__class__


if type(responseChecks) is list :
    print "responseChecks is list !"


if type(fileChecks) is dict :
    print "fileChecks is dict !"



#responseChecks.append("hello")
#responseChecks.append(10)
print responseChecks.__iter__()