--- [06/02/2014] ------------------------------------------------------------------------------------------------------

	***************************************************************************
	!! ATTENTION aux noms de package !!
		==> ils ne doivent pas interferer avec un nom de module existant
	***************************************************************************
		
	ex:
		Au debut, j'ai appele ce package "collections"
		Quand je lancais le script ./exceptions/HanlingXMLException.py, j'avais l'erreur :

		[...]
		Traceback (most recent call last):
		  File "/home/sylvain/eclipse_workspaces/galileo-3.5-alternate/ZONE-PYTHON/src/exceptions/HanlingXMLException.py", line 7, in <module>
		    from lxml import etree
		  File "parsertarget.pxi", line 4, in init lxml.etree (src/lxml/lxml.etree.c:141775)
		  File "/usr/lib/python2.6/inspect.py", line 42, in <module>
		    from collections import namedtuple
		ImportError: cannot import name namedtuple
		[...]
		
		==> il y avait collision entre le module "collections.py" de Python (/usr/lib/python2.6/collections.py) et 
			mon package "collections" perso.
			
		Workaround :
			Je l'ai renomme avec une majuscule ('C')
		
-----------------------------------------------------------------------------------------------------------------------