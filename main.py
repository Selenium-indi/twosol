from selenium import webdriver

# 드라이버 경로 없이 실행 (GitHub Actions에서는 자동으로 다운로드)
driver = webdriver.Chrome()
driver.get('https://oliveyoung.co.kr')

#5초 대기
time.sleep(5)

#종료
driver.quit()