import pandas as pd
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

job_list = []

#  爬取1~11頁，104 data analyst
for page in range(1, 11):
    url = f'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Data%20analyst&expansionType=area%2Cspec%2Ccom%2C' \
          f'job%2Cwf%2Cwktm&area=6001001000%2C6001002000%2C6001004000&order=12&asc=0&page={page}&mode=s&langFlag=0&lang' \
          f'Status=0&recommendJob=1&hotJob=1'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    job_items = soup.find('div', id='js-job-content').find_all('div',class_='b-block__left')

# 開始爬蟲
    for item in job_items:
        job = {}
        job['date'] = item.find('span',class_='b-tit__date').text.strip()
        company_pattern = re.compile("^公司名")
        job['company'] = item.find('a',title=company_pattern).text.strip()
        job['title'] = item.find('a',class_='js-job-link').text
        job['link'] = item.find('a')['href']
        job_list.append(job)

# 整理資料
df = pd.DataFrame(job_list).sort_values('date',ascending=False).reset_index(drop=True)

# 存成csv跟存入資料庫
today = datetime.now().strftime("%m%d")
filename = "find_job_" + today
df.to_csv(filename + '.csv')
conn = create_engine('mysql+mysqlconnector://root:12345678@127.0.0.1:3306/job_listings.db',echo=False)
df.to_sql(name=filename,con=conn,if_exists='append',index=False)
print(f"{filename} and job_listings table have been saved!")
