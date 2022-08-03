
#!pip install bs4
import requests
from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url)
    return r.text
def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return soup
def job_code(soup):
    datastring = ""
    #finds hyperlinks for job titles
    items = soup.find_all()
    items = soup.find_all("a")
    for item in items:
        datastring  = datastring + item.get_text()
    result = datastring.split("\n")
    return result
def companydata(soup):
    datastring = ""
    result = ""
    for item in soup.find_all("div"):
        datastring = datastring+item.get_text()
    result = datastring.split("\n")
    res = []
    for i in range(1, len(result)):
        if len(result[i]) >1:
            res.append(result[i])
    return(res)

url = "https://www.linkedin.com/jobs/search/?geoId=102095887&keywords=computer%20science%20intern&location=California%2C%20United%20States"

print( find_jobs(url))

  
def find_jobs(url):
    soup = html_code(url)
    jobresults = job_code(soup)
    companyresults = companydata(soup)
    temporary = 0
    for i in range(1, len(jobresults)):
        j = temporary
        for j in range(temporary, 2 + temporary):
            print("Company Name and Address: " + companyresults[j])
        temporary = j
        print("job: " +jobresults[i])
        print("----------------------")
