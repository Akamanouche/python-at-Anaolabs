'''
Created on May 21, 2010

@author: sylvain
'''
from heritage.inmanymodules import Atome


# ----------------
# Classe heritante
# ----------------               
class Ion(Atome.Atome):
    """les ions sont des atomes qui ont gagne ou perdu des electrons"""
     
    def __init__(self, nat, charge):
        "le num. atomique et la charge electrique determinent l'ion"
        Atome.Atome.__init__(self,nat)
        self.ne = self.ne - charge
        self.charge = charge
    
    def affiche(self):
        "cette methode remplace celle heritee de la classe parente" 
        Atome.Atome.affiche(self)            # ... tout en l'utilisant elle-meme ! 
        print "Particule electrisee. Charge =", self.charge        
 
       
# ---------------------------
# Programme principal
# ---------------------------     

a1 = Atome.Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.affiche()
a2.affiche()
a3.affiche()
