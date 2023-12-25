import subprocess #for terminal command

if __name__ =="__main__":
    #Basic terminal command
    subprocess.run({"ls","-ltr"}) #run "ls -ltr" "spacebar = ,"
    subprocess.run(["rm","-r","/home/nattakonpu/testfolder1"]) #"remove folder testfolder1"
    subprocess.run(["python","test.py","--num","5","--XX","10"])
    subprocess.run(["python","test.py","--num","10","--XX","20"])
    subprocess.run(["python","test.py","--num","15"])

