#cd C:\Users\Peter\"OneDrive - Eastern Connecticut State University"\"senior resarch"\Scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import pandas as pd


driver = webdriver.Chrome(executable_path='C:\\Users\\Peter\\OneDrive - Eastern Connecticut State University\\senior resarch\\Scraper\\chromedriver.exe')
driver.get("https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=e5f9a4020f0cbf61&advn=5555284187286628&from=gnav-util-jobsearch--indeedmobile")
#class jcs-JobTitle
time.sleep(1)
jobDescription = driver.find_element(By.CLASS_NAME,"jobsearch-jobDescriptionText")
time.sleep(1)
ActionChains(driver).move_to_element(jobDescription).perform()
codingLanguages = [
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
langaugeCount = [0,0,0,0,0,0,0,0,0,0]
elements = jobDescription.find_elements(By.TAG_NAME,"p,ul")
def find_elements():
    for element in elements:
        elementText = element.text
        print(element.text)
        if(elementText.find('Python')!= -1 or elementText.find('python')!= -1) == True:
            langaugeCount[0] += 1
        if(elementText.find('Javascript') != -1 or elementText.find('javascript') != -1 or elementText.find('JavaScript') != -1) == True:
            langaugeCount[1] += 1
        #looking for 'java' captialized or lowercased and return true if it doesn't return -1
        if((elementText.find('Java') != -1) or (elementText.find('java') != -1) == True and
        (elementText.find('Script',elementText.find('Java')) != -1) or (elementText.find('script',elementText.find('java')) != -1) == True):
        #looking to find 'script' after the word java in lowercase and uppercase
            langaugeCount[2] += 1
        if(elementText.find('C/C++')!= -1) == True:
            langaugeCount[3] += 1
        if(elementText.find('C#')!= -1) == True:
            langaugeCount[4] += 1
        if(elementText.find('SQL')!= -1) == True:
            langaugeCount[5] += 1
        if(elementText.find('PHP')!= -1) == True:
            langaugeCount[6] += 1
        if(elementText.find('Matlab')!= -1) == True:
            langaugeCount[7] += 1
        if(elementText.find('Swift')!= -1) == True:
            langaugeCount[8] += 1
        if(elementText.find('Kotlin')!= -1) == True:
            langaugeCount[9] += 1
        if(elementText.find('Assembly')!= -1) == True:
            langaugeCount[10] += 1
print(codingLanguages)
print(langaugeCount)
'''
    
    elif element.text.casefold().find('C#'):
        langaugeCount[2] += 1
    elif element.text.casefold().find('SQL'):
        langaugeCount[3] += 1
    elif element.text.casefold().find('Go'):
        langaugeCount[4] += 1
    elif element.text.casefold().find('Matlab'):
        langaugeCount[5] += 1
    elif element.text.casefold().find('swift'):
        langaugeCount[6] += 1
    elif element.text.casefold().find('Kotlin'):
        langaugeCount[7] += 1
    elif element.text.casefold().find('Assembly'):
        langaugeCount[8] += 1
    elif element.text.casefold().find('PHP'):
        langaugeCount[9] += 1
print(langaugeCount)
'''
'''
jobDescriptionText = jobDescription.text
print('Python'.casefold() in jobDescriptionText)
if'Python'.casefold() in jobDescriptionText:
    langaugeCount[0] += 1
if 'Javascript'.casefold() in jobDescriptionText:
    langaugeCount[1] += 1
if 'C#' in jobDescriptionText:
    langaugeCount[2] += 1
if 'SQL' in jobDescriptionText:
    langaugeCount[3] += 1
if 'Go' in jobDescriptionText:
    langaugeCount[4] += 1
if 'Matlab' in jobDescriptionText:
    langaugeCount[5] += 1
if 'swift' in jobDescriptionText:
    langaugeCount[6] += 1
if 'Kotlin' in jobDescriptionText:
    langaugeCount[7] += 1
if 'Assembly' in jobDescriptionText:
    langaugeCount[8] += 1
if 'PHP' in jobDescriptionText:
    langaugeCount[9] += 1
print(langaugeCount)
'''
'''
print("this is the start of the job description")
print(jobDescription)

pythonCount = 0
javascriptCount = 0
javaCount = 0
cSharpCount = 0
sQLCount = 0
goCount = 0
matlabCount = 0
swiftCount = 0
kotlinCount = 0
assemblyCount = 0
pHPCount = 0

codingLanguages = [
    'Python',
    'Javascript',
    'Java',
    'C#',
    'SQL',
    'Go',
    'Matlab',
    'Swift',
    'Kotlin',
    'Assembly',
    'PHP'
]
print('this is the start of the tags')
langaugeCount = []
'''
'''
for tag in jobDescription:
    print(tag.get_text())
    if'Python'.casefold() in tag.get_text():
        pythonCount += 1
    elif 'Javascript'.casefold() in tag.get_text():
        javascriptCount += 1
    elif 'C#' in tag.get_text():
        cSharpCount += 1
    elif 'SQL' in tag.get_text():
        sQLCount += 1
    elif 'Go' in tag.get_text():
        goCount += 1
    elif 'Matlab' in tag.get_text():
        matlabCount += 1
    elif 'swiftCount' in tag.get_text():
        swiftCount += 1
    elif 'Kotlin' in tag.get_text():
        kotlinCount += 1
    elif 'Assembly' in tag.get_text():
        assemblyCount += 1
    elif 'PHP' in tag.get_text():
        pHPCount += 1
'''
'''
for tag in jobDescription:
    print(tag.get_text())
    if'Python'.casefold() in tag.get_text():
        langaugeCount[0] += 1
    elif 'Javascript'.casefold() in tag.get_text():
        langaugeCount[1] += 1
    elif 'C#' in tag.get_text():
        langaugeCount[2] += 1
    elif 'SQL' in tag.get_text():
        langaugeCount[3] += 1
    elif 'Go' in tag.get_text():
        langaugeCount[4] += 1
    elif 'Matlab' in tag.get_text():
        langaugeCount[5] += 1
    elif 'swift' in tag.get_text():
        langaugeCount[6] += 1
    elif 'Kotlin' in tag.get_text():
        langaugeCount[7] += 1
    elif 'Assembly' in tag.get_text():
        langaugeCount[8] += 1
    elif 'PHP' in tag.get_text():
        langaugeCount[9] += 1

df = pd.DataFrame(data={'language':codingLanguages, 'number of occurances':langaugeCount})
df
'''
