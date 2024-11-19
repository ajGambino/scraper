from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the URL
    url = "https://www.rotowire.com/daily/nba/optimizer.php"
    driver.get(url)

    # Wait for the table to load
    wait = WebDriverWait(driver, 20)
    table = wait.until(EC.presence_of_element_located((By.ID, "player-pool-table")))

    # Locate the scrollable container
    scrollable_div = driver.find_element(By.CSS_SELECTOR, ".overflow-y-scroll")

    # Initialize variables
    last_height = 0
    data = {}
    scroll_attempts = 0

    while True:
        # Get all visible rows
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            try:
                # Extract PLAYER and FPTS
                player_cell = row.find_element(By.CSS_SELECTOR, "a")
                player_name = player_cell.text.strip()
                player_href = player_cell.get_attribute("href")  # Unique identifier

                fpts_input = row.find_element(By.CSS_SELECTOR, "input[type='number']")
                fpts_value = fpts_input.get_attribute("value").strip()

                # Add to data if not already present
                if player_href not in data:
                    data[player_href] = (player_name, fpts_value)
            except Exception as e:
                print(f"Skipping row due to error: {e}")

        # Scroll down slightly
        driver.execute_script("arguments[0].scrollTop += 100", scrollable_div)
        time.sleep(1)  # Allow time for rows to render

        # Check if scrolling is complete
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0
        last_height = new_height

        # Stop if scrolling hasn't added new content after 5 attempts
        if scroll_attempts >= 5:
            break

    # Save the data to a CSV file
    csv_file = 'rotowire.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['PLAYER', 'FPTS'])  # Header
        writer.writerows(data.values())  # Data rows

    print(f"Data saved to {csv_file} with {len(data)} rows.")

finally:
    # Close the browser
    driver.quit()
