import shutil

shutil.copy('files/test.txt', 'files/test-copy.txt')
shutil.copy2('files/test.txt', 'files/test-copy-2.txt')

#shutil.copytree('.', './files')
#shutil.copytree('.', 'dst_folder', ignore=shutil.ignore_patterns('*.tmp', '*.log'))

usage = shutil.disk_usage('/')
print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Used: {usage.used / (1024**3):.2f} GB")
print(f"Free: {usage.free / (1024**3):.2f} GB")
