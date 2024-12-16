import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_element_presence(setup):
    driver = setup
    driver.get('https://oliveyoung.co.kr')

    wait = WebDriverWait(driver, 10, poll_frequency=2)

    element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'login'))
    )
    assert element is not None, "FAIL"
    print("PASS")

    element.click()
    print("PASS")