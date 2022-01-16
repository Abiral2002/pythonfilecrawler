import os

files=[]

def scraw(mainpath):
    path=mainpath
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
            scraw(os.path.join(path,i))
        else:
            files.append(os.path.join(path,i))



maindir="C:\\Users\\abila\\OneDrive\\Desktop\\Tor Browser"
for i in os.listdir(maindir):
    path=os.path.join(maindir,i)
    if os.path.isdir(path):
        scraw(path)
    else:
        files.append(i)

print(files)