from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\boy10\Desktop\git\private\macro\Include\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://www.naver.com')

# https://yonoo88.tistory.com/1200