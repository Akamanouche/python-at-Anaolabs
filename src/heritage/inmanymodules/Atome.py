'''
Created on May 21, 2010

@author: sylvain
'''
class Atome:
    """atomes simplifies, choisis parmi les 10 premiers elements du TP""" 
    table =[None, ('hydrogene',0), ('helium',2), ('lithium',4),
            ('beryllium',5), ('bore',6), ('carbone',6), ('azote',7),
            ('oxygene',8), ('fluor',10), ('neon',10)]

    def __init__(self, nat):
        "le num. atomique determine le n. de protons, d'electrons et de neutrons" 
        self.np, self.ne = nat, nat       # nat = numero atomique
        self.nn = Atome.table[nat][1]     # nb. de neutrons trouves dans table
        
    def affiche(self):
        print
        print "Nom de l'element :", Atome.table[self.np][0]
        print "%s protons, %s electrons, %s neutrons" % \
                  (self.np, self.ne, self.nn)
