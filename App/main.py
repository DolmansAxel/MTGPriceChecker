from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from tkinter import Tk
from tkinter import filedialog
from selenium.webdriver.chrome.service import Service

# Function to get the price of a card from Cardmarket using Selenium
def get_card_price(driver, card_name):
    search_url = "https://www.cardmarket.com/en/Magic"
    driver.get(search_url)
    
    # Find the search box and enter the card name
    search_box = driver.find_element(By.NAME, "searchString")
    search_box.send_keys(card_name)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Wait for the results to load
    print("I am sleeping")
    try:
        # Find the price in the search results
        price_element = driver.find_element(By.CSS_SELECTOR, ".table-body .col-price.pe-sm-2")

        price = price_element.text.strip().replace("€", "").replace(",", ".")
        print(f"Price for {card_name}: {price}")
        return float(price)
    except Exception as e:
        print(f"Could not find price for {card_name}: {e}")
        return None



# Use tkinter to open a file dialog and select the Excel file
root = Tk()
root.withdraw()  # Hide the main window
excel_file = filedialog.askopenfilename(
    title="Select Excel File",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

# Check if a file was selected
if not excel_file:
    print("No file selected. Exiting.")
    exit()

# Load the Excel file
df = pd.read_excel(excel_file)

# ...

# Set up the Selenium WebDriver (Chrome in this case)
driver_path = "C:/Users/axeld/Documents/chromedriver.exe"  # Update this path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

df['Price'] = df['Card Name'].apply(lambda name: get_card_price(driver, name))

# ...
df.to_excel("cards_with_prices.xlsx", index=False)

print("Prices have been updated and saved to cards_with_prices.xlsx")

# Close the WebDriver
driver.quit()
