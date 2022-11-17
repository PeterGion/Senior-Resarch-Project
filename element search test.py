
langaugeCount = []
codingLanguages = []
import pandas as pd
'''import matplotlib.backends.backend_tkagg
import pandas.plotting._matplotlib
matplotlib.use('tkagg')'''
import matplotlib.pyplot as plot


def main():
    #print(globals()['codingLanguages'])
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
    testing_Find()
    #print(globals()['codingLanguages'])
    #test_edit()
    #print(langaugeCount)
    #print(codingLanguages)
    #test()
    '''
    count = [78,30,70,25,3,150,4,2,5,6,7]
    langaugeCount = count
    #print(langaugeCount)
    #langaugeCount = [5,8,9,10]
    #test_list_incrementation(langaugeCount)
    #print(langaugeCount)
    '''
    

def testing_Find():
    withJava = 'Opportunity: Are you a Software Engineer looking to make a change? Does joining a team creating cutting edge software for the Architectural, Engineering and Construction (AEC) community excited you? \
    When you join our team at ASSA ABLOY, you will play a key role in charting the future development of software applications that guide users through the entire process of managing projects from estimating, detailing, and procuring doors, frames and related hardware through to project completion.\
    What you will be doing:\
    You will take a key role on a talented multi person team and work on the development and enhancements of software applications. You will write a large amount of code, design, communicate ideas to the team, implement and ultimately be able to step in and handle any component or the entire life cycle of the process. We have a fast-moving environment where you may have multiple projects - new development, upgrades, \
    enhancements, etc.\
    You will for certain use a wide range of programming skills in completing these tasks.\
    Specific activities will include:\
    Writing:\
    Java code, HTML, Javascript, SQL.\
    Evaluating:\
    Requested changes/enhancements to size requests.\
    Software products to be offered in conjunction with existing products.\
    Development, test and productivity tools.\
    Operating environments required for application usage.\
    Extension of the application onto mobile platforms.\
    Determining:\
    How to incorporate requests into the existing database structure and multi-language codebase.\
    End user hardware and software requirements for product installations.\
    Developing and/or identifying:\
    Integration of internal and external product design into a cohesive user experience.\
    Requirements for a requested software change/enhancement.\
    Automated test capabilities through software design.\
    Paths from existing to future software architectures.\
    Maintaining:\
    Documentation and coding standards.\
    Up-to-date knowledge of technological advances.\
    What skills and experience you should have:\
    A bachelor\'s degree, coding bootcamp, in Engineering, Computer Science, or related major, or relevant experience.\
    Experience with object-oriented programming in Java.\
    Experience with Java frameworks such as Spring and Hibernate/JPA, as well as Servlet containers like Tomcat, Jetty, or WildFly.\
    Proficiency with Java builds tools such as Maven and Gradle.\
    Proficiency with Git.\
    Experience utilizing Eclipse, IntelliJ, or Netbeans IDEs.\
    Experience using a SQL database engine and accessing data via JDBC or an ORM, as well as writing SQL.\
    Solid understanding of object-, component- and service-oriented design principles.\
    Experience with GWT and specifically SmartGWT frameworks, SmarGWT Version 12 or 13 with enterprise level features preferred. Both client and server-side development experience a plus.\
    We seek talent with:\
    Exceptional interpersonal and communication skills, including the ability to act as a bridge between non-technical users and technical resources.\
    The ability to:\
    Perform against tight deadlines and multi-task effectively.\
    Work effectively with groups of varying technical expertise.\
    Excel at both working independently and in a group setting.\
    Strong self-motivation balanced with a desire to achieve team goals.\
    We are the ASSA ABLOY Group\
    Our people have made us the global leader in access solutions. In return, we open doors for them wherever they go. With nearly 51,000 colleagues in more than 70 different countries, we help billions of people experience a more open world. Our innovations make all sorts of spaces – physical and virtual – safer, more secure, and easier to access.\
    As an employer, we value results – not titles, or backgrounds. We empower our people to build their career around their aspirations and our ambitions – supporting them with regular feedback, training, and development opportunities. Our colleagues think broadly about where they can make the most impact, and we encourage them to grow their role locally, regionally, or even internationally.\
    As we welcome new people on board, it’s important to us to have diverse, inclusive teams, and we value different perspectives and experiences.'
    #print((withoutJava.find('Script',withoutJava.find('Java')) != -1) == True)
    #print((withJava.find('Java') != -1) or (withJava.find('java') != -1) == True)
    #print((withJava.find('Script',withJava.find('Java')) != -1) or (withJava.find('script',withJava.find('java')) != -1) == True)
    #print((withJava.find('Java') != -1) or (withJava.find('java') != -1) == True and (withJava.find('Script',withJava.find('Java')) != -1) or (withJava.find('script',withJava.find('java')) != -1) == True)
    print((withJava.find('Javascript') != -1 or withJava.find('javascript') != -1 or withJava.find('JavaScript') != -1) == True)
    print((withJava.find('Java') != -1) or (withJava.find('java') != -1) == True and
        (withJava.find('Script',withJava.find('Java')) != -1) or (withJava.find('script',withJava.find('java')) != -1) == True)

def test_list_incrementation(list):
    list.append(1)
    print(list)
    list.append(1)
    print(list)
    langaugeCount = list
    print(langaugeCount)
def create_plot():
    df = pd.DataFrame(data = {"languages":codingLanguages, "Number":langaugeCount})
    plt = df.plot.barh(x = "languages", y = "Number", title = "Languages from Indeed",legend = False)
    #plt = df.plot.barh(rot = 0,legend = False)
    plt.set_xlabel("Amount")
    plt.set_ylabel("Languages")
    plot.show(block=True)
def test():
    print(codingLanguages)
def test_edit():
    globals()['langaugeCount'][0] = 69
    print(globals()['langaugeCount'])
    print(globals()['langaugeCount'][0])


if __name__ == '__main__':
    main()
