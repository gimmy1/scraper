


# options = webdriver.ChromeOptions()
# # pass in headless argument to options
# options.add_argument("--headless")
# # intialize driver
# browser = webdriver.Chrome(options=options)
# browser.get("https://www.reddit.com/r/AskReddit/")

# search_form = browser.find_element_by_id("search_form_input_homepage")
# search_form.send_keys("real_python")

# search_form.submit()


# results = browser.find_elements_by_class_name("result")
# print(results[0].text)
# browser.close()
# quit()

from scrapers.scraper import get_driver, connect_to_base

if __name__ == "__main__":
    browser = get_driver()
    connect_to_base(browser)
