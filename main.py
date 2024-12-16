import pytest
import time
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

    username_field = wait.until(
        EC.presence_of_element_located((By.ID, 'loginId'))  
    )
    assert element is not None, "FAIL"
    print("PASS")
    
    username_field.send_keys("lon1553")
    print("PASS")

    password_field = wait.until(
        EC.presence_of_element_located((By.ID, 'password'))  # ID는 로그인 페이지의 실제 ID 값으로 대체
    )
    assert element is not None, "FAIL"
    print("PASS")

    password_field.send_keys("test001!")
    print("PASS")

    element = driver.find_element(By.CLASS_NAME, 'btn-login')
    element.click()
    print("PASS")

    time.sleep(10)