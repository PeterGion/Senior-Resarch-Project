'''https://www.youtube.com/watch?v=HOS5Hix--bE&t=269s'''
from requests_html import HTMLSession
if __name__ ==  '__main()__':
    main()

def get_data(s, url):
    r = s.get(url)
    return r.html.find('div.job_seen_beacon')
def parse_html(html):
    job = {
    'title': html.find('h2 > a')[0].text
    }
    return job
def main():
    
    session= HTMLSession()
    url = 'https://uk.indeed.com/jobs?q=python%20developer&l=bristol'
    jobs = get_data(session, url)
    print("this is a test")
    print(jobs)
    for job in jobs:
        print(parse_html(job))


'''
session= HTMLSession()
url = 'https://uk.indeed.com/jobs?q=python%20developer&l=bristol'
r = session.get(url)

job = {
    'title': r.find('h2 > a')[0].text
    }
jobs = r.html.find('div.job_seen_beacon')
for job in jobs:
    print(job)  
'''