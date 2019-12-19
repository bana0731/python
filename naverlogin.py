from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#네이버 로그인

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://nid.naver.com/nidlogin.login?mode=form/')
iidd_input = driver.find_element_by_css_selector('#id')
iidd_input.send_keys('7890')
ppww_input = driver.find_element_by_css_selector('#pw')
ppww_input.send_keys('1234')
ppww_input.send_keys(Keys.RETURN)