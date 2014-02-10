'''
Created on Jun 4, 2010

@author: sylvain
'''
'''
Created on Jun 4, 2010

@author: sylvain
'''
import os
import sys
from lxml import etree



baseDir = "/home/sylvain/eclipse_workspaces/galileo-3.5-alternate/ZONE-PYTHON/resources/xml/parsing"

filepath = os.path.join(baseDir,"suite.xml")
print "filepath: ",filepath 


# Parsing by direct access to XML File
        
tree = etree.parse(filepath)
r = tree.xpath('/suite')
if len(r) <= 0 or len(r[0].get("name")) == 0:
    print >> sys.stderr, "Error loading xml suite ", filepath, " : A suite name have to be set."
    raise RuntimeError("Error loading xml suite "+ filepath+" : A suite name have to be set.")


print "suite name: ",r[0].get("name")
print "suite needauth: ",r[0].get("needauth")


# Parsing by XML flow, based on XML File
