# -*- coding: cp936 -*-
import os
import shutil
import sys

result_fn = sys.argv[1]
classify_fn = sys.argv[2]


# ͳ���ж��پ�����������������
l = [0]*1600
fp = open(result_fn)
for line in fp:
    (fn, classify) = line.strip().split(' ')
    l[int(classify)] += 1
print len([x for x in l if x>0])
fp.close()


# ���������������Ʋ�ʹ�þ���������
fp = open(result_fn)
i = 0
for line in fp:
    (fn, classify) = line.strip().split(' ')
    shutil.copy(os.path.join('ocr', fn), '%s/%s(%d).jpg' % (classify_fn, classify, i))
    i += 1
