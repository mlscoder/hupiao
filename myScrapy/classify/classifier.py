"""
文本分类
实现读取文本，实现分词，构建词袋，保存分词后的词袋。
提取 tfidf 特征，保存提取的特征
"""
import os
import jieba
import joblib
from sklearn import metrics
import classify.tools as tools
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression


# 文本分类器
class TextClassifier:
    def __init__(self, clf_model, data_dir, model_path):
        """
        分类器
        :param clf_model:   分类器算法
        :param data_dir:    特征数据存放目录
        :param model_path:  模型保存路径
        """
        self.data_dir = data_dir
        self.model_path = model_path
        self.train_data = os.path.join(data_dir, 'train_tfidf.data')
        self.test_data = os.path.join(data_dir, 'test_tfidf.data')
        self.vocabulary_data = os.path.join(data_dir, 'vocabulary.data')
        self.clf = self._load_clf_model(clf_model)

    def _load_clf_model(self, clf_model):
        '''
        加载模型，如果没有则训练模型，并且保存到相应文件中
        :param clf_model:
        :return:
        '''
        if os.path.exists(self.model_path):
            print('loading exists models...')
            return joblib.load(self.model_path)
        else:
            print('training models...')
            train_set = tools.readObject(self.train_data)
            clf = clf_model.fit(train_set.tdm, train_set.label)
            joblib.dump(clf, self.model_path)
            return clf

    def _predict(self, tdm):
        """
        :param tdm: 加载特征矩阵
        :return:
        """
        return self.clf.predict(tdm)

    def validation(self):
        """使用测试集进行模型验证"""
        print('starting validation...')
        test_set = tools.readObject(self.test_data)
        predicted = self._predict(test_set.tdm)
        actual = test_set.label
        for flabel, file_name, expct_cate in zip(actual, test_set.filenames, predicted):
            if flabel != expct_cate:
                pass
            # print(file_name, ": 实际类别:", flabel, " --> 预测类别:", expct_cate)
        print('准确率: {0:.3f}'.format(metrics.precision_score(actual, predicted, average='weighted')))
        print('召回率: {0:0.3f}'.format(metrics.recall_score(actual, predicted, average='weighted')))
        print('f1-score: {0:.3f}'.format(metrics.f1_score(actual, predicted, average='weighted')))

    def predict(self, text_string=None):
        vocabulary = tools.readObject(self.vocabulary_data)
        if text_string:
            corpus = [' '.join(jieba.cut(text_string))]
            vectorizer = TfidfVectorizer(vocabulary=vocabulary, stop_words=tools.stopWords())
            tdm = vectorizer.fit_transform(corpus)
            return self._predict(tdm)
        else:
            return None


if __name__ == '__main__':
    from sklearn.naive_bayes import MultinomialNB

    data_dir = 'news2'
    model_dir = 'models'
    # clf = MultinomialNB(alpha=0.001)
    # model_path = data_dir + '/NBclassifier.pkl'
    clf = LogisticRegression(C=1000.0)
    model_path = data_dir + '/LRclassifier.pkl'
    ##clf = RandomForestClassifier(bootstrap=True, oob_score=True, criterion='gini')
    ## model_path = data_dir + '/Radfclassifier.pkl'

    classifier = TextClassifier(clf, data_dir + "/feature_space", model_path)
    # classifier.validation()

    # 预测一个文本字符串
    text_string = '李兰迪出道比赵露思早，出圈也比赵露思早，一部校园青春剧让她成为观众心中的白月光，更让大家看到了她作为新晋小花的潜力。后来在综艺上首秀演技，徐峥形容她是“天才演员”。可她后来的发展却不尽如人意。'
    ret = classifier.predict(text_string=text_string)
    print(ret)
