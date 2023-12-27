import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import lxml

testUrl = "https://www.nike.com/"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get(testUrl)

# TODO: Need to build a function that will navigate to product page.

# TODO: Filter out shoes that don't match the preferences.


class Bot:

  def __init__(self):
    self.trackedUrl = []
    self.vistedUrls = []

  def processData(self, url):
    try:
      r = requests.get(url)
      r.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)

      # Use BeautifulSoup to parse the webpage content
      soup = BeautifulSoup(r.text, 'lxml')

      product_name = soup.find_all('div', class_="product-card__title")
      
      product_price = soup.find_all(
          "div",
          class_="product-price us__styling is--current-price css-11s12ax")
      product_details = zip(product_name, product_price)
      # print(product_details)

      # Printing product details
      print("{:<40} | {:<10}".format("Product Name", "Product Price"))
      print("-" * 60)

      for name, price in product_details:
        print("{:<40} | {:<10}".format(name.text.strip(), price.text.strip()))
      # print(product_details)
      return product_details  # Return poduct details for further processing

    except requests.RequestException as e:
      print(f"Failed to fetch the page: {e}")

  def urls(self, url):
    self.trackedUrl.append(url)
    self.vistedUrls.append(url)


class User:

  def __init__(self, name, email):
    self.name = name
    self.email = email

  def greet(self):
    print(f"Welcome, {self.name} What are we doing today?\n")
    print("1. Track a website")
    print("2. Track multiply websites")
    print("3. Dash board")
    print("4. Exit\n")

  def interact(self):
    while True:
      self.greet()
      choice = input("Choose your option:\n")
      if choice == "1":
        url = testUrl  # Gets url to track
        driver.get(url)
        categoryChoice = driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header-v2"]/div[3]/header/div[1]/div[2]/nav/div[2]/div/ul/li[2]/a')
        categoryChoice.click()
        menCategory = driver.find_element_by_xpath('//*[@id="08fa77c7-66ea-4345-a592-cb13c26e1a34"]/div/section/ul/li[2]/figure/a')
        menCategory.click()
      elif choice == "2":
        urls = input("Enter url (separated by space, ):")
        # print(urls)T
        urls = urls.split(" ")
        for url in urls:
          print(url)
          # product_details = processData(url)
      elif choice == "3":
        print("Dash board")
      elif choice == "4":
        print("Closing the program")
        break

  def get_perferences(self):
    print("What are your preferences?")
    gender = input("Gender: ")
    shoeSize = input("Shoe size: ")
    # print(gender)
    # print(shoeSize)


name = input("Please enter your name:\n")
email = input("Please enter your email:\n")
user = User(name, email)
user.interact()
