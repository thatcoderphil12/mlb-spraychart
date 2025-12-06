import os
import glob
remove = glob.glob('*.png')
for files in remove:
    try:
        os.remove(files)
        print(f"Removed: {files}")
    except OSError as e:
        print(f"Error removing {files}: {e.strerror}")