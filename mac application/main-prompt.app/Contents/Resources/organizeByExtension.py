import errno
import os


def organize_by_extension(path):
    try:
        all_files = os.listdir(path)
        all_ext = []
        # split all file extensions from the dir
        for f in all_files:
            _, ext = os.path.splitext(f)
            if ext == "":
                continue
            if ext[1:] not in all_ext:
                all_ext.append(ext[1:])
        try:
            for ext in all_ext:
                if ext:
                    os.mkdir(os.path.join(path, ext))
        except OSError as e:
            if e.errno == errno.EEXIST:
                pass

        # #move all files to their respective dirs
        for f in all_files:
            _, ext = os.path.splitext(f)
            old_path = os.path.join(path, f)
            new_path = os.path.join(path, ext[1:], f)
            os.rename(old_path, new_path)
    except Exception:
        print("Error Occurs")
    else:
        print("")
        print("Success!! All files are organized by Extension")
