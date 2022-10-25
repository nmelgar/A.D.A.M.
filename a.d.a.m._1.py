# import selenium library
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
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
# web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/introduction-to-the-new-testament-seminary-teacher-manual?lang=spa"
# web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/1-3-john-jude?lang=spa"
web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/doctrinal-mastery-review-23?lang=spa"
# web_page_url = "https://www.churchofjesuschrist.org/study/manual/new-testament-seminary-teacher-manual-2023/assess-your-learning-11?lang=spa"
driver.get(web_page_url)

# maximize window
driver.maximize_window()

# to accept cookies of the website
ID_COOKIES = "truste-consent-button"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ID_COOKIES))
)
accept_cookies = driver.find_element(By.ID, ID_COOKIES).click()

try:
    next_page = "span.traversalLink-JrW0G:nth-child(4) > a:nth-child(1)"
    available_next_page = driver.find_elements(By.CSS_SELECTOR, next_page)
    
    # to run the program
    run = True

    while run:

        # will get the url of the site
        actual_url = driver.current_url

        # will get the title of the document by using h1
        title_page = driver.find_element(By.ID, 'title1').text

        # convert the actual webpage to pdf with the title of the h1
        pdfkit.from_url(actual_url, title_page)

        if len(available_next_page) == 0:           
            run = False
        else:
            # click to next page
            available_next_page[0].click()

except NoSuchElementException:
    print("Program is done")

# def main():
#     print("Hello World")

# if __name__ == "__main__":
#     main()
