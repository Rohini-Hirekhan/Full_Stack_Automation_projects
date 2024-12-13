import logging
logging.basicConfig(filename='mylog.txt',level=logging.DEBUG)
print("log")
logging.info("hi")
logging.basicConfig(filename='mylog2.txt',format='%(levelname)s',datefmt=='%d/%m/%Y %I:%M:%S %p'))