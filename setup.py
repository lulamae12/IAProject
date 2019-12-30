from cx_Freeze import setup, Executable

exe = [Executable("SixSigmaGrapher.py", base = "Win32GUI",icon ="icon.ico")]


setup(name = "Six Sigma Grapher" , #name of app
      version = "0.1" , #version num
      description = "" , #desc of app
      executables = exe)#what to convert

      
#DONT FORGET BOTH 36 AND 3 DLLS FOR IT TO WORK
#python setup.py build