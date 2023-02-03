# coding=<utf-8>
import math
import pickle
import numpy
import pandas as pd
import csv
import doubleagent
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()


colstandard = doubleagent.picklereader('cafe24_df_columns.pkl')
constandardoriginal = doubleagent.picklereader('contentstandard.pkl')
df_from_excel = pd.read_csv('카페24.csv')
finalcolumns = df_from_excel.columns
print(len(finalcolumns))
finalq = pd.DataFrame(columns=finalcolumns)
fileselct = filedialog.askopenfilename()
df = pd.read_excel(fileselct, engine='openpyxl')
content = df.values.tolist()

for con in content:
    esmswitch = False
    sumerize = con[-1]

    if pd.isna(con[2]) == True:
        break

    if 'bbs' in con[2][:3]:
        itemno = con[2][4:]
        imagefile = con[2][3:]+'.jpg'

        esmswitch = True
    if 'esm' in con[2][:3]:
        itemno = con[2][4:]
        imagefile = con[2][3:]+'.jpg'
        esmswitch = True   
    if not "esm" in con[2][:3] and not 'bbs' in con[2][:3]:
        itemno = con[2][1:]
        imagefile = con[2]+'.jpg'
    number = itemno

    if '-' in number:

        number = number.split('-')[0]

    itemname = con[4]
    if pd.isna(itemname) == True:
        break

    if pd.isna(con[5]) == True:
        break
    originalprice = round(con[6])

    if pd.isna(con[4]) == True:
        break

    finalprice = round(con[5])

    keywordlist = con[7]
    if pd.isna(keywordlist) == True:
        break

    sobijaga = finalprice + 300
    itemprice = finalprice - 3000
    

    if len(number) <5 and esmswitch == False: 

        html = '''<center>
    <img src="http://gi.esmplus.com/didutc/fast.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/accurate.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/revin2.jpg" />
    
    <br />
    <br />
    <br />
    <br />
    <br />
    </center>
    <center>
    <img src="https://media97.imghost.cafe24.com/'''+str(number)+'''.jpg" />
    <br />
    <img src="http://media97.imghost.cafe24.com/MS.jpg" />
    </center>'''
    if len(number) > 4 and esmswitch == False: 
         html = '''<center>
    <img src="http://gi.esmplus.com/didutc/fast.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/accurate.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/revin2.jpg" />
    
    <br />
    <br />
    <br />
    <br />
    <br />
    </center>
    <center>
    <img src="http://mskorea3118.cafe24.com/'''+str(number)+'''.jpg" />
    <br />
    <img src="http://media97.imghost.cafe24.com/MS.jpg" />
    </center>'''  
    if esmswitch == True: 
         html = '''<center>
    <img src="http://gi.esmplus.com/didutc/fast.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/accurate.jpg" /><br /><br />
    <img src="http://gi.esmplus.com/didutc/revin2.jpg" />
    
    <br />
    <br />
    <br />
    <br />
    <br />
    </center>
    <center>
    <img src="https://gi.esmplus.com/didutc/'''+str(number)+'''.jpg" />
    <br />
    <img src="http://media97.imghost.cafe24.com/MS.jpg" />
    </center>'''
    constandard = constandardoriginal[:]
    constandard[7] = itemname
    if 'bbs' in con[2][:3]: 
        itemno = con[2][3:]
        constandard[9] = itemno
    if 'esm' in con[2][:3]: 
        itemno = con[2][3:]
        constandard[9] = itemno
    if not "esm" in con[2][:3] and not 'bbs' in con[2][:3]:
        constandard[9] = con[2]

    if 'bbs' in con[2][:3]: 
        itemno = con[2][3:]
        constandard[11] = itemno
    if 'esm' in con[2][:3]: 
        itemno = con[2][3:]
        constandard[11] = itemno
    if not "esm" in con[2][:3] and not 'bbs' in con[2][:3]:
        constandard[11] = con[2]


    constandard[12] = sumerize
    constandard[13] = sumerize
    constandard[14] = html
    constandard[16] = html
    constandard[17] = keywordlist
    constandard[19] = sobijaga
    constandard[20] = originalprice
    constandard[21] = itemprice
    constandard[22] = finalprice
    constandard[46] = imagefile
    constandard[47] = imagefile
    constandard[85] = keywordlist
    constandard[82] = itemname

    finalq.loc[len(finalq)] = constandard


finalq.to_csv("filename.csv", mode='w', index=False, encoding='utf-8-sig')
