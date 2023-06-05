from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set the path to the chromedriver executable
webdriver_path = '/Users/snehakumari/Documents/webscraping/chromedriver'

# Set the URL of the web page to scrape
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

# Set up the Chrome webdriver with the specified path
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the web page
driver.get(url)

try:
    # Wait for the Search Postings heading to be visible
    search_postings_heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Search Postings')]"))
    )

    # Scroll to the Search Postings heading to ensure it's in view
    driver.execute_script("arguments[0].scrollIntoView();", search_postings_heading)

    # Find the parent element of the Search Postings heading
    parent_element = search_postings_heading.find_element(By.XPATH, "./..")

    # Find the first 5 postings under the Search Postings heading
    postings = parent_element.find_elements(By.CSS_SELECTOR, "ul > li > a")[:5]

    # Extract the required information from each posting
    for posting in postings:
        try:
            est_value_notes = posting.find_element(By.CSS_SELECTOR, ".est_value_notes").text
        except NoSuchElementException:
            est_value_notes = "N/A"

        try:
            description = posting.find_element(By.CSS_SELECTOR, ".description").text
        except NoSuchElementException:
            description = "N/A"

        try:
            closing_date = posting.find_element(By.CSS_SELECTOR, ".closing_date").text
        except NoSuchElementException:
            closing_date = "N/A"

        # Print the extracted information
        print("Est. Value Notes:", est_value_notes)
        print("Description:", description)
        print("Closing Date:", closing_date)
        print("---")

finally:
    # Quit the webdriver
    driver.quit()
