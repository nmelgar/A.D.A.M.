# import selenium library
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import pdfkit


# open mozilla firefox
driver = webdriver.Firefox(executable_path="geckodriver")
# driver = webdriver.Firefox()

# Open Google Chrome
# driver = webdriver.Chrome(executable_path='/chromedriver')
# driver = webdriver.Chrome()

options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Firefox(options=options)

# open a web page online
driver.get('https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/introduction-to-the-new-testament-seminary-teacher-manual?lang=spa')

# maximize window
driver.maximize_window()

# to accept cookies of the website
ID_COOKIES = "truste-consent-button"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ID_COOKIES))
)
accept_cookies = driver.find_element(By.ID, ID_COOKIES).click()

# will get the url of the site
actual_url = driver.current_url

# will get the title of the webpage
title_page = driver.find_element(By.ID, 'title1').text

# convert the actual webpage to pdf with the title of the h1
pdfkit.from_url(actual_url, title_page)
