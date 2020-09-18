import sys
if len(sys.argv) != 2:
    print('Expected format: python strip.py [file]')
    sys.exit(1)

lines = []
with open(sys.argv[1]) as old:
    lines = old.readlines()

with open(sys.argv[1], 'w') as new:
    new.writelines(lines[0:6]+['\t\t\t<link rel="stylesheet" href="../style.css">\n']+lines[260:-1])
