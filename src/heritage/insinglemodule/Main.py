

# ----------------
# Classe heritee
# ----------------               
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

# ----------------
# Classe heritante
# ----------------               
class Ion(Atome):
    """les ions sont des atomes qui ont gagne ou perdu des electrons"""
     
    def __init__(self, nat, charge):
        "le num. atomique et la charge electrique determinent l'ion"
        Atome.__init__(self, nat)
        self.ne = self.ne - charge
        self.charge = charge
    
    def affiche(self):
        "cette methode remplace celle heritee de la classe parente" 
        Atome.affiche(self)            # ... tout en l'utilisant elle-meme ! 
        print "Particule electrisee. Charge =", self.charge        
 
       
# ---------------------------
# Programme principal
# ---------------------------     

a1 = Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.affiche()
a2.affiche()
a3.affiche()
