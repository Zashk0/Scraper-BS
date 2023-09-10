import time
import requests
from bs4 import BeautifulSoup

def find_jobs():
    html_text = requests.get("https://dev.bg/company/jobs/back-end-development/").text
    soup  = BeautifulSoup(html_text, 'lxml')
    jobs = soup.findAll('div', class_ = 'inner-right listing-content-wrap')

    for job in jobs:
        name= job.find('h6').text.replace(' ','')
        date = job.find('span' ,class_='date date-with-icon').text.replace(' ','')
        more_info = job.a['href']
        print(f"Company Name: {name.strip()}")

        print(f"Listing Date: {date.strip()}")
        print(f"Additional Information: {more_info}")
        print("------")
if __name__ =="__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait *60)
        