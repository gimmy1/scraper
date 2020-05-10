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
    # base_url = "https://www.sec.gov/Archives/edgar/data/1341439/000119312518090656/0001193125-18-090656.txt"
    base_url = f"https://news.ycombinator.com/news?p={page_number}"
    connection_attempts = 0

    while connection_attempts < 3:
        try:
            browser.get(base_url)
            # wait for table element with id = "hnmain" to load 
            # before returning True
            # wait = WebDriverWait(browser, 5)
            # wait.until(EC.presence_of_element_located((By., "hnmain")))
            return True
        except Exception as ex:
            connection_attempts += 1
            print(f"Error connecting to {self.base_url}")
            print(f"Connection attempt: {connection_attempts}")
    return False

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    output_list = []
    # parse soup object to get article id, rank, score, and title
    tr_blocks = soup.find_all("tr", class_="athing")
    article = 0
    for tr in tr_blocks:
        article_id = tr.get("id")
        article_url = tr.find_all("a")[1]["href"]
        # check if article is a hacker news article
        if "item?id=" in article_url:
            article_url = f"https://news.ycombinator.com/{article_url}"
        load_time = get_load_time(article_url)

        try:
            score = soup.find(id=f'score_{article_id}').string
        except Exception as ex:
            score = '0 points'
        
        article_info = {
            'id': article_id,
            'load_time': load_time,
            'rank': tr.span.string,
            'score': score,
            'title': tr.find(class_='storylink').string,
            'url': article_url
        }

def get_load_time(url):
    try:
        # set headers
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # make get request to article_url
        response = requests.get(
            article_url, headers=headers, stream=True, timeout=3.000)
        # get page load time
        load_time = response.elapsed.total_seconds()
    except Exception as ex:
        load_time = 'Loading Error'
    return load_time


