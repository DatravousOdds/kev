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



# Need to build a function that will navigate to product page.
# def navigateToProductPage(url):
def processData(url):
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


def filterShoes(preferences, product_details):
  shoe_name = None

  # Filtering shoes based on user preferences
  for name, _ in product_details:
    print(name.text)
    # if preferences['type'] in name.text.lower() and preferences['size']:
  


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
      self.greet()
      choice = input("Choose your option:\n")
      if choice == "1":
        url = testUrl
        product_details = processData(url)
        # Get user preference for product
        gender = input("Women or Men Sneakers?: ")
        shoeSize = input("What is your shoe size?: ")

        preferences = {'type': gender, 'size': shoeSize}

      elif choice == "2":
        urls = input("Enter url (separated by space, ):")
        # print(urls)
        urls = urls.split(" ")
        for url in urls:
          print(url)
          product_details = processData(url)
      elif choice == "3":
        print("Dash board")
      elif choice == "4":
        print("Closing the program")
        break


print("Please enter your name:")
name = input()
user = User(name)
user.interact()
