'''
Created on May 12, 2010

@author: akamanouche
'''

class Introspector(object):
    '''
    Cette classe permet de tester les focntionnalites d'introspection/reflection de Python
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print "\n\tin __init__() function"
        self.dummy = "This is a dummy property"

    def intro(self):
        print "\n\tin intro() function"
        
        print "\n\t# Introspections sur l'objet 'Introspector' (via 'self')"
        print "\t\t- __doc__ ?: ",self.__doc__
        print "\t\t- __class__ ?: ",self.__class__
        print "\t\t- __str__ ?: ",self.__str__()
        print "\t\t- propriete 'dummy' ?: ",self.dummy
        
        
        results = ["hello", 1]
        
        print "\n\t# Introspections sur l'objet 'results'"
        print "\t\t- methodes de l'objet: ",dir(results)
        print "\t\t- methodes de la methode \"append\": ",dir(results.append(object))
        print "\t\t- __class__ ?: ",results.__class__
        print "\t\t- __init__ sur l'objet: ",results.__init__

    
"""
Main
"""
print "# Introspections sur main()"
print "'__name__' : ",__name__

introspector = Introspector()
introspector.intro()
