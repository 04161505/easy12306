# -*- coding: cp936 -*-
import os
import shutil


# ͳ���ж��پ�����������������
l = [0]*1000
fp = open('10000���Խ��2.txt')
for line in fp:
    (fn, classify) = line.strip().split(' ')
    l[int(classify)] += 1
print len([x for x in l if x>0])


'''
# ���������������Ʋ�ʹ�þ���������
fp = open('10000���Խ��2.txt')
i = 0
for line in fp:
    (fn, classify) = line.strip().split(' ')
    shutil.copy(os.path.join('ocr', fn), 'classify2/%s(%d).jpg' % (classify, i))
    i += 1
'''
