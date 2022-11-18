#cd C:\Users\Peter\"OneDrive - Eastern Connecticut State University"\"senior resarch"\Scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import matplotlib.pyplot as plot

'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile'
#last page url 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=480&pp=gQLQAAABhIeCedIAAAAB7hgVOgC7AQQBJ2oGDgc-BgQGOajjWXbVPKtoxz6gCwrUiOulV1DE8uIWhUoN96a_OuBT8U_7MVbePCJ-LGFcdnO782Xn_FHn_kyCyXzXzUApJebFu3ZPLcBJ7fR3OAKkzXXF7yin61pkBkXh0NtyPYQkbIV6AQywYLj9_Svtj_2y5YhVU1Ak0d7D0YfDB32euOSKGPhbdg1WLeCKNO8mN10bZM35cPeLX_vBSufZLhQmk3ygIaMFnrjAdYemIt0iIAAA&vjk=58cab7537268f79a'
intialLink = 'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile'

codingLanguages = None
langaugeCount = None

def main():
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
    globals()['langaugeCount'] = [0,0,0,0,0,0,0,0,0,0,0]
    driver.get(intialLink)
    
    
    lastPageElement = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")
    
    while(len(lastPageElement) != 0):
        time.sleep(3)
        #all other logic will go here
        #jobPannels = driver.find_elements(By.CLASS_NAME,"jobsearch-ResultsList > li")
        
        #this is not going to be here in the final version
        ActionChains(driver).move_to_element(lastPageElement[0]).perform()
        time.sleep(1)
        lastPageElement[0].click()
        lastPageElement = driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")

    # print(len(driver.find_elements(By.CSS_SELECTOR,".css-jbuxu0 > div:last-child > a[aria-label=\"Next Page\"]")))
    #onlyTwo(driver, jobAnchors)
    #create_plot()


def onlyTwo(driver,jobPannels):
    for i in range(4):
        time.sleep(5)
        ActionChains(driver).move_to_element(jobPannels[i]).perform()
        time.sleep(5)
        jobPannels[i].click()
        time.sleep(3)
        jobDescription = findJobDescription(driver)
        find_Languages(jobDescription)


def allJobListings(driver, jobPannels):
    for job in jobPannels:
        if len(job.find_elements(By.ID,'mosaic-afterFifthJobResult')) == 0:
            time.sleep(5)
            ActionChains(driver).move_to_element(job).perform()
            time.sleep(1)
            job.click()
            #job = wait.until(EC.invisibility_of_element_located(job))
            #job = wait.until(EC.element_to_be_clickable(job))
            #job.click()
            #jobDescription = findJobDescription(driver)
            #find_Languages(jobDescription)
            #create_plot()
            time.sleep(5)


def findJobAnchors():
    jobAnchors =  globals()['driver'].find_elements(By.CLASS_NAME,"jcs-JobTitle")
    print(len(jobAnchors))
    return jobAnchors


def findJobDescription(driver):
    #class jcs-JobTitle
    #jobDescription = seleniumDriver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    jobDescription = driver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    time.sleep(1)
    ActionChains(driver).move_to_element(jobDescription).perform()
    return jobDescription


def find_Languages(element):
    elementText = element.text
    if(elementText.find('Python')!= -1 or elementText.find('python')!= -1) == True:
        globals()['langaugeCount'][0] += 1
    if(elementText.find('Javascript') != -1 or elementText.find('javascript') != -1 or elementText.find('JavaScript') != -1) == True:
        globals()['langaugeCount'][1] += 1
        print('this is going off')
    #looking for 'java' captialized or lowercased and return true if it doesn't return -1
    if((elementText.find('Java') != -1) or (elementText.find('java') != -1) == True and
    (elementText.find('Script',elementText.find('Java')) != -1) or (elementText.find('script',elementText.find('java')) != -1) == True):
    #looking to find 'script' after the word java in lowercase and uppercase
        print('adding to java')
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
    print('this is in find_Languages ' + str(langaugeCount))

    
def find_LanguagesOG(element):
    print('gets to find_languages')
    #print(element.text)
    elements = element.find_elements(By.TAG_NAME,"p,ul")
    #print(element.text)
    time.sleep(1)
    for tagElement in elements:
        print('started for loop')
        elementText = tagElement.text
        #print('got this far')
        #print(element.text)
        if(elementText.find('Python')!= -1 or elementText.find('python')!= -1) == True:
            globals()['langaugeCount'][0] += 1
        if(elementText.find('Javascript') != -1 or elementText.find('javascript') != -1 or elementText.find('JavaScript') != -1) == True:
            globals()['langaugeCount'][1] += 1
            print('this is going off')
        #looking for 'java' captialized or lowercased and return true if it doesn't return -1
        if((elementText.find('Java') != -1) or (elementText.find('java') != -1) == True and
        (elementText.find('Script',elementText.find('Java')) != -1) or (elementText.find('script',elementText.find('java')) != -1) == True):
        #looking to find 'script' after the word java in lowercase and uppercase
            print('adding to java')
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
    print('this is in find_Languages ' + str(langaugeCount))

def create_plot():
    df = pd.DataFrame(data = {"languages":codingLanguages, "Number":langaugeCount})
    plt = df.plot.barh(x = "languages", y = "Number", title = "Languages from Indeed",legend = False)
    #plt = df.plot.barh(rot = 0,legend = False)
    plt.set_xlabel("Amount")
    plt.set_ylabel("Languages")
    plot.show(block=True)


if __name__ == '__main__':
    main()