from pathlib import Path

# current working directory
p = Path('.')

p = p / 'files' / 'text.txt'
print(p.name, p.parent, p.suffix, p.parents[1])

