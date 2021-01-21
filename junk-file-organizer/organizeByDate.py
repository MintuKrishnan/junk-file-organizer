import os
import shutil
import datetime


def organize_by_date(path):
    try:
        files = [
            file for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file))
        ]
        f = [f for f in files if checkFile(f) is False]
        for i in f:
            mtime = (os.stat(os.path.join(path, i)).st_mtime)
            timestamp = datetime.datetime.fromtimestamp(mtime).strftime(
                '%Y-%m-%d')
            if not os.path.exists(os.path.join(path, timestamp)):
                os.mkdir(os.path.join(path, timestamp))
            shutil.move(os.path.join(path, i), os.path.join(path, timestamp))

    except Exception:
        print("Error Occurs")
    else:
        print("")
        print("Success!! All files are organized by Date")


def checkFile(filename):
    d = os.path.basename(__file__)
    if filename == d:
        return True
    return False
