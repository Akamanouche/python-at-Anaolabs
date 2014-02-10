'''
Created on Jun 4, 2010

@author: sylvain
'''

line1 = "<SERVER_NAME name=\"__BUILTIN_NAME_SERVER__\">192.168.101.10</SERVER_NAME>"
line2 =line1.replace("__BUILTIN_NAME_SERVER__", "zozo")
print line2