#-*- coding:utf-8 -*-
# @Project:FilterStrings
# @File:FilterToFile
# @Author:dengxuquan
# @Datetime:2021/11/8 18:27
# @Software: PyCharm
# @Description:
import re,os
from datetime import datetime
from os import path
from pathlib import Path
import configparser

def getConfig(configFile,pathLike:bool):
    config = configparser.ConfigParser()
    if pathLike:
        config.read(configFile, encoding="UTF-8")
    else:
        config.read_file(configFile, source=None)
    return config

def getDelimeter(config):
    delimeter = config["Output"]["Delimeter"]
    if type(delimeter)==str:
        delimeter=delimeter.replace("\\t",'\t')
    return delimeter

def getSourceFile(files_dict:dict):
    sourceFile = files_dict.get("sourceFile")
    if not path.exists(sourceFile.name):
        print(path.abspath(sourceFile.name) + "不存在")
        exit(0)
    return sourceFile

def getDefaultConfigFilePath(dir,configFileName):
    for dirpath, dirnames, filenames in os.walk(dir):
        if ".idea" in dirnames:
            dirnames.remove(".idea")
        if "Testenv_venv" in dirnames:
            dirnames.remove("Testenv_venv")
        if "__pycache__" in dirnames:
            dirnames.remove("__pycache__")
        if "markDownPic" in dirnames:
            dirnames.remove("markDownPic")

        if configFileName in filenames:
            configFilePath=os.path.join(os.path.abspath(dirpath), configFileName)
            print("使用默认配置文件    ",configFilePath)
            return configFilePath

        for d in dirnames:
            r=getDefaultConfigFilePath(d,configFileName)
            if r:
                return r

def extractToWrite(files_dict:dict):
    sourceFile=getSourceFile(files_dict)

    configFile=files_dict.get("config")
    if not configFile:
        configFileName="reg_config.ini"
        defalutConfigFile=getDefaultConfigFilePath(os.path.abspath(os.path.dirname(__file__)),configFileName)
        if not defalutConfigFile:
            print("找不到配置文件",configFileName)
            exit(0)
        config=getConfig(defalutConfigFile,pathLike=True)
    else:
        config=getConfig(configFile,pathLike=False)
    reg = re.compile(config["RegExp"]["Expression"])
    delimeter=getDelimeter(config)
    outputFileSuffix=config["Output"]["FileSuffix"]

    if not files_dict.get("targetFile"):
        targetFileName=datetime.now().strftime("%Y%m%d%H%M%S")+"-"+Path(sourceFile.name).stem+outputFileSuffix
        targetFile=open(targetFileName,"w",encoding="UTF-8")
    else:
        targetFile= files_dict.get("targetFile")

    lineContent=sourceFile.readlines()
    for line in lineContent:
        match = reg.search(line)
        if match:
            output_line=''
            for index in range(1,len(match.groups())+1):
                output_line+=match.group(index)+delimeter
            count=len(output_line)-len(delimeter)
            output_line=output_line[:count]   #每一行最后不需要分割字符，所以去掉最后的分割字符
            targetFile.write( output_line+"\n")
    targetFile.flush();

    print("提取的内容已写入到    ",os.path.abspath(targetFile.name))
    if not targetFile.closed:
        targetFile.close();
    if not sourceFile.closed:
        sourceFile.close();
