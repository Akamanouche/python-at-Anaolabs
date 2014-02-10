'''
Created on Jun 1, 2010

@author: akamanouche

Les syntaxes :
    - except BaseException as be :
    - except BaseException, be :
    
    ... sont equivalentes

'''

from MiscObjects import DummyObject



# BaseException exception (on top of IOError)
print
print "# Handling BaseException exception"
print "# ==> ici, on montre qu'on peut catcher une IOError via son parent BaseException"
print
try:
    fichier = open("foo.txt", "r")
except BaseException as be :
    print "caught by BaseException"
    print be
    print str(be)



# IOError exception
print
print "# Handling IOError exception"
print
try:
    fichier = open("foo.txt", "r")
except IOError:
    print "Erreur lors de l'ouverture du fichier !"

try:
    fichier = open("foo.txt", "r")
except IOError as ioe :
    print ioe.filename


# ValueError exception
print
print "# Handling ValueError exception"
print
try:
    print int("abc")
except ValueError, vae:
    print vae



# AttributeError exception
print
print "# Handling AttributeError exception"
print "# ==> ex: appel a un attribut inexistant sur un objet"
print
try:
    myobject = DummyObject("myObject")
#except BaseException as be :
#    print "caught by BaseException"
#    print be
except AttributeError as ae :
    print "caught by AttributeError"
    print ae
