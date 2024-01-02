import subprocess  # for terminal command

def run_and_sum(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
    return int(result.stdout.strip())

if __name__ == "__main__":
    # Basic terminal commands
    subprocess.run(["ls", "-ltr"])  # run "ls -ltr"
    subprocess.run(["rm", "-r", "/home/nattakonpu/testfolder1"])  # remove folder testfolder1

    # First run
    print("first run num=100 XX=90")
    result_first_run = run_and_sum(["python", "testpy.py", "--num", "100", "--XX", "90"])
    print("---------------------------------")

    # Second run
    print("second run num=10 XX=90")
    result_second_run = run_and_sum(["python", "testpy.py", "--num", "10", "--XX", "-90"])
    print("---------------------------------")

    # Third run
    print("third run num=0")
    result_third_run = run_and_sum(["python", "testpy.py", "--num", "0"])
    print("---------------------------------")

    # Sum the results
    total_result = result_first_run + result_second_run + result_third_run

    # Print the total result
    print(f'Total Result: {total_result}')
