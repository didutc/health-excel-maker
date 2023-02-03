# coding=<utf-8>
import math
import pickle
import numpy
import pandas as pd
import csv
import doubleagent


df_from_excel = pd.read_csv('filename.csv')
finalcolumns = df_from_excel.columns

finalq = pd.DataFrame(columns=finalcolumns)

content = df_from_excel.values.tolist()

for i, con in enumerate(content):
    keyword = con[17]
    while True:
        if len(keyword.encode('euc-kr')) < 190:
            break
        else:
            keyword = keyword.split(',')
            keyword = doubleagent.mix(keyword)[1:]
            keyword = ','.join(keyword)
    print(len(keyword.encode('euc-kr')))
    concopy = con[:]
    concopy[85] = keyword

    concopy[17] = keyword
    finalq.loc[len(finalq)] = concopy
finalq.to_csv("filename2.csv", mode='w', index=False, encoding='utf-8-sig')
