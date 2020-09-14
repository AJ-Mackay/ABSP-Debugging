# Module 12 - Debugging: Logging

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

### To save the logging messages to a different file ###
### instead of displaying them in the shell, add "filename='.txt', " ###
### As the commented line below: ###
# logging.basicConfig(filename='myLogs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

### The line below will disable ALL the logging messages when uncommented. ###
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')

# There are 5 logging levels, from lowest to highest they are:
# logging.debug() - not that important.
# logging.info() - more important.
# logging.warning() - something COULD go wrong.
# logging.error() - something HAS gone wrong.
# logging.critical() - something has gone wrong and program should stop immediately.

### To disable the logging at warning level and below use: ###
# logging.disable(logging.WARNING)
### change the capitalised level as appropriate for other levels. ###
