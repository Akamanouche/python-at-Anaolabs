'''
Created on May 21, 2010

@author: <a href="mailto:tech@bee-ware.net">BeeWare Development Team</a>
'''
import logging
import sys

# -------------------
# Defining the Logger
# -------------------

# create logger
logger = logging.getLogger("defaultLogger")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(filename)s] - %(lineno)04d - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

  

# ----
# Main
# ----
logger.debug("hello !")
