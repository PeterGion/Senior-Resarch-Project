languages = ['Python', 'C', 'C++', 'C#', 'Java']
enum_iter = enumerate(languages)
for index, elem in enum_iter:
    #print(jobPannels[i].tag_name)
    #print(jobPannels[i].get_attribute)
    #ActionChains(driver).move_to_element(jobPannels[i]).perform()
    #wait = WebDriverWait(driver, 15)
    #wait.until(EC.element_to_be_clickable(jobPannels[i]))
    #time.sleep(1)
    #jobPannels[i].click()
    print(index, elem)
    if elem == "Python":
        index1, elem1 = next(enum_iter)
        print(index1, elem1, "*")
    
    #print(jobPannels[i].click().__getattribute__)