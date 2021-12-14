这是一个用命令行程序，读取配置文件的正则表达式和其他配置，从输入文件中匹配出目标字符串，输出到一个文件，通常用于接口测试的大批量参数化。

构建成exe的命令：
pyinstaller  argsParser.py  -D --name extractToFile -i favicon.ico --clean --add-data config/reg_config.ini;config -c 

上述命令会产生一个extractToFile.spec文件，用命令 pyinstaller extractToFile.spec可再次构建出exe

构建成exe后的执行方法：
.\extractToFile.exe -s D:\PythonProjects\FilterStrings\getCategoryAndCloudMaterialListWithOutContent_test.py