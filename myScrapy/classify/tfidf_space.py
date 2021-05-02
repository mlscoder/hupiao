# -- coding: utf-8 --

import jieba
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from bunch import Bunch
from concurrent import futures
import sys
import pickle


def readfile(filepath, encoding='utf-8'):
    # 读取文本
    with open(filepath, "rt", encoding=encoding) as fp:
        content = fp.read()
    return content


def writeObject(path, obj):
    # 持久化python对象
    with open(path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def check_dir_exist(dir):
    # 检查目录是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)


def folder_handler(args):
    """遍历一个文件夹下的文本"""
    folder, encoding, seg = args
    print('遍历：', folder)
    try:
        assert os.path.isdir(folder)
    except AssertionError:
        return None
    files = os.listdir(folder)
    content = []
    filenames = []
    for name in files:
        filepath = os.path.join(folder, name)
        text = readfile(filepath, encoding)
        # 在此可直接分词
        if seg:
            text = ' '.join(jieba.cut(text))
        content.append(text)
        filenames.append(filepath)
    return filenames, content


def corpus_bunch(data_dir, encoding='utf-8', seg=True):
    """
    得到文本库，返回一个 Bunch 对象
    :param data_dir:    文本库目录，目录下以文件归类 data_dir/category/1.txt
    :param encoding:    文本库编码
    :param seg:         是否需要分词
    :return:
    返回一个Bunch对象包含以下属性：
     filenames (list) ：[19200个文件名（字符串，包含news2开头的路径）]
     label (list) ：[19200个标签（字符串，取文本文件所在的文件名）]
     contents (list) ：[19200个文本的内容（字符串）]
    """
    try:
        assert os.path.isdir(data_dir)
    except AssertionError:
        print('{} is not a folder!')
        sys.exit(0)

    corpus = Bunch(filenames=[], label=[], contents=[])
    # 获得每个文件夹的目录
    folders = [os.path.join(data_dir, d) for d in os.listdir(data_dir)]
    # 创建线程池遍历二级目录
    with futures.ThreadPoolExecutor(max_workers=len(folders)) as executor:
        folders_executor = {executor.submit(folder_handler, (folder, encoding, seg)): folder for folder in folders}
        for fol_exe in futures.as_completed(folders_executor):
            folder = folders_executor[fol_exe]
            filenames, content = fol_exe.result()
            if content:
                cat_name = folder.split('\\')[-1]
                content_num = len(content)
                print(cat_name, content_num, sep=': ')
                label = [cat_name] * content_num
                corpus.filenames.extend(filenames)
                corpus.label.extend(label)
                corpus.contents.extend(content)
    return corpus


def vector_space(corpus_dir, stop_words=None, vocabulary=None, encoding='utf-8', seg=True):
    """
    将一个语料库向量化
    """
    vectorizer = TfidfVectorizer(stop_words=stop_words, vocabulary=vocabulary)
    # 得到文本库
    corpus = corpus_bunch(corpus_dir, encoding=encoding, seg=seg)
    tfidf_bunch = Bunch(filenames=corpus.filenames, label=corpus.label, tdm=[], vocabulary={})
    # 计算TF-IDF向量
    tfidf_bunch.tdm = vectorizer.fit_transform(corpus.contents)
    # 语料库词汇表
    tfidf_bunch.vocabulary = vectorizer.vocabulary_
    return tfidf_bunch


def tfidf_space(data_dir, save_path, stopword_path=None, encoding='utf-8', seg=True):
    '''
    获取语料库特征向量并将其持久化
    :param data_dir: 数据所在文件夹
    :param save_path:持久化对象保存目录
    :param stopword_path: 加载停用词文件路径
    :param encoding: 字符编码。默认UTF-8
    :param seg: 是否分词，默认是True
    :return:
    '''
    stopWord = None
    # 加载停用词，使用baidu_stopwords.txt
    # 如果需要添加自定义停用词，可在此文件中直接补充
    if stopword_path:
        stopWord = [wd.strip() for wd in readfile(stopword_path).splitlines()]
    check_dir_exist(save_path)
    train = data_dir + '/train'
    # 向量化训练集文本
    train_tfidf = vector_space(train, stop_words=stopWord, encoding=encoding, seg=seg)
    test = data_dir + '/test'
    # 向量化测试集文本
    test_tfidf = vector_space(test, stop_words=stopWord, vocabulary=train_tfidf.vocabulary, encoding=encoding, seg=seg)
    # 持久化训练集特征向量
    writeObject(os.path.join(save_path, 'train_tfidf.data'), train_tfidf)
    # 持久化测试集特征向量
    writeObject(os.path.join(save_path, 'test_tfidf.data'), test_tfidf)
    # 持久化训练集词语库（词频）
    writeObject(os.path.join(save_path, 'vocabulary.data'), train_tfidf.vocabulary)


if __name__ == '__main__':
    # 数据集目录
    data_dir = 'text2'
    # 持久化特征向量存放目录
    feature_space = 'feature_space'
    # 构建tfidf特征向量
    tfidf_space(data_dir, 'feature_space', stopword_path='baidu_stopwords.txt', seg=True)
    print("done")
