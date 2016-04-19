__author__ = 'например Андрей'
from Dbmaker import start_stat_collecting
import datetime
print(__name__)
if __name__ == '__main__':
    i = 1
    while i is not None:
        if ((datetime.now().hour == 22) & (datetime.now().minute == 00) & (datetime.now().second == 00)) | (i == 1):
            dirList = []
        i = start_stat_collecting()