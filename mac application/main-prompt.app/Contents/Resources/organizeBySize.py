import math
import shutil
import os


def organize_by_size(path):
    try:
        files = os.listdir(path)
        file_size1 = {}
        for i in files:
            file_size1[i] = os.stat(os.path.join(path, i)).st_size
        sorted_file = sorted(file_size1.items(), key=lambda x: x[1])
        # print("file size 1:", file_size1)
        # print("")
        file_size0 = []
        size_types = []
        for i in sorted_file:
            f1 = (os.stat(os.path.join(path, i[0])).st_size)
            f2 = convert_size(f1)
            f3 = str(f2).split("_")
            if f3 == [] or f3 == ["0B"]:
                pass
            else:
                file_size0.append(f3)
        # print("file size 0:", file_size0)
        # print("")
        types = []
        sub = "."
        for i in sorted_file:
            if sub in i[0]:
                a1 = i[0][::-1].find(".")
                a2 = i[0][-a1:]
                if a2 not in types:
                    types.append(a2)
        # print("types : ", types)
        # print("")
        # # folder creation according to size
        for i in file_size0:
            if i[1] not in size_types:
                size_types.append(i[1])
        # print("size types : ", size_types)
        # print("")
        for i in size_types:
            for k in file_size0:
                if k[1] == i:
                    if not os.path.exists(os.path.join(path, k[1] + " files")):
                        os.mkdir(os.path.join(path, k[1] + " files"))

        # move files to their respective folders
        new_files = [
            file for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file))
        ]
        # print("new files= ", new_files)
        # print("")
        f = [f for f in new_files if checkFile(f) is False]

        for i in f:
            size_new = convert_size(os.stat(os.path.join(path, i)).st_size)
            size_new = size_new.split("_")

            # if size_new[1] == "MB":
            shutil.move(os.path.join(path, i),
                        os.path.join(path, size_new[1] + " files"))
    except Exception:
        print("Error Occurs")
    else:
        print("")
        print("Success!! All files are organized by size")


# # below function converts bytes to their readable size (ex: 1024b=1kb)
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s_%s" % (round(s), size_name[i])


# this function protects current script from being moved with other files
def checkFile(filename):
    d = os.path.basename(__file__)
    if filename == d:
        return True
    return False
