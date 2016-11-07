import os, inspect
from os.path import basename

converter = "C:\Python34_64\Lib\site-packages\PyQt4\pyuic4"
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))


print("Path: {0}".format(path))

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.ui'):
            bname = os.path.basename(file).rsplit('.', 1)[0]
            cmd = '{0} {1} -o "{2}\{3}UI.py"'.format(converter, file, path, bname)
            os.system(cmd)
            print(cmd)
print("Ende")
