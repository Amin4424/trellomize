import logging

logname = 'data/logfile.log'
logging.basicConfig(
    filename=logname,
    filemode='a',  
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.DEBUG
)
announcement = logging.getLogger('My_log')

# logger = logging.getLogger('my_logger')

# logger.info("User performed an action.")
# logger.warning("User attempted an unauthorized action.")

