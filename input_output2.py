import tempfile
import os

tempdir = tempfile.gettempdir()
tempfolder = os.path.join(tempdir,'testfolder')
readme = os.path.join(tempfolder,'readme.txt')
if not os.path.exists(tempfolder):
    os.mkdir(tempfolder)
lines = ['We have joy, We have fun,We have season in the sun but the hills that we climb were just season out of time']
# fd = open(readme, 'w')
# fd.write(lines[0] + '\n')
# fd.close()

with open(readme, 'w') as f:
    for line in lines:
        f.write(line + '\n')

f = open(readme, 'r')
f.readlines()
print(f)
f.close()
