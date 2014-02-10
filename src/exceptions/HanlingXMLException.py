'''
Created on Jun 1, 2010

@author: akamanouche

'''
from lxml import etree
from StringIO import StringIO


# Handling BaseException exception when parsing good XML without StringIO
print
print "# Handling BaseException exception when parsing XML without StringIO"
print

xmlflowOK = "<response status=\"1\">" \
            "<tokenId uid=\"cWE=\" su=\"true\">e280427e1479be2715857cdb4ce8e4b0</tokenId>" \
            "</response>"


try:
    tree = etree.parse(xmlflowOK)
except etree.XMLSyntaxError, xmle:
    print "caught by XMLSyntaxError"
    print xmle
except BaseException, be :
    print "caught by BaseException"
    print be




xmlflowNOK = "<zzzzzresponse status=\"1\">" \
             "<tokenId uid=\"cWE=\" su=\"true\">e280427e1479be2715857cdb4ce8e4b0</tokenId>" \
             "</response>"


# Handling XMLSyntaxError exception when parsing bad XML with StringIO
print
print "# Handling XMLSyntaxError exception when parsing bad XML with StringIO"
print
try:
    tree = etree.parse(StringIO(xmlflowNOK))
except etree.XMLSyntaxError, xmle:
    print "caught by XMLSyntaxError"
    print xmle
except BaseException, be :
    print "caught by BaseException"
    print be


# Handling XMLSyntaxError exception when parsing bad XML without StringIO
print
print "# Handling XMLSyntaxError exception when parsing bad XML without StringIO"
print
try:
    tree = etree.parse(xmlflowNOK)
except etree.XMLSyntaxError, xmle:
    print "caught by XMLSyntaxError"
    print xmle
except BaseException, be :
    print "caught by BaseException"
    print be





# Debug sur un flux particuliers
print
print
print "# [02/06/2010] debug sur Entity load..." 
print

xmlflow2 = "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">"\
           "<html><head><title>403 Forbidden</title></head>"\
           "<body><h1>Forbidden</h1><p>You don't have permission to access /env_vars.php/on this server.</p></body></html>"


try:
    print StringIO(xmlflow2)
    tree = etree.parse(StringIO(xmlflow2))
except etree.XMLSyntaxError, xmle:
    print "caught by XMLSyntaxError"
    print xmle
except BaseException, be :
    print "caught by BaseException"
    print be
