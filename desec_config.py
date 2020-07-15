from tkinter import *
from tkinter import filedialog
import platform
import re

def main():

    root = Tk()
    opsys=platform.system()
    if opsys=='Windows':
        root.filename = filedialog.askopenfilename(initialdir="C:\\")
    else:
        root.filename = filedialog.askopenfilename(initialdir="/home",title="Select a linux file")
    file=open(root.filename, "r")
    desec(file, opsys)


    filename=root.filename
    root.destroy()
    root.mainloop()


def desec(file, opsys):
    if opsys=="Windows":
        fileloc="C:\\user\ericmoo\desec.txt"
    else:
        fileloc="/home/campagnollo/tech/desec.txt"
    removed=re.compile('(<removed>)')
    aaa=re.compile('^[a]{3,3} ')
    endstr=re.compile('^end')
    curconf=re.compile("^Current configuration.*")
    lined=file.readlines()
    filedesec=open(fileloc,"w")
    preview=True
    for i in lined:
        if preview==True:
            if re.search(curconf,i):
                preview=False
                continue
            else:
                continue


        if re.search(removed,i) or re.search(aaa,i):
            filedesec.write("!"+i)
        else:
            filedesec.write(i)
        if re.search(endstr,i):
            filedesec.write("\n")
            break
    filedesec.close()
    #file.close()
    return



if __name__ == '__main__':
    try: main()
    except UnboundLocalError:
        print("Program cancled")

