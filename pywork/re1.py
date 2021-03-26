import re
from bs4 import BeautifulSoup

with open("python_高中職_台北市_新北市_104.html") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

skills = soup.findAll('p',class_="job-list-item__info b-clearfix b-content")

i=0
for skill in skills:
    i=i+1
    print("-----Begin{}----".format(i))
    skill_contents = skill.contents
    if skill_contents is not None:
        skill_contents_string = ' '.join([str(elem) for elem in skill_contents])

        skill_contents_string = re.sub("(?i)<.{0,1}em[^>]*>", "",skill_contents_string)
        #skill_contents_string = re.sub("(?i)</em[^>]*>", "",skill_contents_string)
        print('{}\n'.format(skill_contents_string))
        print("-----End{}----".format(i))
        if i >=2:
            break

