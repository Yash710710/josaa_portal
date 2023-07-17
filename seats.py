import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

# Set the path to chromedriver
chromedriver_path = "E:\Josaa_PROJECT\chromedriver"  # Replace with your actual path to chromedriver

# Set the options for Chrome webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode, remove this line if you want to see the browser
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Create a new Chrome webdriver instance
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Define the URL
url = "https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx"

# Load the webpage
driver.get(url)

# Click on the dropdown menu to expand it
dropdown = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstType_chosen")
dropdown.click()

# Find the desired option by its text and click on it
desired_option_text = "Institute Type"
options = driver.find_elements(By.CSS_SELECTOR, ".chosen-results li")
for option in options:
    if option.text.strip() == desired_option_text:
        option.click()
        break

# Scroll down to the submit button using JavaScript
submit_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
actions = ActionChains(driver)
actions.move_to_element(submit_button).perform()

# Click the submit button
driver.execute_script("arguments[0].click();", submit_button)

# Wait for the table to load
wait = WebDriverWait(driver, 10)
table_element = wait.until(EC.presence_of_element_located((By.ID, "GridView1")))

# Extract data from the table
soup = BeautifulSoup(driver.page_source, "html.parser")
tables = soup.find("table", id="GridView1")

row1 = tables.find_all('th')[:]
rows = tables.find_all("tr")[1:]



data1 = []
data2 = []
row_d = [cell.text.strip() for cell in row1]
data1.append(row_d)

for row in rows:
    cells = row.find_all("td")
    if cells and len(cells) > 2:
        if 'Female-only (including Supernumerary)' in cells[0].text.strip():
            row_data2 = [cell.text.strip() for cell in cells]
            data2.append(row_data2)
        else:
            row_data1 = [cell.text.strip() for cell in cells]
            data1.append(row_data1)

# Create a DataFrame and print it
df1 = pd.DataFrame(data1)
print(df1)
df2 = pd.DataFrame(data2)
print(df2)

# Save the DataFrame to a CSV file
df1.to_csv("seatsall.csv", index=False)
df2.to_csv("seatfemale.csv", index=False)


# Quit the webdriver
driver.quit()
