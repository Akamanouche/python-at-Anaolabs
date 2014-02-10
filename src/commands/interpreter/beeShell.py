'''
Created on May 31, 2010

@author: sylvain

Objet :
-------
    On utilise ici l'objet "cmd.Cmd", qu'il suffit d'etendre pour fabriquer un interpreteur de commande
    (tout comme dans le "BeeShell" de Beeware)
    
    > http://docs.python.org/library/cmd.html
    
'''
import cmd
import sys

class beeShell(cmd.Cmd):
  
    print "cmd name: ",cmd.__name__
  
    def precmd(self, line):
        print "in precmd()"
        return cmd.Cmd.precmd(self, line)
    
    def onecmd(self, s):
        print "in onecmd()"
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        print "in emptyline()"
        return cmd.Cmd.emptyline(self)

    def postcmd(self, stop, line):
        print "in postcmd()"
        return cmd.Cmd.postcmd(self, stop, line)

    # --------------------
    # callbacks de process
    # --------------------

    def do_bonjour(self, line):
        print "bonjour !"

    def do_sortir(self, line):
        return True

    def do_qqch(self, line):
        print "je fais qqch..."


    # --------------------
    # callbacks de help
    # --------------------

    def help_qqch(self):
        print "Ceci est l'aide pour la commande 'qqch'..."


#
# Main function
#
if __name__ == '__main__':

    beeShell = beeShell()

    while 1:
        try:
            beeShell.cmdloop()
            break
        except KeyboardInterrupt:
            print "\n** Interrupted by keyboard **"
