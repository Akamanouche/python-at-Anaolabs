'''
ici, on teste en Python le decalage de bits a gauche ou a droite

@author: sylvain
'''

print "1 << 0 (pas de decalage): "+ str(1<<0)
print "1 << 1 (decalage a gauche de 1 bit): "+ str(1<<1)
print "1 << 2 (decalage a gauche de 2 bits): "+ str(1<<2)

print
print

print "2 << 1 (decalage a gauche de 1 bit): "+ str(2<<1)
print "2 << 2 (decalage a gauche de 2 bits): "+ str(2<<2)

print
print

print "8 >> 1 (decalage a droite de 1 bit): "+ str(8>>1)
print "8 >> 2 (decalage a droite de 2 bits): "+ str(8>>2)
