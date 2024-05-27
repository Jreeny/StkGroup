import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from tabulate import tabulate
import tkinter as tk
import sqlite3

# 连接到SQLite数据库
# 如果文件不存在，会自动在当前目录创建一个数据库文件
# conn = sqlite3.connect('data.db')


def getfinlist(dataType,stockCode):
    # 设置请求的URL和头部
    url = "http://www.chinastock.com.cn/website2020/margin/stockList?dataType="+dataType+"&stockCode="+stockCode+"&queryDate="
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "Referer": "http://www.chinastock.com.cn/newsite/cgs-services/stockFinance/businessAnnc.html?type=marginList",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "sensorsdata2015jssdkcross=...; aliyungf_tc=...; acw_tc=..."
    }

    # 发送GET请求
    response = requests.get(url, headers=headers)

    # 确保请求成功
    response.raise_for_status()

    # 将响应内容解析为JSON
    data = response.json()

    # 目标函数返回的数据中有一个键为'data'的列表
    df = pd.DataFrame(data['data'])
    # 将数据转换为pandas DataFrame
    # 注意：这里假设返回的JSON数据是一个字典，其中包含一个列表，列表中的每个元素都是一个记录。
    # 您可能需要根据实际返回的JSON结构调整这里的代码。

    # 设置显示最大行
    pd.set_option('display.max_rows', None)

    # 设置显示最大列
    pd.set_option('display.max_columns', None)

    # 筛选不全为NaN的列
    df_not_empty = df.dropna(axis=1, how='all')

    # # 使用tabulate格式化输出为表格
    # print(tabulate(df_not_empty, headers='keys', tablefmt='fancy_grid',colalign=("center", )))
    filtered_df = df_not_empty[df_not_empty['code'].str.startswith(('6', '0', '3'))]

    filtered_df = filtered_df[~filtered_df['name'].str.contains("国债")]

    # 存储为excel文件
    filtered_df.to_excel('OMRGrp.xlsx', index=False)


    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS people (code INTEGER PRIMARY KEY，name TEXT, margin_ratio DECIMAL(5, 2),
    # offset_margin_ratio DECIMAL(5, 2) )''')

getfinlist('3','')

# 1融资 2融券 3可冲抵