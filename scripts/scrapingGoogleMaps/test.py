from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()

browser = webdriver.Chrome(options=options)

url = "https://www.google.com.br/maps/search/pizza/@-7.9167485,-34.8955189,15z?entry=ttu"

browser.get(url)


def scroll_the_page(driver, scrollable_div):
    try:
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "section-layout-root")))

        pause_time = 2
        max_count = 5
        x = 0

        while (x < max_count):
            try:
                ActionChains(driver).scroll_to_element(
                    scrollable_div).perform()
                # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
            except:
                pass
            time.sleep(pause_time)
            x = x+1
    except:
        driver.quit()


# review titles / username / Person who reviews

review_titles = browser.find_elements(
    By.CLASS_NAME, "hfpxzc")
for i in review_titles:
    i.click()
    time.sleep(5)
    element = browser.find_element(
        By.CLASS_NAME, "lMbq3e")
    print(element.text)
    print("----")
    time.sleep(2)
    scrollable_div = browser.find_element(By.CLASS_NAME,
                                          'AeaXub')
    scroll_the_page(browser, scrollable_div)
    phone = browser.find_element(
        By.CLASS_NAME, "rogA2c")
    print(phone.text)
    print("----")
    site = browser.find_elements(
        By.CLASS_NAME, "AeaXub")
    for j in site:
        print("j", j.text)
    print(site)
    print("----")
    address = browser.find_element(
        By.CLASS_NAME, "Io6YTe")
    print(address.text)
    print("----")

    # print(element.text)

print([review_titles])
print([a.text for a in review_titles])

# review text / what did they think

review_text = browser.find_elements_by_class_name(
    "section-review-review-content")

print([a.text for a in review_text])

# get the number of stars

stars = browser.find_elements_by_class_name("section-review-stars")

first_review_stars = stars[0]

active_stars = first_review_stars.find_elements_by_class_name(
    "section-review-star-active")

print(f"the stars the first review got was {len(active_stars)}")
