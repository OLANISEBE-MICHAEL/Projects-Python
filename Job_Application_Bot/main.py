import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

def abort_application():
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()
    dismiss_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[0]
    dismiss_button.click()

# LinkedIn URL
URL = "https://www.linkedin.com/feed/"

# Setup Chrome options
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(URL)
driver.maximize_window()

# Environment credentials
linkedin_details = {
    "email": os.environ.get("email"),
    "password": os.environ.get("password"),
    "phone_number": os.environ.get("number")
}

try:
    # Enter email and password
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
            "/html/body/div/main/div[2]/div[1]/form/div[1]/input"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
            "/html/body/div/main/div[2]/div[1]/form/div[2]/input"))
    )

    email_input.send_keys(linkedin_details["email"])
    password_input.send_keys(linkedin_details["password"])
    password_input.send_keys(Keys.ENTER)

    # Wait for manual CAPTCHA completion
    input("Press Enter when you have solved the Captcha")

    # Click on job button to get to jobs page to search for job
    job_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#global-nav > div > nav > ul > li:nth-child(3)"))
    )
    job_button.click()

    search_job_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]"))
    )
    search_job_input.send_keys("Python Intern")
    search_job_input.send_keys(Keys.ENTER)

    # Filter the job offers based on easy-apply
    easy_apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchFilter_applyWithLinkedin"))
    )
    easy_apply_button.click()

    # Allow job cards to load
    time.sleep(15)
    all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

    for index, job in enumerate(all_jobs):
        print(f"Applying to job {index + 1} of {len(all_jobs)}")
        job.click()
        time.sleep(3)

        try:
            apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
            apply_button.click()
            time.sleep(5)

            # Fill phone number if not filled
            phone_number_input = driver.find_elements(By.XPATH,
                "/html/body/div[4]/div/div/div[2]/div/div/form/div/div[1]/div[4]/div/div/div[1]/div/input"
            )
            if phone_number_input:
                phone = phone_number_input[0]
                if phone.get_attribute("value") == "":
                    phone.send_keys(linkedin_details["phone_number"])
            else:
                print("No phone number input found.")
                abort_application()
                continue

            # Check if the application is multi-step
            submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if submit_button.get_attribute("aria-label") == "Continue to next step":
                print("Complex application. Skipping.")
                abort_application()
                continue
            else:
                submit_button.click()
                print("Application submitted.")
                time.sleep(2)

                # Close modal
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()

        except NoSuchElementException:
            print("Apply button not found. Skipping.")
            continue

except TimeoutException:
    print("Initial elements took too long to load.")
except ElementNotInteractableException:
    print("An element could not be interacted with.")
