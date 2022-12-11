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
from datetime import datetime

#orginal intial link 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&from=searchOnHP&vjk=d09ebd87acd223b8'
#second iteration link 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=210&pp=gQE7AAAAAAAAAAAAAAAB8SMfdgDZAQQBLFoKFgpuDAD79s41_w3Tm8mlDV_8crKDg-pPvmJDw7sx9fj6j7kFax3kNHqjXIB1ytLD5gRkXSPhCkxVfG9NjWYK38ViW-7mSd7tOdT_Z9thnHR_OT0lp-eeM3n4kY6afuWt5Welm-tHnl1UxSTNPj5q4TdBg43VLsFOGFIeILRkemehd4hx92hQOHH4XJ4Si0eAuYL_CwxFGo9o_4rl0pmsRPdtwb5laTQZ5bBN3k_-jOm8auWNTq7MKHt0MGMkVE0bWw3hJYvcuHUp5kkY361WanB_xAAA&vjk=3136008da9d512bc'
#third iteration 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=240&pp=gQF3AAABhPxrSFYAAAAB8SMfdgDaAQQBJ1AakgELQAYBfloBH2xj5q31G11MXpVqpqAYSVN2UxwVy5z7dcGTFMXIjIQiZ10gNSeDTBBxcRNL-fgYzUx36kxJ8fI5ABlqFFE-XstyybYAw06ViaaEE75yi_gT2EoBG77i8NArQF1iRSFFCGWtYetJKtVIMWKtYwFc3NxP8uWSJMOJgxMTGEdoPdbX3SOgzB7TFHbjH8KpsIOfjzjoqntI3b7L93ueWOI95_9VugMuEctQlfveEk6VL9fR9WP5gA4huZjBhEK5452rSmXqBgt4ir3D2OgAAA&vjk=dc08bc8430b3cb68'
#fourth iteration 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=300&pp=gQHCAAABhP09MyAAAAAB8SMfdgD0AQYBRIwBDSgHEAgYDkgHA2xkR8CfxPTew33B4VHKKgGAVzoQRJYneL0RMstXCj7aZqnGARUwzwZhv9jjZJH4ocH_ACKy-8hg98F7EceKqK0UxpCFCvUjWOuSmPCCpFzXuhl7iZ5KCULbAF-zTbYKsbYJUXUgDma6lWlvxh1Oi0aHl2HplhdVYyJAxRONpphLEaa5Om7jkRTFI95d_Otn5xn3EdnBmvGYfqvbn6bNUIMqLRT2Q2lQvn3ZZThMPJgwllTSPADBR8OfB6BmaxEiAmcCOAylv2zpyuoB3-AJAiJrN8-HdaYd7pYnWDnfX4w8qokCQQAA&vjk=e5778ae092c5a8e6'
#last page url 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=480&pp=gQLQAAAAAAAAAAAAAAAB8SMfdgCpAQIBIWoHF9LctcuqedDkIQ0B_bvLDQPvJEgzpL-sZt4diEKLkULhQt6umozoDwYl99nEcLf6pzE-iFaSl7TAO4D_DyADAsSCbZp6AXY7PdqsSYe1lXxMEHXfo2zFhB21nplycfTyE769YqwyhCfsQIcqelMAavMOe7f2TGik0CSMBV6Lavp6oGSABR5miyTxRdQS1GhbKQQhPx2UdYDVt-2ARIpjxB5ZKgAA&vjk=df9b21b48b69e8a3'

 
intialLink = 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&from=searchOnHP&vjk=f8ef50a012b552b9&advn=2277496059378972'

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
    #globals()['langaugeCount'] = [34,238,363,34,114,273,39,4,16,8,2]
    driver.get(intialLink)
    #checking if the last page element is there
    lastPageElement = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
    #goThoughSetPages(driver, jobPannels, lastPageElement, 1)Gionfriddo
    #jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
    #allJobListings(driver,jobPannels)
    goThoughPages(driver, lastPageElement)
    #print(globals()['langaugeCount'])
    #run this to make sure it works
    create_plot()


def systemTime():
    now = datetime.now()
    return now.strftime("%I:%M:%S")
    

def generateSeconds():
    randomTime = randint(10,30)
    print(str(randomTime) + ' was randomly created at: ' + systemTime())
    return randomTime


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
    pageNbr = 0
    while(len(element) != 0):
        #all other logic will go here
        print()
        print('starting page ' + str(pageNbr))
        print('***************************************************************************************************************************')
        jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
        allJobListings(driver,jobPannels)
        ActionChains(driver).move_to_element(element[0]).perform()
        driver.execute_script("window.scrollBy(0 , " + str(jobPannels[0].size['height']) + " );")
        time.sleep(generateSeconds())
        element[0].click()
        element = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
        print('leaving page ' + str(pageNbr) + ' going to ' + str(pageNbr+ 1))
        pageNbr += 1
    #run again on the last page
    jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
    allJobListings(driver,jobPannels)
        

def allJobListings(driver,jobPannels):
    #the first jobdescription is always selected so there is no point in wasting time clicking on it
    time.sleep(2)
    jobDescription = findJobDescription(driver)
    find_Languages(jobDescription)
    #print(globals()['langaugeCount'])
    for job in range(1, len(jobPannels)):
        if(len(jobPannels[job].find_elements(By.CSS_SELECTOR,"#mosaic-afterFifthJobResult")) == 0 and 
        len(jobPannels[job].find_elements(By.CSS_SELECTOR,"#mosaic-afterTenthJobResult")) == 0 and
        len(jobPannels[job].find_elements(By.CSS_SELECTOR,"#mosaic-afterFifteenthJobResult")) == 0):
            time.sleep(generateSeconds())
            print('joblisting: ' + str(job) + ' ' + systemTime())
            #time.sleep(5)
            ActionChains(driver).move_to_element(jobPannels[job]).perform()
            driver.execute_script("window.scrollBy(0 , " + str(jobPannels[job].size['height']) + " );")
            #print(jobPannels[job].text)
            jobPannels[job].click()
            time.sleep(2)
            jobDescription = findJobDescription(driver)
            find_Languages(jobDescription)
            globals()['jobCount'] += 1
            updateCsv()


def findJobDescription(driver):
    #class jcs-JobTitle
    #jobDescription = seleniumDriver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    jobDescription = driver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    time.sleep(2)
    #time.sleep(generateSeconds())
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
    #print(percentages)
    df['%'] = percentages

    plt = df.plot.bar(x = "Languages", y = "Amount", title = "Languages from Indeed",legend = False)
    
    for i in range(len(globals()['codingLanguages'])):
        plt.text(i,globals()['langaugeCount'][i],globals()['langaugeCount'][i],ha = 'center')
    plt.set_ylabel("Amount")
    df.sort_values(by='Amount', inplace=True, ascending=False)
    print(tabulate(df,headers='keys', tablefmt='plain-text'))
    plot.show(block=True)


if __name__ == '__main__':
   main()