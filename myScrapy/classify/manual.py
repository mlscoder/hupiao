# -- coding: utf-8 --

# -- coding: utf-8 --
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import random
import shutil
from threading import Thread
from queue import Queue


# 检查目录是否存在，不存在则创建
def check_dir_exist(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


# 复制文件到新目录下
def copyfile(q):
    while not q.empty():
        full_folder, train, test, divodd = q.get()
        files = glob.glob(full_folder)
        filenum = len(files)
        testnum = int(filenum * divodd)
        # 生成3000以内的600个随机数
        testls = random.sample(list(range(filenum)), testnum)
        for i in range(filenum):
            # 如果序号是在testls中的放到测试集，否则放到训练集.
            if i in testls:
                shutil.copy(files[i], os.path.join(test, os.path.basename(files[i])))
            else:
                shutil.copy(files[i], os.path.join(train, os.path.basename(files[i])))


def data_divi(from_dir, to_dir, testProp=0.2):
    '''
    :param from_dir: 来源文件夹
    :param to_dir:  拆分后的文件夹
    :param testProp:   测试拆分比例，默认0.2
    :return:
    '''
    train_folder = os.path.join(to_dir, "train")
    test_folder = os.path.join(to_dir, "test")
    check_dir_exist(train_folder)
    check_dir_exist(test_folder)
    q = Queue()
    for basefolder in os.listdir(from_dir):
        full_folder = os.path.join(from_dir, basefolder)
        train = os.path.join(train_folder, basefolder)
        check_dir_exist(train)
        test = os.path.join(test_folder, basefolder)
        check_dir_exist(test)
        full_folder += "/*.txt"
        q.put((full_folder, train, test, testProp))
    for i in range(8):
        Thread(target=copyfile, args=(q,)).start()


if __name__ == "__main__":
    corpus_dir = 'text'
    exp_path = 'text2'
    testProp = 0.1
    data_divi(corpus_dir, exp_path, testProp)
    print("拆分完成")
