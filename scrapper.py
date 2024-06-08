from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_content():

    # Set up the WebDriver (Chrome in this case)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    login(driver, '*****@gmail.com', '******')
    search(driver,"AL30D")
    inside_block(driver)
    search(driver,"AL30C")
    inside_block(driver)


    driver.quit()

def login(driver, username, password):
    # Navigate to the login page
    login_url = 'https://bonds.mercapabbaco.com'
    driver.get(login_url)

    # Wait for the redirection to Auth0 login page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))  # Adjust based on actual form field
    )

    # Fill in the login form
    username_input = driver.find_element(By.XPATH, '//*[@id="username"]')  # Adjust based on actual form field
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')  # Adjust based on actual form field


    username_input.send_keys(username)  # Replace with your actual username
    password_input.send_keys(password)  # Replace with your actual password

    # Submit the form (assuming the password input field is the last one in the form)
    password_input.send_keys(Keys.RETURN)
    print(f"Logged with {username}")

def search(driver, search_term):
    print(f"---- {search_term} ----")
    # Find the input field by placeholder text
    input_placeholder = "Ej.: AL30"  # The placeholder text of the input field

    # Wait for the redirection after login
    # 

    #WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/table/tbody/tr[1]/td[1]/div'))  # Adjust based on actual post-login page element
    #)

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//input[@placeholder="{input_placeholder}"]'))  # Adjust based on actual post-login page element
    )
    
    search_input.send_keys(search_term)


    # Find the first anchor element within the dropdown menu
    first_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.list-group-item.dropdown-item'))
    )

    # Get the text of the first option
    first_option_text = first_option.text
    first_option.click()

    button_search = driver.find_element(By.XPATH, '/html/body/div/div/div/nav/div/div[2]/div[1]/div/div[2]/button')  # Adjust based on actual form field

    button_search.click()

def inside_block(driver):
    titles = [{"name":"TIR","value": ""},{"name":"M. Duration","value": ""},{"name":"Última Cotización","value": ""},{"name":"Paridad","value": ""}]

    for element_info in titles:
        print(f"getting {element_info['name']}")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="card-body"]//h6[contains(text(), "{element_info["name"]}")]//following-sibling::div[@class="h4 card-text"]/span'))
        )

        element_value = element.text
        element_info["value"] = element_value
    
    print(titles)

    # Now you can scrape the protected page
    #dashboard_page = driver.page_source
    #print(dashboard_page)   

    