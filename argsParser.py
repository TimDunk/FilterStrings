#-*- coding:utf-8 -*-
# @Project:FilterStrings
# @File:testArgsParser
# @Author:dengxuquan
# @Datetime:2021/11/16 9:05
# @Software: PyCharm
# @Description:

import argparse
import filterToFile

parser = argparse.ArgumentParser()
parser.add_argument('-c','--config' , type=argparse.FileType('r',  encoding="UTF-8", errors="文件不存在"), help="配置文件,默认是reg_config.ini" , required=False)
parser.add_argument('-s','--sourceFile', type=argparse.FileType('r',  encoding="UTF-8", errors="文件不存在"), help="读取的文件", required=True)
parser.add_argument('-t','--targetFile', type=argparse.FileType('w', encoding='UTF-8'), help="输出的文件")
# args=parser.parse_args(['--sourceFile', 'getCategoryAndCloudMaterialListWithOutContent_test.py'])
args=parser.parse_args()
filterToFile.extractToWrite(vars(args))






