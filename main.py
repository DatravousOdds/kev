import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import lxml
import json


testUrl = "https://www.nike.com/"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get(testUrl)


# TODO: Need to build a function that will navigate to product page.
def naviagteToProductPage(url):
  try:
    driver.get(url)
  except Exception as e:
    print(f'Error occur when navigatin to the page: {e}')


# TODO: Filter out shoes that don't match the preferences.

# TODO: Build a function that select item base off user preferences.


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

      # Printing product details
      print("{:<40} | {:<10}".format("Product Name", "Product Price"))
      print("-" * 60)

      for name, price in product_details:
        print("{:<40} | {:<10}".format(name.text.strip(), price.text.strip()))

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
    self.bot = Bot()

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
        url = testUrl  # Gets the URL input from the user
        self.bot.urls(url)
        naviagteToProductPage(url)
      elif choice == "2":
        urls = input("Enter url (separated by space, ):")
        urls = urls.split(" ")
        for url in urls:
          print(url)
      elif choice == "3":
        print("Dash board")
      elif choice == "4":
        print("Closing the program")
        break

  def get_perferences(self):
    print("What are your preferences?")
    gender = input("Gender: ")
    shoeSize = input("Shoe size: ")
    shoeName = input("Shoe name: ")
    return gender, shoeSize, shoeName


name = input("Please enter your name:\n")
email = input("Please enter your email:\n")
user = User(name, email)
user.interact()
