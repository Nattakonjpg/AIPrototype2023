import subprocess #for terminal command

if __name__ =="__main__":
    #Basic terminal command
    subprocess.run({"ls","-ltr"}) #run "ls -ltr" "spacebar = ,"
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
    process_output = subprocess.Popen(["python","testpy.py","--num","0"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
    out, err = process_output,communicate()
    print(out.decode("utf-8"))
    print(len(out.decode("utf-8")))
    
    #HW write subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello word)
    # Define the subprocess commands
    commands = [
        ['python', 'testpy.py', '--num', '100', '--XX', '90'],
        ['python', 'testpy.py', '--num', '10', '--XX', '-90'],
        ['python', 'testpy.py', '--num', '0',]
    ]

    # Extract the last numbers from each command and convert to integers
    #last_numbers = [int(command[-1]) for command in commands]

    # Sum up the values and print the total result
   # total_result = sum(last_numbers)
    #print(f"The total result is: {total_result}")
    results = [run_and_capture_output(command) for command in commands]

    # Sum up the values and print the total result
    total_result = sum(results)
    print(f"The total result is: {total_result}")

