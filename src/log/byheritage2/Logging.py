import logging.config

class Logger:
    '''
    classdocs
    '''
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("defaultLogger") 

    def __init__(self):
        '''
        Constructor
        '''
        
        # PAS BESOIN DE CE CONSTRUCTEUR
        print "[InnerLogger] - in constructor"
