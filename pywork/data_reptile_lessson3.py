import re
from bs4 import BeautifulSoup
#r = requests.get('https://www.1111.com.tw/search/job?ks=python&c0=100100%2C100200&gr=2&fs=1&page=1')
#r = requests.get('https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&edu=2&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc')
#soup = BeautifulSoup(r.text, 'html.parser')
#someString.replaceAll("(?i)<td[^>]*>", "");
list = []
with open("python_高中職_台北市_新北市_104.html") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
#print(soup)
jobs = soup.findAll('article')
for job in jobs:
    if  job.get('data-cust-name') is not None:
        list.append(job.get('data-cust-name'))
        list.append(job.get('data-job-name'))
skills = soup.findAll('p',class_="job-list-item__info b-clearfix b-content")
insert_index = -1
for skill in skills:
    skill_contents = skill.contents
    if skill_contents is not None:
        skill_contents_string = ' '.join([str(elem) for elem in skill_contents])
        skill_contents_string = re.sub("(?i)<.{0,1}em[^>]*>", "",skill_contents_string)
        insert_index = insert_index + 3
        list.insert(insert_index, skill_contents_string)
print(list)

