#import selenium library
from selenium import webdriver

#open mozilla firefox
# driver = webdriver.Firefox(executable_path="geckodriver")
driver = webdriver.Firefox()

#Open Google Chrome
# driver = webdriver.Chrome(executable_path='/chromedriver')
# driver = webdriver.Chrome()
#open a web page online
driver.get('https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/introduction-to-the-new-testament-seminary-teacher-manual?lang=spa')