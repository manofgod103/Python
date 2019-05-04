"""
1、获取页面源代码
2、提取有用的数据

"""

import requests
import re
import csv

# dict_message={}
url="https://search.51job.com/list/080200,000000,0000,00,9,99,python,2,1.html"

response = requests.get(url)
response.encoding="GBK"
ret = response.text
# print(ret)

# 职位的正则表达式，获取所有的职位<a target="_blank" title="Python爬虫工程师" href="https://jobs.51job.com/hangzhou-gsq/113048420.html?s=01&t=0" onmousedown="">
#和职位名<span class="t1">职位名</span>
reg_position = '<a target="_blank" title="(.*)" href="https://jobs.51job.com.*" onmousedown="">'
position = re.findall(reg_position,ret)
# print(position)

#获取公司名称 <span class="t2"><a target="_blank" title="杭州羽联信息科技有限公司" href="https://jobs.51job.com/all/co4709160.html">和公司名<span class="t2">公司名</span>
reg_company = ' <span class="t2"><a target="_blank" title="(.*)" href="https://jobs.51job.com/all.*">'
company = re.findall(reg_company,ret)
# print(company)

#获取工作地点 <span class="t3">杭州-拱墅区</span>
reg_place = '<span class="t3">(.*)</span>'
place = re.findall(reg_place,ret)
place.remove("工作地点")
# print(place)

#获取薪资 <span class="t4">1-1.5万/月</span>
reg_wage = '<span class="t4">(.*)</span>'
wage = re.findall(reg_wage,ret)
wage.remove("薪资")
# print(wage)

#获取发布时间<span class="t5">05-02</span>
reg_date = '<span class="t5">(.*)</span>'
date = re.findall(reg_date,ret)
date.remove("发布时间")
# print(date)

# for i in range(len(company)):
#     dict_message[company[i]]=[position[i],place[i],wage[i],date[i]]
# print(dict_message)

# 保存数据到表格中
path = "D:\Python study\WorkSpace\Python\hahaha\爬虫\demo.csv"
with open(path,"w") as f:
    write_mes = csv.writer(f,dialect=("excel"))
    write_mes.writerow(["公司名称","职位","地区","薪资","发布日期"])
    for j in range(len(company)):
        write_mes.writerow([company[j],position[j],place[j],wage[j],date[j]])