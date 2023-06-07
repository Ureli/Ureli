import os
import time

DAYZ = 5        # Maximal age of file to stay, olders well be del
FOLDERS = [
            "home/ureli/Music"
          ]
TOTAL_DELETED_SIZE = 0     # Total deleted size of all files in BYTES
TOTAL_DELETED_FILE = 0     # Total deleted files
TOTAL_DELETED_DIRS = 0     # Total deleted empty folders

nowTime = time.time()                 # Get Current time in SECONDS
ageTime = nowTime - 60*60*24*DAYZ     # Minus DAYS in SECONDS

def delete_old_files(folder):
    ### Delete files older than X DAYS ###
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)            # get Full PATH to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile             # Count SUM of all free space
                TOTAL_DELETED_FILE += 1                    # Count number of deleted files
                print("Deleting file: " + str(fileName))
                os.remove(fileName)                        # Deleted file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_time = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_time += 1
            print("Deleting EMPTY Dir: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_time > 0:
        delete_empty_dir(folder)
#================================MAIN======================
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)     # Delete old files
    delete_empty_dir(folder)     # Delete empty folders

finishtime = time.asctime()

print("-----------------------------------------------")
print("TART TIME: " + str(starttime))
print("Total Deleted Size: " + str(int(TOTAL_DELETED_SIZE/1024/1024)) + " MB")
print("Total Deleted Files: " + str(TOTAL_DELETED_FILE))
print("Total Deleted Empty folders: " + str(TOTAL_DELETED_DIRS))
print("FINISH TIME: " + str(finishtime))
print("-----------------------EOF---------------------")