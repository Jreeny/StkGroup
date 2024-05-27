import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from tabulate import tabulate
import tkinter as tk
import sqlite3


def getfinlist():
    # 设置请求的URL和头部 datatype=1:融资 3:冲抵
    url1 = "http://www.chinastock.com.cn/website2020/margin/stockList?dataType=1&stockCode=&queryDate="
    url2 = "http://www.chinastock.com.cn/website2020/margin/stockList?dataType=3&stockCode=&queryDate="
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "Referer": "http://www.chinastock.com.cn/newsite/cgs-services/stockFinance/businessAnnc.html?type=marginList",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "sensorsdata2015jssdkcross=...; aliyungf_tc=...; acw_tc=..."
    }

    # 发送GET请求1
    response = requests.get(url1, headers=headers)

    # 确保请求成功1
    response.raise_for_status()

    # 将响应内容解析为JSON
    data = response.json()

    # 目标函数返回的数据中有一个键为'data'的列表
    df1 = pd.DataFrame(data['data'])

    # 发送GET请求2
    response = requests.get(url2, headers=headers)

    # 确保请求成功2
    response.raise_for_status()

    # 将响应内容解析为JSON
    data = response.json()

    # 目标函数返回的数据中有一个键为'data'的列表
    df2 = pd.DataFrame(data['data'])

    # 筛选不全为NaN的列，重复列
    df1.dropna(axis=1, how='all', inplace=True)
    df2.dropna(axis=1, how='all', inplace=True)

    # 重命名rate列以便于区分
    df1.rename(columns={'rate': '融资比例'}, inplace=True)
    df2.rename(columns={'rate': '冲抵比例'}, inplace=True)

    # 合并DataFrame
    merged_df = pd.merge(df1, df2, on=['code', 'name', 'date', 'stkGroup'], how='outer')

    filtered_df = merged_df[merged_df['code'].str.startswith(('6', '0', '3'))]

    filtered_df = filtered_df[~filtered_df['name'].str.contains("国债")]

    # 保存到Excel
    excel_path = 'merged_data.xlsx'
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        merged_df.to_excel(writer, index=False, sheet_name='Sheet1')

    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS people (code INTEGER PRIMARY KEY，name TEXT, margin_ratio DECIMAL(5, 2),
    # offset_margin_ratio DECIMAL(5, 2) )''')


getfinlist()

# 1融资3可冲抵
