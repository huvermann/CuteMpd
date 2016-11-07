rem C:\Python34_64\Lib\site-packages\PyQt4\pyuic4 CuteMpdMainWindow.ui -o CuteMpdMainWindowUI.py
call C:\Python34_64\python.exe compileGui.py
call C:\Python34_64\Lib\site-packages\PyQt4\pyrcc4 resources.qrc -o ..\resources_rc.py -py3
pause

