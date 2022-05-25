import os
import shutil
s=input("enter the source folder")
d=input ("enter the destination folder")
s=s+'/'
d=d+'/'
listfiles=os.listdir(s)
for i in listfiles:
    shutil.copy((s+i),d)
    