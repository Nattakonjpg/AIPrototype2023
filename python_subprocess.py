import subprocess #for terminal command

if __name__ =="__main__":
    #Basic terminal command
    subprocess.run({"ls","-ltr"}) # spacebar = ,
    subprocess.run(["rm","-r","/home/nattakonpu/testfolder1"])