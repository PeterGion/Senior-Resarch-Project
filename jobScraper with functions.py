#cd C:\Users\Peter\"OneDrive - Eastern Connecticut State University"\"senior resarch"\Scraper
#git push -u origin master
#git commit -a -m ""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
import matplotlib.pyplot as plot
import csv
from random import randint
from tabulate import tabulate

'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile'
#last page url 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=480&pp=gQLQAAABhIeCedIAAAAB7hgVOgC7AQQBJ2oGDgc-BgQGOajjWXbVPKtoxz6gCwrUiOulV1DE8uIWhUoN96a_OuBT8U_7MVbePCJ-LGFcdnO782Xn_FHn_kyCyXzXzUApJebFu3ZPLcBJ7fR3OAKkzXXF7yin61pkBkXh0NtyPYQkbIV6AQywYLj9_Svtj_2y5YhVU1Ak0d7D0YfDB32euOSKGPhbdg1WLeCKNO8mN10bZM35cPeLX_vBSufZLhQmk3ygIaMFnrjAdYemIt0iIAAA&vjk=58cab7537268f79a'
intialLink = 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile'

codingLanguages = None
langaugeCount = None
jobCount = 0

def main():
    #path to my driver
    driver = webdriver.Chrome(executable_path='C:\\Users\\Peter\\OneDrive - Eastern Connecticut State University\\senior resarch\\Scraper\\chromedriver.exe')
    globals()['codingLanguages'] = [
        'Python',
        'Javascript',
        'Java',
        'C/C++',
        'C#',
        'SQL',
        'PHP',
        'Matlab',
        'Swift',
        'Kotlin',
        'Assembly',
    ]
    #initializing langaugeCount so that the length is known
    globals()['langaugeCount'] = [0,0,0,0,0,0,0,0,0,0,0]
    #globals()['langaugeCount'] = [0,3,0,4,5,6,7,3,4,0,0]
    driver.get(intialLink)
    #checking if the last page element is there
    lastPageElement = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
    #jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
    #goThoughSetPages(driver, jobPannels, lastPageElement, 1)
    goThoughPages(driver, lastPageElement)
    #print(globals()['langaugeCount'])
    #run this to make sure it works
    create_plot()


def generateSeconds():
    return randint(30,360)


#updates the csv file with the most recent languageCount information
def updateCsv():
    with open('laguageCount.csv', 'w') as rowElement:
        writer = csv.writer(rowElement)
        writer.writerow(globals()['codingLanguages'])
        writer.writerow(globals()['langaugeCount'])
        writer.writerow(['number of job listings', globals()['jobCount']])


def goThoughSetPages(driver, jobPannels, lastPageElement, amount):
    iteration = 0
    #while there is a last page element and it is not higher than the iteration amount
    while(len(lastPageElement) != 0 and iteration < amount):
        time.sleep(3)
        #all other logic will go here
        #the way that indeed is set up is that they have all of the jobs in clickable divs
        #jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
        #going though all of the job listings on the page
        allJobListings(driver,jobPannels)
        ActionChains(driver).move_to_element(lastPageElement[0]).perform()
        time.sleep(1)
        #clicks on the next page element when the page is finished
        lastPageElement[0].click()
        #checks to see if  the next page eleement is there so when it goes to the loop condtional it can decided if it should continue
        lastPageElement = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
        iteration += 1


def goThoughPages(driver, element):
    #while there is a last page element and it is not higher than the iteration amount
    while(len(element) != 0):
        time.sleep(generateSeconds())
        #all other logic will go here
        jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
        allJobListings(driver,jobPannels)
        ActionChains(driver).move_to_element(element[0]).perform()
        time.sleep(generateSeconds())
        element[0].click()
        element = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
        

def allJobListings(driver,jobPannels):
    for job in jobPannels:
        if(len(job.find_elements(By.CSS_SELECTOR,"#mosaic-afterFifthJobResult")) == 0 and 
        len(job.find_elements(By.CSS_SELECTOR,"#mosaic-afterTenthJobResult")) == 0 and
        len(job.find_elements(By.CSS_SELECTOR,"#mosaic-afterFifteenthJobResult")) == 0):
            time.sleep(generateSeconds())
            ActionChains(driver).move_to_element(job).perform()
            time.sleep(generateSeconds())
            #print(job.text)
            job.click()
            time.sleep(generateSeconds())
            jobDescription = findJobDescription(driver)
            find_Languages(jobDescription)
            globals()['jobCount'] += 1
            updateCsv()


def findJobDescription(driver):
    #class jcs-JobTitle
    #jobDescription = seleniumDriver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    jobDescription = driver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    time.sleep(generateSeconds())
    ActionChains(driver).move_to_element(jobDescription).perform()
    return jobDescription


def find_Languages(element):
    elementText = element.text
    if(elementText.find('Python')!= -1 or elementText.find('python')!= -1) == True:
        globals()['langaugeCount'][0] += 1
    if(elementText.find('Javascript') != -1 or elementText.find('javascript') != -1 or elementText.find('JavaScript') != -1) == True:
        globals()['langaugeCount'][1] += 1
    #looking for 'java' captialized or lowercased and return true if it doesn't return -1
    if((elementText.find('Java') != -1) or (elementText.find('java') != -1) == True and
    (elementText.find('Script',elementText.find('Java')) != -1) or (elementText.find('script',elementText.find('java')) != -1) == True):
    #looking to find 'script' after the word java in lowercase and uppercase
        #print('adding to java')
        globals()['langaugeCount'][2] += 1
    if(elementText.find('C/C++')!= -1) == True:
        globals()['langaugeCount'][3] += 1
    if(elementText.find('C#')!= -1) == True:
        globals()['langaugeCount'][4] += 1
    if(elementText.find('SQL')!= -1) == True:
        globals()['langaugeCount'][5] += 1
    if(elementText.find('PHP')!= -1) == True:
        globals()['langaugeCount'][6] += 1
    if(elementText.find('Matlab')!= -1) == True:
        globals()['langaugeCount'][7] += 1
    if(elementText.find('Swift')!= -1) == True:
        globals()['langaugeCount'][8] += 1
    if(elementText.find('Kotlin')!= -1) == True:
        globals()['langaugeCount'][9] += 1
    if(elementText.find('Assembly')!= -1) == True:
        globals()['langaugeCount'][10] += 1
    #print('this is in find_Languages ' + str(langaugeCount))

#run this to make sure it works
def create_plot():
    # df = pd.DataFrame(data = {"languages":codingLanguages, "Number":langaugeCount})
    # plt = df.plot.bar(x = "languages", y = "Number", title = "Languages from Indeed",legend = False)
    # #plt = df.plot.barh(rot = 0,legend = False)
    # plt.set_xlabel("Amount")
    # plt.set_ylabel("Languages")
    # plot.show(block=True)

    df = pd.DataFrame(data = {"Languages":globals()['codingLanguages'], "Amount":globals()['langaugeCount']})

    #globals()['jobCount'] = 15
    percentages = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
    for index in range(len(df)):
        #print(type(percentages[index]))
        percentages[index] = df['Amount'][index] / globals()['jobCount'] * 100
        if(percentages[index] != 0):
            percentages[index] = "{:.2f}%".format(percentages[index])
        else:
            percentages[index] = "{:.0f}%".format(percentages[index])
    print(percentages)
    df['%'] = percentages

    plt = df.plot.bar(x = "Languages", y = "Amount", title = "Languages from Indeed",legend = False)
    
    for i in range(len(globals()['codingLanguages'])):
        plt.text(i,globals()['langaugeCount'][i],globals()['langaugeCount'][i],ha = 'center')
    plt.set_ylabel("Amount")
    print(tabulate(df, tablefmt='plain-text'))
    plot.show(block=True)


if __name__ == '__main__':
   main()