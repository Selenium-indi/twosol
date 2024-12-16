from selenium import webdriver

# 드라이버 경로 없이 실행 (GitHub Actions에서는 자동으로 다운로드)
driver = webdriver.Chrome()
driver.get('https://oliveonedev.cj.net')

#5초 대기


#종료
driver.quit()