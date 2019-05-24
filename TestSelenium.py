from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.get("http://www.bidue.com")
driver.get("http://www.google.com")

driver.maximize_window()

#找到元素element按右鍵也可copy xpath

driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input").send_keys('Mac\n')
#driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()
#driver.find_element_by_name('q').send_keys('Mac\n')

#driver.save_screenshot('Google.png')
