# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 22:34:08 2022

@author: 신지원
"""

score = []
for i in range(5):
    num = int(input())
    if num >= 40:
        score.append(num)
    else:
        score.append(40)
print(int(sum(score)/5))