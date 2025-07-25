import time
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the driver with undetected Chrome
driver = Driver(uc=True, headless=False)

# Open the game
url = "https://orteil.dashnet.org/cookieclicker/"
driver.uc_open_with_reconnect(url, reconnect_time=6)

timeout = time.time() + 5
five_mins = time.time() + 60 * 5


# Optional: Maximize window
driver.maximize_window()

# Wait for language selection button
try:
    eng_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    eng_button.click()
    print("✅ English language selected.")
except TimeoutException:
    print("⚠️ No language selection found (maybe skipped automatically).")

# Wait for the big cookie to appear
try:
    big_cookie = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    print("✅ Game loaded.")
except TimeoutException:
    print("❌ Failed to load the game or find the cookie.")
    driver.quit()
    exit()

while True:
    big_cookie.click()

    if time.time() > timeout:
        try:
            # obtaining number of cookies
            cookie = driver.find_element(By.ID, value="cookies")
            cookie_text = cookie.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # obtain product prices
            print("getting product prices...")
            products = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='product']"))
            )
            # find best price
            best_price = ""
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_price = product
                    break

            if best_price:
                best_price.click()

        except (NoSuchElementException, ValueError):
            print("Product or item not found")

        # reset timer
        timeout = time.time() + 5

    # stop timer
    if time.time() > five_mins:
        try:
            cookie = driver.find_element(By.ID, value="cookies")
            print(f"Final cookie: {cookie.text}")
        except NoSuchElementException:
            print("cookie element not found")
        break




# Done – you can keep the browser open or close it
# driver.quit()  # Uncomment to close automatically
