from cx_Freeze import setup, Executable 
  
setup(name = "Six Sigma Grapher" , #name of app
      version = "0.1" , #version num
      description = "" , #desc of app
      executables = [Executable("bothFileTest.py")]) #what to convert 

#python setup.py build