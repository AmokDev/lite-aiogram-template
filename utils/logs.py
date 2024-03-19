import logging
from datetime import datetime
from colorama import init, Fore, Back

datenow = datetime.now().strftime("%H.%M.%S_%m-%d-%Y")

file = logging.FileHandler(f"data/logs/{datenow}.log")
console = logging.StreamHandler()

logging.basicConfig(
    handlers = (file, console),
    format = u'%(filename)s [Line:%(lineno)d] #%(levelname)-1s [%(asctime)s] %(message)s',
    datefmt='%H:%M:%S %m.%d.%Y',
    level = logging.INFO
)

class CustomFormatter(logging.Formatter):

    grey = Fore.LIGHTWHITE_EX
    yellow = Fore.YELLOW
    red = Fore.RED
    bold_red = Back.RED
    reset = Fore.RESET + Back.RESET
    format = u'%(filename)s [Line:%(lineno)d] #%(levelname)-1s [%(asctime)s] %(message)s'
    info_format = Fore.GREEN + u'%(filename)s' + grey + u' [Line:%(lineno)d] ' + Fore.CYAN + u'#%(levelname)-1s' + grey + ' [' + Fore.LIGHTRED_EX + u'%(asctime)s' + grey + u'] %(message)s'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + info_format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(
            fmt = log_fmt,
            datefmt = '%H:%M:%S %m.%d.%Y',
        )
        return formatter.format(record)

console.setFormatter(CustomFormatter())
