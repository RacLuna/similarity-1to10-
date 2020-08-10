# -*-coding:utf-8-*-
import os

#open result; know each book
file_obj1 = open('result.txt')
file_obj2 = open('dict.txt','r',encoding = 'utf-8')
all_book_fv = file_obj1.readlines()
del all_book_fv[0]  #删掉第一个两个数字的
all_book_info = file_obj2.readlines()

#获得字典{书序号：书其他信息}
#获得字典{书序号：特征向量}
book_num = []
book_fea_vec = []
book_info = []
mid1 = []
mid2 = []
for i in range(143620):
    book_num.append(i)
    mid1 = all_book_fv[i].split(' ')  #读书序+特征向量，格式是字符串组成的列表
    mid2 = all_book_info[i].split(' ')  #读书序+书信息，格式是字符串组成的列表
    del mid1[0]  #删去书的序号
    del mid2[0]
    for j in range(300):
        mid1[j] = float(mid1[j])        #循环读取300个维度的向量值，变成一个向量一个300维的列表，格式：浮点数
    book_fea_vec.append(mid1)     #把每一个特征向量（一个300维度的列表）放进总的向量列表中（列表包含列表）
    book_info.append(mid2)
book_pair = dict(zip(book_num, book_fea_vec))       #字典：{书序号：特征向量（列表格式）}
book_info_pair = dict(zip(book_num, book_info))

#输入书号，找到最相似（点乘最大），排序得到前十
target_book_num = int(input('请输入书序号')) #目前先做书序号，如果输入书名的话，用dict.txt转换一下即可
dot_mul = 0     #用于存储input的书和每一个另外的书的特征向量点乘值
all_dot_mul = []        #用于存储所有点乘值（按顺序，包含乘以自身的）
for k in range(143620):
    dot_mul = 0
    for t in range(300):
        dot_mul += (book_pair[target_book_num][t]) * (book_pair[k][t])
    all_dot_mul.append(dot_mul)

prep_4_rank = dict(zip(all_dot_mul, book_num))      #字典{点乘的值：书本序号}
rank_dot = sorted(prep_4_rank.keys(), reverse = True)
rank_in_book_num =[]
for dot in rank_dot:
    rank_in_book_num.append(prep_4_rank[dot])
top_10_num = rank_in_book_num[:10]

#找到前十的书名等信息
print('your input is:{}'.format(book_info_pair[target_book_num]))
for book in top_10_num:
    print(book_info_pair[book],'%.6f' % all_dot_mul[book])

'''
输出的格式：
    第一行：input的书名
    后10行：书名、作者、出版年份、出版社  最后一个值：向量点乘的值（相似度）
需要修改的地方：
    1. 可能会输出自己，如果输出自己的话要删掉。
'''