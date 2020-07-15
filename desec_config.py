from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import platform
import re

def main():

    root = Tk()

    opsys=platform.system()
    if opsys=='Windows':
        root.filename = filedialog.askopenfilename(initialdir="C:\\Users\ericmoo\Downloads")
    else:
        root.filename = filedialog.askopenfilename(initialdir="/home",title="Select a linux file")
    file=open(root.filename, "r")
    dfile = desec(file, opsys)

    root.destroy()
    root.mainloop()

    root2 = Tk()
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        exit()
    root2.destroy()
    root2.mainloop()
    for item in dfile:
        f.write(item)
    f.close()


def desec(file, opsys):
    """if opsys=="Windows":
        fileloc="C:\\Users\ericmoo\Downloads\desec.txt"
    else:
        fileloc="/home/campagnollo/tech/desec.txt" """
    removed=re.compile('(<removed>)')
    aaa=re.compile('^[a]{3,3} ')
    endstr=re.compile('^end')
    curconf=re.compile("^Current configuration.*")
    lined=file.readlines()
    filedesec=[]
    preview=True
    for i in lined:
        if preview==True:
            if re.search(curconf,i):
                preview=False
                continue
            else:
                continue


        if re.search(removed,i) or re.search(aaa,i):
            filedesec.append("!"+i)
        else:
            filedesec.append(i)
        if re.search(endstr,i):
            filedesec.append("\n")
            break


    return filedesec



if __name__ == '__main__':
    try: main()
    except UnboundLocalError:
        print("Program cancled")

