import os
import shutil
import time
import random

sourceDir = "C:/Users/ayush/Downloads"
destinationDir = "C:/DocsFromDownloads"
docsExts = ['.ppt', '.xlsx', '.csv', '.pdf', '.txt', '.docx']
docsList = os.listdir(sourceDir)
# print(docsList)

for i in docsList:
    name, ext = os.path.splitext(i)
    if ext == " ":
        continue
    for j in docsExts:
        if (ext == j):
            path1 = sourceDir + "/" + i
            path2 = destinationDir
            path3 = destinationDir + "/" + i
            if(os.path.exists(path2)):
                shutil.copy(path1, path3)
            else:
                os.makedirs(path2)
                shutil.copy(path1, path3)