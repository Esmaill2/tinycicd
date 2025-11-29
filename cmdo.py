import subprocess 
import time
proc = subprocess.Popen(["python3", "pipo/heloo.py"])
print("started")


while True:
 time.sleep(3)
 with open("pipo/heloo.py", "r") as f:
     
     rep =f.readlines()


 with open("pipo/rheloo.py", "r") as f:
     
      run =f.readlines()


 if rep == run:
     
     continue
 
 else:
    test_proc = subprocess.Popen(["python3", "pipo/rheloo.py"])
    time.sleep(5)

    if test_proc.poll() is None:

        test_proc.terminate()

        with open("pipo/heloo.py", "w") as f:
            f.writelines(run)

        proc.terminate()
        proc.wait()  

        proc = subprocess.Popen(["python3", "pipo/heloo.py"])
        
    else:
       test_proc.terminate()
       print("update has some error")
       with open("pipo/rheloo.py", "w") as f:
        f.writelines(rep)