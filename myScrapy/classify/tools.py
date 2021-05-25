# -- coding: utf-8 --
"""
工具函数
"""
import os
import pickle


def readfile(filepath, encoding='utf-8'):
    # 读取文本
    with open(filepath, "rt", encoding=encoding) as fp:
        content = fp.read()
    return content


def savefile(savepath, content, encoding='utf-8'):
    # 保存文本
    with open(savepath, "wt", encoding=encoding) as fp:
        fp.write(content)


def writeObject(path, obj):
    # 持久化python对象
    with open(path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def readObject(path):
    # 载入python对象
    with open(path, "rb") as file_obj:
        obj = pickle.load(file_obj)
    return obj


def check_dir_exist(dir):
    # 检查目录是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)

def stopWords(stopword_path="../../myScrapy/classify/baidu_stopwords.txt"):
    # 返回停用词列表，默认使用百度停用词表
    stopWords = [wd.strip() for wd in readfile(stopword_path).splitlines()]
    return stopWords
