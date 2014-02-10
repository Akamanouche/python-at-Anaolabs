'''
Created on Jun 3, 2010

@author: sylvain
'''
import re


def analye(value, regexp):
    print "**** in analyse() for value: '"+str(value)+"' and regexp: '"+regexp+"'"
    print "type of value is: "+str(value.__class__)
    match = re.match(regexp, str(value), re.MULTILINE | re.DOTALL)
    print "match: ",match
    if match == None :
        print "No match !"
    else : 
        print "matched."
        
    print
    
    
# MAIN
analye("1", "^1$")
analye("2", "^1$")

analye(float(2.0), "^1.0")



analye("Path transversal", "^Path")
analye("Path transversal", "^Pathztransversal")
