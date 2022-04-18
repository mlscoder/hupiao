# 导入sklearn中相关算法包
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
# 导入第5步骤编写的分类器
from classify.classifier import TextClassifier
from time import *

# 多项式朴素贝叶斯分类器
from config import project_path


def Multinomial(data_dir, model_dir):
    clf = MultinomialNB(alpha=1.0, fit_prior=True)
    model_path = model_dir + '/NBclassifier.pkl'
    classifier = TextClassifier(clf, data_dir, model_path)
    return classifier


# 逻辑回归分类器
def Logistic(data_dir, model_dir):
    clf = LogisticRegression(C=1000)
    model_path = model_dir + '/LRclassifier.pkl'
    classifier = TextClassifier(clf, data_dir, model_path)
    return classifier


# 随机森林分类器
def RandomForest(data_dir, model_dir):
    clf = RandomForestClassifier()
    model_path = model_dir + '/Radfclassifier.pkl'
    classifier = TextClassifier(clf, data_dir, model_path)
    return classifier


# 支持向量机分类器
def svm(data_dir, model_dir):
    clf = SVC()
    model_path = model_dir + '/SVMclassifier.pkl'
    classifier = TextClassifier(clf, data_dir, model_path)
    return classifier


def duibi():
    model_dir = 'models'  # 模型存放目录
    data_dir = 'feature_space'  # 特征数据存放目录

    classifier1 = Multinomial(data_dir, model_dir)
    print('多项式朴素贝叶斯分类器:')
    classifier1.validation()

    classifier2 = Logistic(data_dir, model_dir)
    print('逻辑回归分类器:')
    classifier2.validation()

    classifier3 = RandomForest(data_dir, model_dir)
    print('随机森林分类器: ')
    classifier3.validation()

    classifier4 = svm(data_dir, model_dir)
    print('支持向量机分类器: ')
    classifier4.validation()


def get_classifier():
    model_dir = f'{project_path}\\myScrapy\\classify\\models'  # 模型存放目录
    data_dir = f'{project_path}\\myScrapy\\classify\\feature_space'  # 特征数据存放目录
    classifier = Logistic(data_dir, model_dir)
    return classifier


if __name__ == '__main__':
    data_dir = 'models'
    model_dir = 'feature_space'
    classifier2 = Logistic(data_dir, model_dir)
    print('逻辑回归分类器:')
    text1 = "申北路[烟花]正峰苑小区 朝南单间带独立阳台1300元 民用水电燃气平摊"
    text2 = "3号线 大柏树站0距离 朝南大主卧带飘窗 3户合租 燃气做饭 电梯房 密码锁 3200拎包入住"
    text3 = "7号线上海大学地铁站步行五分钟，锦秋花园，精装全配一室户南北通透光线好，干湿分离，押一付一"
    text4 = "标题：房东直租:9号线泗泾地铁站整租精装一室户独立卫生间，1600元押一付一月付，"
    print(classifier2.predict(text1))
    print(classifier2.predict(text2))
    print(classifier2.predict(text3))
    print(classifier2.predict(text4))
