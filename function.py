import tensorflow.keras.backend as K
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.layers.core import Flatten, Dense
from tensorflow.python.keras.layers.convolutional import Convolution2D
from tensorflow.python.keras.layers.pooling import MaxPooling2D
from tensorflow.python.keras.layers.pooling import AveragePooling2D
from tensorflow.python.keras.layers.convolutional import ZeroPadding2D
import matplotlib.pylab as plt
import numpy as np
# import theano.tensor.nnet.abstract_conv as absconv
import csv
import h5py
import os
from math import sqrt

def read_csv(path_csv): #读取csv文件为narry形式
    csv_reader=csv.reader(open(path_csv))
    s=[]
    for row in csv_reader:
        s.append(row)
    b=np.array(s)
    return b
def multipl(a, b):
    sumofab = 0.0
    for i in range(len(a)):
        temp = a[i] * b[i]
        sumofab += temp
    return sumofab


def corrcoef(x, y):
    n = len(x)
    # 求和
    sum1 = np.sum(x)
    sum2 = np.sum(y)
    # 求乘积之和
    sumofxy = multipl(x, y)
    # 求平方和
    sumofx2 = sum([pow(i, 2) for i in x])
    sumofy2 = sum([pow(j, 2) for j in y])
    num = sumofxy - (float(sum1) * float(sum2) / n)
    # 计算皮尔逊相关系数
    den = sqrt((sumofx2 - float(sum1 ** 2) / n) * (sumofy2 - float(sum2 ** 2) / n))
    return num / den

def matrix_matrix(arr,brr):
    s= np.sum(arr*brr,axis=1)/(np.sqrt(np.sum(arr**2,axis=1))*np.sqrt(np.sum(brr**2,axis=1)))
    ave = sum(s) / len(s)
    return ave
def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    sim = num / denom
    return sim
#caculate !
def count_weights(n):

    s=(n * (1+n))/2
    return int(s)

def str_to_float(list_datas):
    float_datas=[]
    for i in range(len(list_datas)):
        temps = list(map(float, list_datas[i]))
        float_datas.append(temps)
    return float_datas

def max_min_normal_data(q):
    re = []
    i = min(q)
    a = max(q)
    for k in range(len(q)):
        x = (q[k] - i) / (a - i)
        re.append(x)
    return re

def list_split(items,n): #将一个数组每n个切分为一个数组
    return [items[i:i+n] for i in range(0,len(items),n)]

def mark_datadiv(csv_path):
    marks = []
    dnumber = []
    with open(csv_path, 'r') as csvfile:
        lines = csvfile.readlines()
        csvfile.close()
        for line in lines:
            mark = line.split('\t')[0]  # "," 或者'\t'
            datanumber = line.split('\t')[1]
            dnumber.append(int(datanumber))
            mark1 = mark[:-1][1:]
            marks.append(int(mark1))
        return marks, dnumber
        # pri据标签切分的段点数
def down_sample(s,n):#n为每隔n个点取平均，取代原数组中的数
    left = 0
    right = left + n
    # print(s[left],s[right])

    while right < len(s):
        mean = np.mean(s[left:right])
        s[left] = mean
        del s[left + 1:right]
        left += 1
        right += 1
    return s
def read_csv(path_csv): #读取csv文件为narry形式
    csv_reader=csv.reader(open(path_csv))
    s=[]
    for row in csv_reader:
        s.append(row)
    b=np.array(s)
    return b
def mark_datadiv(csv_path):
    marks = []
    dnumber = []
    with open(csv_path, 'r') as csvfile:
        lines = csvfile.readlines()
        csvfile.close()
        for line in lines:
            mark = line.split('\t')[0]  # "," 或者'\t'
            datanumber = line.split('\t')[1]
            dnumber.append(int(datanumber))
            mark1 = mark[:-1][1:]
            marks.append(int(mark1))
        return marks, dnumber
        # pri据标签切分的段点数
#根据字典的值value找到key
def get_dict_key(dic,value):
    keys=list(dic.keys())
    values=list(dic.values())
    idx=values.index(value)
    key=keys[idx]
    return key


def normalization(x):
    x=(x-np.mean(x))/np.std(x)
    return x
