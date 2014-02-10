'''
Created on Jun 4, 2010

@author: sylvain
'''
import os
import sys
from lxml import etree




__BUILTIN_NAME_SERVER__ = "beebackends"

baseDir = "/home/sylvain/eclipse_workspaces/galileo-3.5-alternate/ZONE-PYTHON/resources/files"

print "*** os.curdir ?: ",os.curdir
print "*** os.getcwd() ?: ",os.getcwd()

# ---------------------------
# TEST 1 : Scanning directory
# ---------------------------
print
print "Scanning directory..."
for filepath in os.listdir(baseDir):
    print "file: ",filepath
    

# ------------------------------------------------------
# TEST 2 : Reading file, replacing string, and rewriting
# ------------------------------------------------------
print
print " Reading file, replacing string, and rewriting..."

filepath = os.path.join(baseDir,"servers.xml")
newfilepath = os.path.join(baseDir,"servers-rewrite.xml")

# on lit
buffer = open(filepath, 'rU').read()

print "buffer: ",buffer
#print "buffer type: ",buffer.__class__

# on remplace
buffer = buffer.replace("__BUILTIN_NAME_SERVER__",__BUILTIN_NAME_SERVER__)
print "new buffer: ",buffer


# on re-ecrit dans le fichier d'origine
file = open(newfilepath, 'w')
file.write(buffer)
file.close()

# On checke le resultat
tree = etree.parse(newfilepath)
r = tree.xpath('/data')
if len(r) <= 0 :
    print >> sys.stderr, "Error loading xml file ", newfilepath


