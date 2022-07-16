#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import openpyxl
import numpy as np
from openpyxl.styles import Font
from openpyxl import load_workbook


# In[2]:


dir #= "C:/Users/Administrator/Desktop/导入订单/5.23/AM-FBA订单-4月"
path_file = str(input('请输入文件所在文件夹目录：'))
need_dir = os.chdir(path_file)


# In[3]:


need_file_name = os.listdir(need_dir)
need_file_name


# In[4]:


#表头
title = str(input('请输入表头文件名，带后缀：'))
bt = pd.read_excel(title)
#更换表头
for file_name in need_file_name:
    if file_name[-3:] =="xls" or file_name[-3:] == "lsx":
        data = pd.read_excel(os.path.join(path_file,file_name),names = list(bt))
        data.to_excel(file_name,index = False)
    else:
        data = pd.read_csv(os.path.join(path_file,file_name),skiprows = 1,names = list(bt),engine = 'python')  #skiprows = 1表示从第二行算起
        data.to_csv(file_name,index = False)


#





# In[ ]:




