# from bs4 import BeautifulSoup

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     # tags = soup.find('h5')
#     # tags = soup.find_all('h5')
#     # # print(tags)
#     # for tag in tags:
#     #     print(tag.text)
#     course_card = soup.find_all('div', class_='card')
#     values = {}
#     for course in course_card:
#         values[course.h5.text] = course.a.text.split()[-1]
#     for i in values:
#         print(i, values[i])

from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')

jlist = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for i, job in enumerate(jlist):
    last_date = job.find('span', class_='sim-posted').find('span').text
    if 'few' in last_date:
        companies = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
# for i in comapnies:
        with open(f'{i}.txt', 'w') as f:
            f.write(f"{companies.strip()}\n")
            f.write(f"{skills.split(',')}\n")
            f.write(f"{last_date.strip()}\n")
            print(f"{more_info}\n")
            if i == 1:
                break
            # print()
# print(jobs_list.text)
