from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class WebDriver:

    location_data = {}

    def __init__(self):
        self.PATH = "chromedriver.exe"
        self.options = Options()
        # self.options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        self.SITE_MAP = {
            "buttons": {
                "object_location": {
                    "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]",
                    "class_name": "Nv2PK THOPZb CpccDe "
                }
            },
            "name_location": {
                "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1/span[1]",
                "class_name": "DUwDvf lfPIob"
            },
            "ratings": {
                "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]",
                "class_name": "F7nice"
            },
            "site": {
                "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/a/div/div[2]/div[1]",
                "class_name": "rogA2c ITvuef"
            },
            "phone": {
                "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[6]/button/div/div[2]/div[1]",
                "class_name": "rogA2c"
            },
            "address": {
                "x_path": "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[3]/button/div/div[2]/div[1]",
                "class_name": "Io6YTe fontBodyMedium kR99db"
            },
        }
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

        self.location_data["rating"] = "NA"
        self.location_data["reviews_count"] = "NA"
        self.location_data["location"] = "NA"
        self.location_data["contact"] = "NA"
        self.location_data["website"] = "NA"
        self.location_data["Time"] = {"Monday": "NA", "Tuesday": "NA", "Wednesday": "NA",
                                      "Thursday": "NA", "Friday": "NA", "Saturday": "NA", "Sunday": "NA"}
        self.location_data["Reviews"] = []
        self.location_data["Popular Times"] = {"Monday": [], "Tuesday": [
        ], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

    def click_open_close_time(self):

        if (len(list(self.driver.find_elements(By.CLASS_NAME, "lI9IFe"))) != 0):
            element = self.driver.find_element(
                By.CLASS_NAME, "lI9IFe")
            self.driver.implicitly_wait(5)
            print("element", element)
            ActionChains(self.driver).move_to_element(
                element).click(element).perform()

    def click_all_reviews_button(self):

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "allxGeDnJMl__button")))

            element = self.driver.find_element(By.CLASS_NAME,
                                               "allxGeDnJMl__button")
            element.click()
        except:
            self.driver.quit()
            return False

        return True

    def get_location_data(self):

        try:
            element = self.driver.find_elements(
                By.CLASS_NAME, self.SITE_MAP["buttons"]["object_location"]["class_name"])
            for i in element:
                print("i", i)
                i.click()
                avg_rating = self.driver.find_element(By.CLASS_NAME,
                                                      self.SITE_MAP["ratings"]["class_name"])
                print("avg_rating", avg_rating.text)
                # total_reviews = self.driver.find_element(By.CLASS_NAME,self.SITE_MAP[""])
                address = self.driver.find_element(By.CLASS_NAME,
                                                   self.SITE_MAP["address"]["class_name"])
                phone_number = self.driver.find_element(By.CLASS_NAME,
                                                        self.SITE_MAP["phone"]["class_name"])
                website = self.driver.find_element(By.CLASS_NAME,
                                                   self.SITE_MAP["site"]["class_name"])
        except:
            print("Error in getting location data")
            pass
        try:
            self.location_data["rating"] = avg_rating.text
            # self.location_data["reviews_count"] = total_reviews.text[1:-1]
            self.location_data["location"] = address.text
            self.location_data["contact"] = phone_number.text
            self.location_data["website"] = website.text
        except:
            print("Error in setting location data")
            pass

    def get_location_open_close_time(self):

        try:
            days = self.driver.find_elements(By.CLASS_NAME,
                                             "lo7U087hsMA__row-header")
            times = self.driver.find_elements(By.CLASS_NAME,
                                              "lo7U087hsMA__row-interval")

            day = [a.text for a in days]
            open_close_time = [a.text for a in times]

            for i, j in zip(day, open_close_time):
                self.location_data["Time"][i] = j

        except:
            pass

    def get_popular_times(self):
        try:
            a = self.driver.find_elements(By.CLASS_NAME,
                                          "section-popular-times-graph")
            dic = {0: "Sunday", 1: "Monday", 2: "Tuesday",
                   3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
            l = {"Sunday": [], "Monday": [], "Tuesday": [],
                 "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}
            count = 0

            for i in a:
                b = i.find_elements(By.CLASS_NAME, "section-popular-times-bar")
                for j in b:
                    x = j.get_attribute("aria-label")
                    l[dic[count]].append(x)
                count = count + 1

            for i, j in l.items():
                self.location_data["Popular Times"][i] = j
        except:
            pass

    def scroll_the_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-layout-root")))

            pause_time = 2
            max_count = 5
            x = 0

            while (x < max_count):
                scrollable_div = self.driver.find_element(By.CLASS_NAME,
                                                          'k7jAl miFGmb lJ3Kh ')
                try:
                    self.driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
                except:
                    pass
                time.sleep(pause_time)
                x = x+1
        except:
            self.driver.quit()

    def expand_all_reviews(self):
        try:
            element = self.driver.find_elements(By.CLASS_NAME,
                                                "section-expand-review")
            for i in element:
                i.click()
        except:
            pass

    def get_reviews_data(self):
        try:
            review_names = self.driver.find_elements(By.CLASS_NAME,
                                                     "section-review-title")
            review_text = self.driver.find_elements(By.CLASS_NAME,
                                                    "section-review-review-content")
            review_dates = self.driver.find_elements(By.CSS_SELECTOR,
                                                     "[class='section-review-publish-date']")
            review_stars = self.driver.find_elements(By.CSS_SELECTOR,
                                                     "[class='section-review-stars']")

            review_stars_final = []

            for i in review_stars:
                review_stars_final.append(i.get_attribute("aria-label"))

            review_names_list = [a.text for a in review_names]
            review_text_list = [a.text for a in review_text]
            review_dates_list = [a.text for a in review_dates]
            review_stars_list = [a for a in review_stars_final]

            for (a, b, c, d) in zip(review_names_list, review_text_list, review_dates_list, review_stars_list):
                self.location_data["Reviews"].append(
                    {"name": a, "review": b, "date": c, "rating": d})

        except Exception as e:
            pass

    def scrape(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            self.driver.quit()
            return
        time.sleep(10)

        # self.click_open_close_time()
        self.get_location_data()
        # self.get_location_open_close_time()
        # self.get_popular_times()
        time.sleep(5)
        self.scroll_the_page()
        self.expand_all_reviews()
        self.get_reviews_data()
        self.driver.quit()

        return (self.location_data)


url = "https://www.google.com.br/maps/search/escola+na+Regi%C3%A3o+Metropolitana+do+Recife,+PE/@-7.9421224,-34.9449702,11.75z?entry=ttu"
x = WebDriver()
print(x.scrape(url))
