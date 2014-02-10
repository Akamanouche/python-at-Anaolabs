'''
Created on Jun 3, 2010

@author: sylvain
'''
from lxml import etree
from StringIO import StringIO
import re



xmlflow = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" \
          "<data>"\
          "<server>"\
          "<HTTP_HOST>192.168.101.10:80</HTTP_HOST>"\
          "<HTTP_ACCEPT_ENCODING>identity</HTTP_ACCEPT_ENCODING>"\
          "<SERVER_NAME value=\"zozo\">192.168.101.10</SERVER_NAME>"\
          "</server>"\
          "</data>"

#xmlflow = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
#          "<response status=\"1\">"\
#          "<tokenId uid=\"cWE=\" su=\"true\">ea7581eeb350f11303481c13a0480e9b</tokenId>"\
#          "<debug/>"\
#          "</response>"



def analyse(xpath,regexp):
    print "."
    print "in analyse() for xpath: '"+xpath+"' and regexp: '"+regexp+"'"
    results = None
    
    tree = etree.parse(StringIO(xmlflow))
    print tree
    try :
        results = tree.xpath(xpath)
    except BaseException, be:
        print be
        print "************************************************************ UNPARSABLED !"

    if results == None or len(results) == 0 :
        print "No results to analyse !"
        return
    
    for result in results:
        try :
            print "result type: ",str(result.__class__)
            match = re.match(regexp, str(result), re.MULTILINE | re.DOTALL)
            if match != None :
                print "************************************************************ MATCHED !"
            else :
                print "************************************************************ NO MATCH !!"
                
        except BaseException, be:
            print be
            print "************************************************************ NOT MATCHABLE !!"
            match = None

        print "match: ", match    

    print "."
 
# MAIN
print "in MAIN"

analyse("/data/server/SERVER_NAME", "192.168.101.10")
analyse("/data/server/SERVER_NAME/@value", "192.168.101.10")
analyse("/data/server/SERVER_NAME/@value", "zozo")
analyse("/data/server/SERVER_NAME/", "192.168.101.10")
analyse("/data/server/SERVER_NAME/text()", "192.168.101.10")

#analyse("/response/tokenId", "ea7581eeb350f11303481c13a0480e9b")

    
