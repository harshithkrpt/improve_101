import os
from pathlib import Path

print(Path('usr').joinpath('bin').joinpath('spam'))
print(Path('usr') / 'bin' / 'spam')


# Home Path
print(Path.home())


print(os.getcwd())

print(Path.home().stat())


# for f in Path.home().iterdir():
#     print(f'Path: {f} - Size: {f.stat().st_size}')

import shutil

print(shutil.which('python3'))