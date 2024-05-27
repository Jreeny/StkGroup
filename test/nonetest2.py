import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def upload_files(driver, pdf_files):
    for pdf_file in pdf_files:
        # 找到文件上传的 input 元素并上传文件
        file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(pdf_file)
        time.sleep(1)

    # 提交上传的文件
    driver.find_element(By.XPATH, '//input[@type="file"]').submit()
    time.sleep(5)
    # 点击上传
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()
    time.sleep(1)


# 创建一个 Chrome WebDriver 实例
driver = webdriver.Chrome()

# 打开目标网页
driver.get('http://10.75.43.191:8000/my-knowledge/space')

# 等待 3 秒钟
time.sleep(3)

# 输入用户名
username_input = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[1]/div/div/div/div/span/input')
username_input.send_keys("lizhuo8")

# 输入密码
password_input = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[2]/div/div/div/div/span/input')
password_input.send_keys("ZHY@lizhuo%8")
time.sleep(3)

# 提交表单选项
submit_button = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/div/div/span[1]/input')
submit_button.click()
time.sleep(1)

# 选择选项
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div')
submit_button.click()
time.sleep(1)

# 点击空白页
submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div')
submit_button.click()
time.sleep(1)

# 提交
submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[4]/div/div/div/div/button')
submit_button.click()
time.sleep(5)

# 打开知识管理
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]').click()
time.sleep(1)

# 打开知识管理
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/aside/div/div[2]/ul/li[2]/div/span/div/span').click()
time.sleep(1)

# 打开我的知识
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/aside/div/div[2]/ul/li[2]').click()
time.sleep(1)

# 打开我的空间
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/aside/div/div[2]/ul/li[2]/ul/li[1]/span/a').click()
time.sleep(3)

# 打开华为云工程师文件夹
driver.find_element(By.XPATH,
                    '/html/body/div/div/div[2]/div[2]/main/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/div/span[2]').click()
time.sleep(1)

# 获取文件夹中所有 PDF 文件的路径
folder_path = 'C:/Users/lizhuo8/Desktop/华为云'
pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".pdf")]

# 每次最多上传40个文件
batch_size = 40
for i in range(0, len(pdf_files), batch_size):
    # 点击上传文件
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div[2]/div[2]/main/div/div[2]/div/div/div[1]/div[1]/button/span[2]').click()
    time.sleep(1)
    # 点击上传文档
    driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[1]/span[2]').click()
    time.sleep(1)

    # 上传文件
    upload_files(driver, pdf_files[i:i + batch_size])
    time.sleep(10)
# 关闭浏览器

time.sleep(100)
driver.quit()
