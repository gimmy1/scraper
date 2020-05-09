from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument("--headless")
    # initialize driver
    driver = webdriver.Chrome(chrome_options=options)
    return driver

def connect_to_base(browser, page_number=1):
    # url = 'https://www.sec.gov/Archives/edgar/data/1341439/000119312518090656/0001193125-18-090656.txt'
    import pdb; pdb.set_trace()
    base_url = f"https://news.ycombinator.com/news?p={page_number}"
    connection_attempts = 0

    while connection_attempts < 3:
        try:
            browser.get(base_url)
            # wait for table element with id = "hnmain" to load 
            # before returning True
            wait = WebDriverWait(browser, 5)
            wait.until(EC.presence_of_element_located((By.ID, "hnmain")))
            return True
        except Exception as ex:
            connection_attempts += 1
            print(f"Error connecting to {self.base_url}")
            print(f"Connection attempt: {connection_attempts}")
    return False

# def parse_html(html):
#     # create soup object
#    soup = BeautifulSoup(html, "html.parser")
