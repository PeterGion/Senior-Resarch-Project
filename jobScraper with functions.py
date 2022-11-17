#cd C:\Users\Peter\"OneDrive - Eastern Connecticut State University"\"senior resarch"\Scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import pandas as pd
import matplotlib.pyplot as plot
'https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile'
intialLink = "https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=d2a438c96f6e9c7e&from=gnav-util-jobsearch--indeedmobile"

codingLanguages = []
langaugeCount = []
driver = None

def main():
    globals()['driver'] = webdriver.Chrome(executable_path='C:\\Users\\Peter\\OneDrive - Eastern Connecticut State University\\senior resarch\\Scraper\\chromedriver.exe')
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
    globals()['driver'].get(intialLink)
    
    jobDescription = findJobDescription()
    find_Languages(jobDescription)
    create_plot()
    

def findJobDescription():
    #class jcs-JobTitle
    time.sleep(1)
    #jobDescription = seleniumDriver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    jobDescription = globals()['driver'].find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
    time.sleep(1)
    ActionChains(globals()['driver']).move_to_element(jobDescription).perform()
    return jobDescription


def find_Languages(element):
    #print(element.text)
    #time.sleep(1)
    elementText = element.text
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