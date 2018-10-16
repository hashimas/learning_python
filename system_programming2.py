import tempfile
import os
content = dir(tempfile)
tempdir = tempfile.gettempdir()
mytempdir = os.path.join(tempdir,"testdir")
print(mytempdir)
if not os.path.exists(mytempdir):
    os.mkdir(mytempdir)
    
