import sys

print(sys.argv)

print(sys.version)
print(sys.version_info)

print(sys.path)
sys.stdout.write("Hello World!\n")

print(sys.platform)

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

for i in range(1000000):
    #print(i)
    if i == 100:
        sys.exit(1)

