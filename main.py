import requests
from bs4 import BeautifulSoup
# from selenuim import webdriver
import lxml

testUrl = "https://www.nike.com/w/new-mens-3n82yznik1"


# Need to build a function that will navigate to product page.
# def navigateToProductPage(url):
def processData(url):
  try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)

    # Use BeautifulSoup to parse the webpage content
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    # Now that we have the webpage content parsed, let's extract some information
    # For example, let's find all the links (anchor tags) on the webpage
    # links = soup.find_all('a')
    product_name = soup.find_all('div', class_="product-card__title")
    product_price = soup.find_all("div",class_="product-price us__styling is--current-price css-11s12ax")
    print("{:<40} {:<10}".format("Product Name", "Product Price"))
    
    for name, price in zip(product_name, product_price):
      print("{:<40} {:<10}".format(name.text.strip(), price.text.strip()))

  except requests.RequestException as e:
    print(f"Failed to fetch the page: {e}")


# def get_product_name(url, driver_path, element_locator):
#   driver = webdriver.Chrome(executable_path=driver_path)
#   driver.get(url)
#   try:
#     name_element = driver.find_element_by_xpath(element_locator)

#     prod


class Bot:

  def __init__(self):
    self.trackedUrl = []
    self.vistedUrls = []

  def urls(self, url):
    self.trackedUrl.append(url)
    processData(url)
    self.vistedUrls.append(url)


class User:

  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Welcome, {self.name} What are we doing today?\n")
    print("1. Track a website")
    print("2. Track multiply websites")
    print("3. Dash board")
    print("4. Exit\n")

  def interact(self):
    while True:
      user.greet()
      choice = input("Choose your option:\n ")
      if choice == "1":
        url = testUrl
        processData(url)
      elif choice == "2":
        urls = input("Enter url (separated by space, ):")
        # print(urls)
        urls = urls.split(" ")
        for url in urls:
          # print(url)
          processData(url)
      elif choice == "3":
        print("Dash board")
      elif choice == "4":
        print("Closing the program")
        break


print("Please enter your name:")
name = input()
user = User(name)
user.greet()
user.interact()

# processData()
