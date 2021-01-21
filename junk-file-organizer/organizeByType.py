import os
from pathlib import Path
import shutil
from directory import DIRECTORIES

FILE_FORMATS = {
    file_format: directory
    for directory, file_formats in DIRECTORIES.items()
    for file_format in file_formats
}


def organize_by_type(path):
    try:
        for file in os.scandir(path):
            if file.is_dir():
                continue
            file_path = Path(file)

            file_format = file_path.suffix.lower()
            if file_format in FILE_FORMATS:
                directory_name = Path(FILE_FORMATS[file_format])
                if not os.path.exists(os.path.join(path, directory_name)):
                    os.mkdir(os.path.join(path, directory_name))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, directory_name))
    except Exception:
        print(Exception)
    else:
        print("")
        print("Success!! All files are organized by File Type")
