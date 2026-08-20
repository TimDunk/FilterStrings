This is a command-line program that reads regular expressions and other configuration settings from a configuration file, matches target strings from an input file, and writes the results to a file. It is typically used for bulk parameterization in API testing.

Build a exe file：
pyinstaller  argsParser.py  -D --name extractToFile -i favicon.ico --clean --add-data config/reg_config.ini;config -c 

The command above would create an extractToFile.spec file; Use the command py"installer extractToFile.spec" can regenerate the exe file.

The approach to execute the exe file：
.\extractToFile.exe -s D:\PythonProjects\FilterStrings\getCategoryAndCloudMaterialListWithOutContent_test.py
