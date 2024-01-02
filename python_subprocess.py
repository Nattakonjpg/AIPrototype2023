import subprocess #for terminal command

if __name__ =="__main__":
    #Basic terminal command
    subprocess.run(["ls","-ltr"]) #run "ls -ltr" "spacebar = ,"
    subprocess.run(["rm","-r","/home/nattakonpu/testfolder1"]) #"remove folder testfolder1"
    print("first run num=100 XX=90")
    subprocess.run(["python","testpy.py","--num","100","--XX","90"])
    print("---------------------------------")
    print("second run num=10 XX=90")
    subprocess.run(["python","testpy.py","--num","10","--XX","-90"])
    print("---------------------------------")
    print("third run num=0")
    subprocess.run(["python","testpy.py","--num","0"])
    print("---------------------------------")


    #ues output from other programk
    process_output = subprocess.Popen(["python", "testpy.py", "--num", "0"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
    out, err = process_output.communicate()  # fix the typo here, change ',' to '.'
    print(out.decode("utf-8"))
    print(len(out.decode("utf-8")))
    
    #HW write subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello word)
    import subprocess

    def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return result.stdout

    if __name__ == "__main__":
    # Store the results of each command
    results = []

    # Basic terminal command
    results.append(run_command(["ls", "-ltr"]))
    results.append(run_command(["rm", "-r", "/home/nattakonpu/testfolder1"]))

    # Run and store the outputs of the Python scripts
    results.append(run_command(["python", "testpy.py", "--num", "100", "--XX", "90"]))
    results.append(run_command(["python", "testpy.py", "--num", "10", "--XX", "-90"]))
    results.append(run_command(["python", "testpy.py", "--num", "0"]))

    # Combine and print the results
    combined_output = '\n'.join(results)
    print(combined_output)

