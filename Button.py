import subprocess
import time

begin = time.time()

subprocess.run(["python", "Output.py"])  # Runs file.py in a new process
subprocess.run(["python", "GoogleSheets.py"])

end = time.time()
total_time_taken = end-begin
minutes = str(int(total_time_taken/60))
seconds = str(round(total_time_taken % 60,3))
total_time_taken = minutes+"m "+seconds+"s"
print(f"Total runtime of the program is {total_time_taken}")    
