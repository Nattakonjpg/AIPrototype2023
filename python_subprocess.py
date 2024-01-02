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

