import subprocess  # for terminal command

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == "__main__":
    # Basic terminal commands
    subprocess.run(["ls", "-ltr"])
    subprocess.run(["rm", "-r", "/home/nattakonpu/testfolder1"])

    print("first run num=100 XX=90")
    subprocess.run(["python", "testpy.py", "--num", "100", "--XX", "90"])
    print("---------------------------------")

    print("second run num=10 XX=90")
    subprocess.run(["python", "testpy.py", "--num", "10", "--XX", "-90"])
    print("---------------------------------")

    print("third run num=0")
    subprocess.run(["python", "testpy.py", "--num", "0"])
    print("---------------------------------")

    # Use output from another program
    process_output = subprocess.Popen(["python", "testpy.py", "--num", "0"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode("utf-8"))
    print(len(out.decode("utf-8")))

    # HW: Write subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello word)
    # Store the results of each command
    results = []

    # Run and store the outputs of the Python scripts
    results.append(run_command(["python", "testpy.py", "--num", "100", "--XX", "90"]))
    results.append(run_command(["python", "testpy.py", "--num", "10", "--XX", "-90"]))
    results.append(run_command(["python", "testpy.py", "--num", "0"]))

    # Combine and print the results
    combined_output = '\n'.join(results)
    print(combined_output)
