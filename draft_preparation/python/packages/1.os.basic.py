import os
import time
print(os.getcwd())


entries = os.listdir(".")
print(entries)

with os.scandir('.') as it:
    for entry in it:
        print("File Name | Is File | Is Directory ")
        print(entry.name, entry.is_file(), entry.is_dir())


os.makedirs('a/b/c', exist_ok=True)
# time.sleep(5)
os.rmdir('a/b/c')            # only removes empty dir
os.removedirs('a/b')

with open('file.txt', 'w') as f:
    f.write('Hello World')
st = os.stat('file.txt')
print(st)
time.sleep(5)
os.remove('file.txt')

pid = os.getpid()
ppid = os.getppid()   # parent pid

print(pid, ppid)