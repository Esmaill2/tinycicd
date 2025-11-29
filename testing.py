import subprocess
import time
proc = subprocess.Popen(["python3", "pipo/heloo.py"])
print("started")
#proc.terminate()
time.sleep(4)
print(proc.poll())