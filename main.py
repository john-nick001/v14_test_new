import subprocess

p1 = subprocess.Popen(['python', 'script1.py'])
p2 = subprocess.Popen(['python', 'script2.py'])

p1.wait()
p2.wait()
