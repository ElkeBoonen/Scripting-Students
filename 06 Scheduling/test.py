import subprocess

subprocess.Popen(r"C:\WINDOWS\System32\calc.exe")
subprocess.Popen(['start', r'path --> test.txt'], shell=True)

# subprocess.Popen([r"path --> python.exe",r"path --> multi.py"])