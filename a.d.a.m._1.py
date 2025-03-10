# import selenium library
from turtle import title
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import pdfkit

# open mozilla firefox
driver = webdriver.Firefox(executable_path="geckodriver")
# driver = webdriver.Firefox()

# Open Google Chrome
# driver = webdriver.Chrome(executable_path='/chromedriver')
# driver = webdriver.Chrome()

options = Options()

driver = webdriver.Firefox(options=options)

# open a web page online
web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/introduction-to-the-new-testament-seminary-teacher-manual?lang=spa"
# web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023?lang=spa"
# web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/matthew-3-13-17-part-2?lang=eng"

driver.get(web_page_url)

# maximize window
driver.maximize_window()

# to accept cookies of the website
ID_COOKIES = "truste-consent-button"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ID_COOKIES))
)
accept_cookies = driver.find_element(By.ID, ID_COOKIES).click()

# to run the program
run = True
name_counter = 0
next_page = "span.traversalLink-JrW0G:nth-child(4) > a:nth-child(1)"
# available_next_page = driver.find_elements(By.CSS_SELECTOR, next_page)
available_next_page = driver.find_element(By.CSS_SELECTOR, next_page)


while available_next_page:
    options.page_load_strategy = 'normal'

    # will get the title of the document by using h1
    title_page = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div/main/div/div[2]/header/span').text
    # will get the url of the site so it can be downloaded as PDF
    actual_url = driver.current_url
    if name_counter < 10:
        full_name = f"00{name_counter}"
        file_name = f"{full_name}. {title_page}.pdf"

    elif name_counter > 9:
        full_name = f"0{name_counter}"
        file_name = f"{full_name}. {title_page}.pdf"
        # file_name = f"{name_counter}"

    # convert the actual webpage to pdf with the title of the h1
    pdfkit.from_url(actual_url, file_name)

    name_counter = name_counter + 1

    # next_page_wait = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, next_page))
    # )
    # driver.implicitly_wait(90)
    time.sleep(15)
    available_next_page.click()