import logging
from datetime import datetime

datenow = datetime.now().strftime("%H.%M.%S_%m-%d-%Y")

file = logging.FileHandler(f"data/logs/{datenow}.log")
console = logging.StreamHandler()

logging.basicConfig(
    handlers=(file, console),
    format = u'%(filename)s [Line:%(lineno)d] #%(levelname)-1s [%(asctime)s] %(message)s',
    datefmt='%H:%M:%S %m.%d.%Y',
    level = logging.INFO
)